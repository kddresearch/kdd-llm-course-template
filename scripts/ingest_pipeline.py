import os
import re
import pandas as pd
import torch
import requests
from bs4 import BeautifulSoup
import fitz  # PyMuPDF
from transformers import pipeline
import yt_dlp

class SovereignIngestor:
    def __init__(self, md_path: str, output_dir: str = "extracted_corpus"):
        self.md_path = md_path
        self.output_dir = output_dir
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        os.makedirs(self.output_dir, exist_ok=True)
        
        print(f"[INIT] Hardware detected: {self.device}")
        if self.device != "cpu":
            print(f"[INIT] GPU: {torch.cuda.get_device_name(0)}")

        # Lazy-load models to save VRAM on local RTX cards
        self.whisper_pipeline = None

    def load_whisper(self):
        """Loads Whisper-v3-turbo explicitly for the Video transcription track."""
        if not self.whisper_pipeline:
            print("[LOAD] Initializing Whisper-v3-turbo for video extraction...")
            self.whisper_pipeline = pipeline(
                "automatic-speech-recognition",
                model="openai/whisper-large-v3-turbo",
                torch_dtype=torch.float16 if self.device != "cpu" else torch.float32,
                device=self.device
            )

    def parse_markdown_table(self):
        """Extracts the seed corpus into a Pandas DataFrame."""
        with open(self.md_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Filter markdown table rows
        rows = [re.split(r'\s*\|\s*', line.strip())[1:-1] for line in lines if line.startswith('|') and '---' not in line]
        headers = rows[0]
        data = rows[1:]
        
        df = pd.DataFrame(data, columns=headers)
        return df

    def extract_html(self, url: str) -> str:
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Strip scripts and styles
            for script in soup(["script", "style", "nav", "footer"]):
                script.decompose()
            return soup.get_text(separator='\n', strip=True)
        except Exception as e:
            return f"[ERROR] HTML Extraction failed: {str(e)}"

    def extract_pdf(self, url: str) -> str:
        try:
            response = requests.get(url, stream=True, timeout=10)
            pdf_path = os.path.join(self.output_dir, "temp.pdf")
            with open(pdf_path, 'wb') as f:
                f.write(response.content)
                
            doc = fitz.open(pdf_path)
            text = "\n".join([page.get_text() for page in doc])
            doc.close()
            os.remove(pdf_path)
            return text
        except Exception as e:
            return f"[ERROR] PDF Extraction failed: {str(e)}"

    def extract_video(self, url: str) -> str:
        self.load_whisper()
        audio_path = os.path.join(self.output_dir, "temp_audio")
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': audio_path + '.%(ext)s',
            'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3'}],
            'quiet': True
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            print(f"       -> Transcribing audio...")
            result = self.whisper_pipeline(audio_path + ".mp3", return_timestamps=False)
            os.remove(audio_path + ".mp3")
            return result['text']
        except Exception as e:
            return f"[ERROR] Video Transcription failed: {str(e)}"

    def run_pipeline(self):
        df = self.parse_markdown_table()
        print(f"[START] Processing {len(df)} canonical sources...\n")
        
        for index, row in df.iterrows():
            doc_id = row['ID']
            url = row['URL']
            fmt = row['Format']
            
            print(f"[{doc_id}] Routing format: {fmt} -> {url}")
            
            if fmt == 'HTML':
                content = self.extract_html(url)
            elif fmt == 'PDF':
                content = self.extract_pdf(url)
            elif fmt == 'Video':
                content = self.extract_video(url)
            else:
                content = f"[ERROR] Unsupported format: {fmt}"
                
            # Save raw extracted text
            out_path = os.path.join(self.output_dir, f"{doc_id}_{row['Category']}.txt")
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(content)

        print("\n[COMPLETE] All extractions saved to output directory.")

if __name__ == "__main__":
    # Point this to the markdown file saved above
    ingestor = SovereignIngestor(md_path="seed_corpus.md", output_dir="kdd_raw_corpus")
    ingestor.run_pipeline()