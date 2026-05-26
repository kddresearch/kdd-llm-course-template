# vLLM Serving Runbook: Lab GPU Cluster
**Status:** Placeholder / Draft
**Target:** Zone 2 (KDD Lab 16x NVIDIA A40 Cluster)

## 1. vLLM Engine Architecture
vLLM utilizes PagedAttention to manage the KV Cache. It is strictly required for multi-user inference serving. Ollama is not permitted in Zone 2.

## 2. Bootstrapping the Server
* [TODO: Insert `docker run` command for the `vllm/vllm-openai` container]
* [TODO: Document VRAM utilization flags (e.g., `--gpu-memory-utilization 0.9`)]
* [TODO: Document quantization targets (AWQ required for Zone 2)]

## 3. Dynamic LoRA Routing
vLLM can serve the base model while dynamically applying different student LoRA adapters (trained in Module 5) on a per-request basis.
* [TODO: Insert `--enable-lora` command parameters]
* [TODO: Provide example Python `requests` payload targeting a specific adapter ID]