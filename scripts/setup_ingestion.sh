#!/bin/bash
# KDD Lab: Zone 1 Ingestion Environment Bootstrap

echo "[1/4] Creating directories..."
mkdir -p scripts data

echo "[2/4] Updating .gitignore..."
grep -qxF 'kdd_raw_corpus/' .gitignore || echo "kdd_raw_corpus/" >> .gitignore
grep -qxF 'temp.pdf' .gitignore || echo "temp.pdf" >> .gitignore
grep -qxF 'temp_audio*' .gitignore || echo "temp_audio*" >> .gitignore

echo "[3/4] Updating requirements.txt..."
for pkg in pandas transformers yt-dlp pymupdf beautifulsoup4 accelerate; do
    grep -qxF "$pkg" requirements.txt || echo "$pkg" >> requirements.txt
done

echo "[4/4] Setup complete. Ready for git commit."