# KDD Lab Sovereign Stack Manifest
**Term:** Spring 2026
**Status:** Canonical Topology

## 1. The 3-Zone Compute Topology
To ensure exact portability of AI pipelines and zero reliance on closed-source APIs, infrastructure is divided into three execution zones:

* **Zone 1 (Local Prototyping):** * *Hardware:* Student laptop/workstation (8-16GB VRAM minimum).
    * *Engine:* Docker Desktop/Engine + Ollama.
    * *Precision:* GGUF (INT4/INT8).
    * *Use Case:* DevContainer bootstrapping, strict grammar/schema development, and unit testing single inference calls.
* **Zone 2 (Lab GPU Cluster):** * *Hardware:* KDD Lab 16x NVIDIA A40 (48GB VRAM each).
    * *Engine:* vLLM via SSH.
    * *Precision:* AWQ or FP16 (pipeline-parallel for 70B+ models).
    * *Use Case:* High-throughput dataset processing, continuous batching, and dynamic LoRA adapter routing.
* **Zone 3 (HPC & Extreme Scale):** * *Hardware:* Beocat (K-State) & PSC Bridges-2.
    * *Engine:* Apptainer (`.sif`) + Slurm (`sbatch`).
    * *Use Case:* Unquantized base model fine-tuning (Axolotl/QLoRA) and massive parallel inference.

## 2. The Spring 2026 Model Stack (M=10)
All tasks must be routed to local models based on their capability niche. No cloud APIs are permitted. The baseline hardware unit is a single A40 (48GB); models ≥70B must be quantized or sharded.

| Niche / Capability | Model (Exact Version / Size) | Why This Model (Closest Competitor to Big-Three) |
| :--- | :--- | :--- |
| **1. General Reasoning (CoT, analysis)** | `DeepSeek-R1-Distill-Qwen-32B` | Primary reasoning engine. Closest open competitor to GPT-o1/Gemini reasoning depth; transparent CoT; fits on A40 unquantized. |
| **2. General Chat / Assistant** | `Llama 3.3-70B-Instruct (4-bit)` | Most "Claude-like" open model; strong writing, tone, and safety-steering via system prompts. |
| **3. Hardcore Coding & Math** | `Qwen 2.5-Coder-32B` | Beats GPT-4-class models on many code benchmarks; ideal for REPL/agent tool use. |
| **4. Agent Routing & High-Throughput** | `Mixtral 8x7B-Instruct` | MoE speed; excellent for LangGraph multi-agent routing and high-volume retrieval parsing. |
| **5. Image Generation** | `Flux.1-dev-12B` | Best open model for text rendering; closest to DALL-E 3/Gemini image quality in open weights. |
| **6. Speech Recognition** | `Whisper-v3-turbo` | *Updated from v3-Large.* Identical accuracy but significantly faster for batch transcript processing. |
| **7. Video Generation** | `Wan 2.2-A14B` | SOTA open video generator; cinematic motion; fits entirely on a single A40. |
| **8. Video / Visual Analysis** | `Qwen2.5-VL-72B (4-bit, PP)` | Closest open competitor to Gemini 2.0 Flash / GPT-4o vision. Heavy-duty visual reasoning. |
| **9. Document / OCR / Math Vision** | `Llama 3.2-Vision-90B (4-bit, PP)` | Complements Qwen-VL; excels at structured PDFs, charts, and math extraction. |
| **10. Local Search / RAG / Retrieval** | `Jina-Embeddings-v3-Large` | High-quality embeddings for sovereign RAG; replaces Perplexity-style retrieval architectures. |

*(Note: Zone 1 testing utilizes `mistral:7b` strictly for Lab 1.0 and 2.0 API connectivity checks due to laptop VRAM constraints).*