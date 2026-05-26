# KDD Lab LLM Short Course: Lab & Runbook Oracle Specifications
**Master Repository:** `https://github.com/kddresearch/kdd-llm-course-template`
**Pacing:** Self-Paced (Module-based progression, independent of weekly schedules)

---

## MODULE 1: Environment & Reproducibility

### Lesson 1.1 - 1.2: Host Substrate & DevContainers
The Gem must enforce the exact DevContainer and Compose setups. Students are not permitted to use native Windows/Mac environments.

**Required `devcontainer.json` Spec:**
    {
      "name": "KDD-LLM-Workspace",
      "image": "mcr.microsoft.com/devcontainers/python:3.11",
      "features": {
        "ghcr.io/devcontainers/features/docker-outside-of-docker:1": {}
      },
      "customizations": {
        "vscode": {
          "extensions": ["ms-python.python", "ms-toolsai.jupyter"]
        }
      },
      "postCreateCommand": "pip install -r requirements.txt"
    }

**Required `docker-compose.yml` (Ollama MVP):**
    version: '3.8'
    services:
      ollama:
        image: ollama/ollama:latest
        ports:
          - "11434:11434"
        volumes:
          - ollama_data:/root/.ollama
        deploy:
          resources:
            reservations:
              devices:
                - driver: nvidia
                  count: 1
                  capabilities: [gpu]
    volumes:
      ollama_data:

### Lesson 1.3 / Lab 1.0: Baseline Run Card
**Objective:** Confirm Zone 1 environment integrity. Throughput benchmarking is explicitly excluded from this lab and reserved for Lab 2.0.
**Acceptance Criteria (DG 0-4 Cleared):**
1. The student's `lab_1_0_baseline.ipynb` commit must contain an `nvidia-smi` output block showing VRAM allocation.
2. The notebook must contain a successful `requests.get("http://localhost:11434/api/tags")` returning HTTP 200.
3. The notebook must contain a successful basic generation request proving the `mistral` or `llama3` weights were pulled to the persistent volume.

---

## MODULE 2: Inference & Systems Intuition

### Lesson 2.1 - 2.2: Math & Memory Calculus
**Key Concept:** The KV Cache formula. The Gem must use this to debug student OOM errors:
`Memory ≈ 2 × Context × Batch Size × Hidden Dim × Layers × Precision`
**Quantization Standard:** Zone 1 uses GGUF (INT4/INT8). Zones 2/3 use AWQ for vLLM compatibility.

### Lesson 2.3 / Lab 2.0: Inference Parameter Sweep
**Objective:** Programmatic grid search mapping determinism and a from-scratch NumPy attention matrix.
**Acceptance Criteria:**
1. **The Parameter Sweep:** A nested loop utilizing `requests.post` against the Ollama API testing `temperature = [0.1, 0.8, 1.5]` and `top_p = [0.5, 0.9]`. Output must be a Pandas DataFrame.
2. **The Attention Implementation:** The notebook must contain this exact mathematical proof executed in NumPy:
    import numpy as np

    def scaled_dot_product_attention(Q, K, V):
        d_k = Q.shape[-1]
        scores = np.matmul(Q, K.swapaxes(-1, -2)) / np.sqrt(d_k)
        exp_scores = np.exp(scores - np.max(scores, axis=-1, keepdims=True))
        attention_weights = exp_scores / np.sum(exp_scores, axis=-1, keepdims=True)
        output = np.matmul(attention_weights, V)
        return output, attention_weights

3. **Observation:** Written confirmation that `T=0.1` yields deterministic extraction, while `T=1.5` causes structural hallucinations.

---

## MODULE 3: RAG & Prompt Engineering

### Lesson 3.1: The Anatomy of a Prompt
**Core Mechanic:** Chain-of-Thought (CoT). For models like `DeepSeek-R1-Distill-Qwen-32B`, the Gem must look for the explicit enforcement of `<think></think>` tags in the student's system prompts to ensure reasoning traces are output prior to final JSON strings.

### Lesson 3.2 - 3.3 / Lab 3.0: Strictly Typed JSON Extraction
**Objective:** Zero `JSONDecodeError`s across 50 iterations on noisy text.
**Acceptance Criteria:**
1. **The Schema:** The student must define a strict `Pydantic` architecture. Example oracle schema:
    from pydantic import BaseModel, Field

    class PatientExtraction(BaseModel):
        patient_id: str = Field(description="Alphanumeric ID")
        diagnosis: str
        confidence_score: float = Field(ge=0.0, le=1.0)

2. **The Execution:** Code utilizing Ollama's `format: json` parameter or the `Instructor` library.
3. **The Deliverable:** A Failure Taxonomy Report pushed to GitHub documenting exact fail states of greedy/unconstrained generation vs. grammar-constrained generation.

---

## MODULE 4: Agentic Retrieval & Evaluation

### Lesson 4.1 - 4.2: Vector Orchestration
Students must add Qdrant to their `docker-compose.yml`. 
**Qdrant Injection:**
      qdrant:
        image: qdrant/qdrant:latest
        ports:
          - "6333:6333"
          - "6334:6334"
        volumes:
          - qdrant_storage:/qdrant/storage

