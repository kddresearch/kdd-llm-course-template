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
    * *Precision:* AWQ or FP16.
    * *Use Case:* High-throughput dataset processing, continuous batching, and dynamic LoRA adapter routing.
* **Zone 3 (HPC & Extreme Scale):** * *Hardware:* Beocat (K-State) & PSC Bridges-2.
    * *Engine:* Apptainer (`.sif`) + Slurm (`sbatch`).
    * *Use Case:* Unquantized base model fine-tuning (Axolotl/QLoRA) and massive parallel inference.

## 2. The Spring 2026 Model Stack
Zero reliance on closed-source APIs (OpenAI, Anthropic, Google). Pipelines must utilize these designated open-weight models:

* **Reasoning/Math:** `DeepSeek-R1-Distill-Qwen-32B` (Requires explicit `<think>` tag parsing).
* **Dialogue/Instruction:** `Llama 3.3-70B`
* **Coding/Environment:** `Qwen 2.5-Coder`
* **Routing/Multi-Agent:** `Mixtral 8x7B`
* **Multimodal/Perception:** `Qwen2.5-VL`, `Llama 3.2-Vision`
* **Embeddings:** `jina-v3` (via FastEmbed)
* **Baseline/Testing (Zone 1):** `mistral:7b` (Used strictly for Lab 1.0 and 2.0 API connectivity checks).