### Lesson 4.3 / Lab 4.0: Programmatic RAG Evaluation (DG 5)
**Objective:** Code-based evaluation of the RAG Triad. Eyeballing results is an automatic failure.
**Acceptance Criteria (DG 5 Cleared):**
1. Multi-node orchestration confirmed (Workspace container communicating with Qdrant container).
2. The student uses `fastembed` (Jina-v3) or equivalent to chunk and embed a target PDF.
3. The student executes an evaluation using **TruLens** or **Ragas**.
4. The notebook must output a dataframe showing scores `> 0.85` across the Triad:
   - Context Precision / Relevance
   - Faithfulness (Groundedness)
   - Answer Relevance

## MODULE 5: Fine-Tuning on HPC

### Lesson 5.1 - 5.2: Declarative Tuning
**Objective:** Transition from prompt engineering to weight adaptation using Axolotl.
**Acceptance Criteria:**
1. The student must utilize an `axolotl` declarative YAML configuration.
2. The `qlora.yml` runbook must target an appropriate Zone 3 model (e.g., DeepSeek-R1-Distill or Llama 3.3).
**Required `qlora.yml` Spec:**
    base_model: deepseek-ai/DeepSeek-R1-Distill-Qwen-32B
    adapter: qlora
    load_in_4bit: true
    sequence_len: 4096
    lora_r: 32
    lora_alpha: 16
    lora_target_modules:
      - q_proj
      - v_proj
    gradient_accumulation_steps: 4
    micro_batch_size: 2
    learning_rate: 0.0002

### Lesson 5.3 / Lab 5.0: The Apptainer Bridge (DG 6)
**Objective:** Execute the tuning run on HPC.
**Acceptance Criteria (DG 6 Cleared):**
1. Docker image successfully converted to `.sif`.
2. A valid Slurm batch script (`.sbatch`) is committed, explicitly requesting GPU allocation and binding the scratch workspace:
    #!/bin/bash
    #SBATCH --job-name=axolotl_qlora
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --gres=gpu:a40:4
    #SBATCH --mem=128GB
    #SBATCH --time=24:00:00
    
    apptainer exec --nv --bind /scratch:/workspace kdd_axolotl.sif \
        accelerate launch -m axolotl.cli.train qlora.yml
3. A verified loss curve (TensorBoard or Weights & Biases export) is pushed to the repo showing convergence.

---

## MODULE 6: Serving & Governance

### Lesson 6.1 - 6.2: vLLM Deployment
**Objective:** Scale the inference engine for multi-user, continuous batching.
**Acceptance Criteria:**
1. The student replaces Ollama with vLLM in Zone 2.
2. The deployment command must explicitly map the LoRA adapter trained in Module 5:
    python -m vllm.entrypoints.openai.api_server \
        --model deepseek-ai/DeepSeek-R1-Distill-Qwen-32B \
        --enable-lora \
        --lora-modules my_adapter=/path/to/lora

### Lesson 6.3 / Lab 6.0: AI RMF Risk Register (DG 7)
**Objective:** Map technical pipelines to the NIST AI RMF.
**Acceptance Criteria (DG 7 Cleared):**
1. The vLLM server must be actively orchestrating the API endpoint.
2. The student commits `risk_register_v1.md`, documenting specific hazards related to their intended Capstone dataset across Map, Measure, and Manage functions.

---

## MODULE 7: Orchestration

### Lesson 7.1 - 7.2: LangGraph Workflows
**Objective:** Build cyclical, stateful agents rather than linear scripts.
**Acceptance Criteria:**
1. The notebook must define a strict `TypedDict` for State management.
    from typing import TypedDict, Annotated
    import operator

    class AgentState(TypedDict):
        messages: Annotated[list, operator.add]
        extracted_data: dict
        retries: int
2. The graph must contain conditional routing edges (e.g., routing back to a retrieval node if validation fails).

### Lesson 7.3 / Lab 7.0: Graph Execution Trace (DG 8)
**Acceptance Criteria (DG 8 Cleared):**
1. The multi-node agent graph compiles successfully.
2. The student pushes an execution trace confirming the agent successfully utilized a tool (e.g., querying Qdrant) and synthesized an answer without getting stuck in an infinite routing loop.

---

## MODULE 8: Biomedical Extraction Capstone

### Lesson 8.1 - 8.3 / Lab 8.0: The 7-Stage Pipeline
**Objective:** Final integration of all course modules tailored to the student's 5x4 Project Matrix coordinate. The oracle exemplar is the Track A (Clinical) / NL (Natural Language) coordinate targeting psychoactive substance misuse.
**Acceptance Criteria:**
1. **Multimodal Ingestion:** Pipeline successfully handles unstructured sources (OCR from images, Whisper transcripts, or raw web scraping).
2. **Tokenizer Stress Testing:** The extraction constraints must not break when confronted with specialized out-of-distribution subculture linguistics (e.g., correctly parsing and retaining terms like *Fànquān*, or anomalous concepts like *CTHULHU* and *shoggoths* without hallucinating formatting).
3. **Ontology Grounding:** Output data must be normalized against established taxonomies (e.g., standardizing street drug names to active chemical compounds).
4. **Final Deliverables:**
    - Fully reproducible Python Runbook.
    - Evaluation Report utilizing programmatic metrics (F1 scores, Ragas Triad).
    - Validated CSV export of the targeted entities.