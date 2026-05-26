# KDD Lab LLM Short Course: Master Syllabus & Course Matrix
**Term:** Spring 2026
**Host:** Kansas State University, Knowledge Discovery in Databases (KDD) Lab
**Instructor:** Dr. William H. Hsu
**Target Audience:** Graduate Research Assistants (GRAs) and sovereign research engineers.
**Repository:** `kddresearch/kdd-llm-course-template`

---

## Part 1.0: Operational Topologies & The GitOps Mandate

### 1.1 The Single Source of Truth (SSOT)
This course does not utilize static Canvas modules for code distribution. All structural configuration, environment variables, and execution logic are handled via Git version control. 
- **Upstream:** `kddresearch/kdd-llm-course-template` acts as the curriculum substrate.
- **Downstream:** Each student maintains a strictly isolated, branched repository.
- **Canvas:** Used strictly as a signaling mechanism for GitHub commit hashes (Assignment submissions) and static policy announcements.

### 1.2 The "Keep Flying" Protocol
Hardware and environment failures are expected. Students must operate under the "Keep Flying" Protocol:
- **Maximum Blocked Time (dt):** 24 calendar hours.
- **Action at Limit:** If blocked for >24h on a deployment or execution step, the student MUST stop thrashing, commit current state, and file an Access Blocker Report (ABR) to their repository issues list.
- **Immediate Pivot:** Upon filing an ABR, the student immediately pivots to conceptual schema design, reading canonical documentation, or data curation. Do not stall.

### 1.3 The 3-Zone Compute Model
To ensure exact portability of AI pipelines, infrastructure is divided into three execution zones.
- **Zone 1 (Local MVP):** DevContainers, Docker Engine/Desktop, Ollama. Used for strict grammar/schema development and unit testing inference scripts. (Constraints: 8-16GB VRAM, GGUF/AWQ quantized models).
- **Zone 2 (Lab GPU Cluster):** 16 x NVIDIA A40 (48GB VRAM each). Accessible via SSH. Deployment utilizes vLLM for continuous batching and Axolotl for adapter training. Used for full-throughput dataset processing.
- **Zone 3 (HPC & Commercial Clouds):** PSC Bridges-2, Beocat, AWS, RunPod. Migrating Docker containers to Apptainer (`.sif`) for Slurm queue job submission. Used for unquantized base model fine-tuning and massive parallel inference.

### 1.4 Sovereign Model Stack (Spring 2026)
Zero reliance on closed-source APIs (OpenAI, Anthropic, Google).
- **Reasoning/Math:** DeepSeek-R1-Distill-Qwen-32B
- **Dialogue/Instruction:** Llama 3.3-70B
- **Coding/Environment:** Qwen 2.5-Coder
- **Routing/Multi-Agent:** Mixtral 8x7B
- **Multimodal/Perception:** Qwen2.5-VL, Llama 3.2-Vision
- **Embeddings:** Jina-v3

---

## Part 2.0: Phase I - Foundations (Modules 1 & 2)

Phase I establishes the immutable execution environment. Students will not write pipeline logic until Docker Gates 0-4 are cleared.

### Module 1: Environment & Reproducibility

**Lesson 1.1: Host Substrate & The Containerization Boundary**
- **Objective:** Configure the host OS to pass hardware interrupts to the container daemon.
- **Linux/WSL2 Architecture:** Bypassing Windows limitations using the Windows Subsystem for Linux.
- **Docker Engine vs. Desktop:** Memory allocation overrides and network bridging.
- **NVIDIA Container Toolkit:** Installing `nvidia-container-toolkit` to expose host GPUs to the Docker daemon. Testing with `docker run --gpus all nvidia/cuda:12.1.0-base-ubuntu22.04 nvidia-smi`.
- **Storage Topologies:** Bind mounts (host-synced) vs. Named Volumes (Docker-managed). Why we use bind mounts for code (`/workspace`) and named volumes for model weights (`/root/.ollama`).

**Lesson 1.2: DevContainers and Ollama Instantiation**
- **Objective:** Define the developer workspace declaratively using `.devcontainer.json`.
- **Anatomy of `devcontainer.json`:**
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

- **Ollama Docker Compose MVP:**
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

**Lesson 1.3 (Lab 1.0): Baseline Run Card Generation**
- **Task:** Students must clone the base repository, spin up the DevContainer, execute the compose file, and pull `llama3.3` (quantized) via the Ollama CLI.
- **Deliverable:** A markdown Run Card containing the `nvidia-smi` output from inside the container, the exact commit hash, and the HTTP 200 response header from `curl http://localhost:11434/api/tags`.
- **Assessment Gate: DG 0-4 Verification**
  - *DG 0:* Host OS recognized virtualization.
  - *DG 1:* Docker daemon responsive.
  - *DG 2:* `nvidia-container-toolkit` successfully passing GPU VRAM allocation.
  - *DG 3:* Volumes mounted correctly (model weights persist across container destruction).
  - *DG 4:* Port 11434 exposed and accepting localhost traffic.

### Module 2: Inference & Systems Intuition

**Lesson 2.1: The Math of Autoregressive Generation & Context Windows**
- **Objective:** Deconstruct the black box of text generation.
- **Tokenization:** BPE (Byte Pair Encoding). Why "CTHULHU" or "Fànquān" might break a tokenizer if not in the corpus. Token-to-word ratios.
- **KV Cache Mechanics:** How the context window is maintained in GPU VRAM. Calculating memory overhead: `VRAM_req = Model_Weights + KV_Cache + Activation_Memory`.
- **Quantization:** The physics of dropping fp16 precision to INT8 or INT4 (GGUF format) and the impact on perplexity vs. memory footprint.

**Lesson 2.2: Decoding Parameters**
- **Objective:** Manipulating the probability distribution of the next token.
- **Temperature (`T`):** Scaling logits. `T < 1` (sharpening, deterministic), `T > 1` (smoothing, creative).
- **Top-K:** Hard cutoff of the probability tail.
- **Top-P (Nucleus Sampling):** Dynamic cutoff based on cumulative probability mass.
- **Presence/Frequency Penalties:** Forcing vocabulary diversity in long-context extraction.

**Lesson 2.3 (Lab 2.0): Latency and Throughput Benchmarking**
- **Task:** Write a Python script using the `requests` library to ping the local Ollama instance. Construct a grid search iterating over `temperature` [0.1, 0.5, 0.9] and `top_p` [0.5, 0.9].
- **Python Inference Snippet:**
    import requests
    import time

    def benchmark_inference(prompt, temp, top_p):
        start_time = time.time()
        payload = {
            "model": "llama3.3",
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": temp, "top_p": top_p}
        }
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        latency = time.time() - start_time
        tps = response.json().get("eval_count", 0) / latency
        return latency, tps

- **Deliverable:** Jupyter Notebook (`lab_2_0_starter.ipynb` completion) mapping Tokens-Per-Second (TPS) and visual assessment of output determinism across the grid.

---

## Part 4.0: Phase II - RAG & Agents (Modules 3 & 4)

Phase II transitions from raw string generation to constrained, reliable data architectures capable of connecting to external knowledge bases.

### Module 3: Prompt Engineering & Structured Output

**Lesson 3.1: System/User Boundaries and Few-Shot CoT**
- **Objective:** Controlling model persona and forcing logical trace steps.
- **The System Prompt:** Establishing the operational bounds (e.g., "You are an OCR validation engine. Output ONLY requested data.").
- **Chain-of-Thought (CoT):** Forcing the model to emit `<thinking>` tags before `<output>`. Why writing reasoning to the context window improves mathematical and logical outcomes.
- **Few-Shot Prompting:** Injecting high-quality `<example>` blocks into the context to bypass instruction-following failures.

**Lesson 3.2: Grammar-Constrained Decoding**
- **Objective:** Eliminating `JSONDecodeError` permanently.
- **The Problem:** LLMs are statistical engines; they naturally append markdown or conversational filler ("Here is your data:").
- **The Solution:** Pydantic models combined with grammar-constrained endpoints (Instructor library or Ollama `format: json` parameter). 
- **Schema Definition Validation:**
    from pydantic import BaseModel, Field

    class PatientExtraction(BaseModel):
        patient_id: str = Field(description="Alphanumeric ID")
        diagnosis: str
        confidence_score: float = Field(ge=0.0, le=1.0)

**Lesson 3.3 (Lab 3.0): Strictly Typed JSON Extraction**
- **Task:** Pass a highly noisy, unstructured block of clinical text to the local LLM. Force it to extract specific entities matching the Pydantic schema perfectly over 50 iterations without a single parsing failure.
- **Deliverable:** The JSON schemas and a Failure Taxonomy Report documenting how unconstrained models fail versus constrained models.

### Module 4: Agentic Retrieval & Evaluation

**Lesson 4.1: Parametric vs. Non-parametric Memory**
- **Objective:** Understanding Retrieval-Augmented Generation (RAG).
- **Parametric Memory:** Information baked into the model weights during training. Prone to hallucination and static cutoff dates.
- **Non-Parametric Memory:** External databases queried at runtime.
- **Dense Embeddings:** Converting text chunks to high-dimensional vectors using `fastembed` (Jina-v3). Cosine similarity math: dot product normalized by vector magnitudes.
- **Chunking Strategies:** Fixed-size vs. Semantic chunking. The impact of chunk overlap on context loss.

**Lesson 4.2: Persistent Vector Databases (Qdrant)**
- **Objective:** Moving beyond in-memory FAISS arrays to production-grade persistent vector storage.
- **Orchestration:** Adding Qdrant to the Docker Compose topology.
    qdrant:
      image: qdrant/qdrant
      ports:
        - "6333:6333"
      volumes:
        - qdrant_storage:/qdrant/storage

- **Ingestion Pipeline:** Parsing PDFs -> Chunking -> Embedding -> Upserting to Qdrant collection with payload metadata.

**Lesson 4.3 (Lab 4.0): Programmatic RAG Evaluation**
- **Objective:** Stop eyeballing LLM outputs. Use code to grade code.
- **Frameworks:** TruLens / Ragas.
- **The RAG Triad:**
  1. *Context Precision / Relevance:* Did the vector DB return the right chunks for the query?
  2. *Faithfulness (Groundedness):* Is the final answer supported *entirely* by the retrieved chunks, or did the model hallucinate?
  3. *Answer Relevance:* Does the generated answer actually address the user's initial query?
- **Deliverable:** **DG 5 Verification** (Docker Compose orchestrating both the Workspace and Qdrant). Submission of a programmatic RAG Eval Report showing scores >0.85 across the triad for a test dataset.

## Part 5.0: Phase III - Tuning & APIs (Modules 5 & 6)

Phase III moves from utilizing static foundational models to adapting weights for domain-specific scientific tasks and serving those models at scale.

### Module 5: Fine-Tuning on HPC

**Lesson 5.1: PEFT Math and GPU Memory Profiling**
- **Objective:** Master Parameter-Efficient Fine-Tuning without OOM (Out of Memory) errors.
- **The Mechanics:** How Low-Rank Adaptation (LoRA) freezes base weights and injects trainable rank decomposition matrices. 
- **QLoRA:** 4-bit NormalFloat (NF4) quantization and double quantization. 
- **Memory Calculus:** Calculating the VRAM footprint for gradient states and optimizer momentum (AdamW) on 32B and 70B parameter models.

**Lesson 5.2: Declarative Tuning with Axolotl and Unsloth**
- **Objective:** Standardize training runs using declarative YAML configurations.
- **Dataset Preparation:** Formatting instruction-tuning datasets (JSONL) with strict system prompts for extraction tasks.
- **Axolotl Config MVP (`qlora.yml`):**
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

**Lesson 5.3 (Lab 5.0): The Apptainer Bridge & Slurm Orchestration**
- **Objective:** Migrate local Docker workflows to HPC schedulers (Beocat / PSC Bridges-2).
- **Container Conversion:** Building an immutable `.sif` file from a Docker image.
- **Slurm Batch Scripting:**
    #!/bin/bash
    #SBATCH --job-name=axolotl_qlora
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --gres=gpu:a40:4
    #SBATCH --mem=128GB
    #SBATCH --time=24:00:00
    
    apptainer exec --nv --bind /scratch:/workspace kdd_axolotl.sif \
        accelerate launch -m axolotl.cli.train qlora.yml

- **Deliverable:** **DG 6 Verification**. Submission of a Weights & Biases (WandB) or local TensorBoard loss curve confirming convergence on a lab-provided dataset.

### Module 6: Serving & Governance

**Lesson 6.1: vLLM Server Deployment**
- **Objective:** Transition from Ollama to a high-throughput, production-grade serving engine.
- **PagedAttention Mechanics:** How vLLM manages the KV cache like an OS virtual memory page table to eliminate fragmentation and handle continuous batching.
- **Deployment:** Spinning up the vLLM OpenAI-compatible server on the KDD Lab GPU cluster, mapping the newly trained LoRA adapters dynamically.

**Lesson 6.2: High-Throughput Endpoints Under Load**
- **Objective:** Load testing and concurrent thread management.
- **Concurrency:** Using Python `asyncio` and `aiohttp` to hammer the vLLM endpoint and measure degradation in TPS vs. total batch throughput.

**Lesson 6.3 (Lab 6.0): AI Risk Management Framework**
- **Objective:** Map the technical infrastructure to compliance and safety standards.
- **NIST AI RMF 1.0 Application:** Framing risks associated with automated data extraction.
- **Deliverable:** **DG 7 Verification** (vLLM Server Orchestration active). Submission of an AI Risk Register v1, mapping Map, Measure, and Manage functions to the pipeline.

---

## Part 6.0: Phase IV - Capstone (Modules 7 & 8)

Phase IV brings all concepts together into a fully autonomous, multi-agent pipeline designed for rigorous scientific document understanding.

### Module 7: Orchestration

**Lesson 7.1: ReAct Prompting and Multi-Agent Workflows**
- **Objective:** Moving from static execution to dynamic tool use.
- **ReAct (Reasoning and Acting):** Forcing the model to loop through Thought -> Action -> Observation cycles.
- **Tool Binding:** Giving the LLM access to Python REPLs, search functions, and the Qdrant vector database.

**Lesson 7.2: LangGraph Orchestration**
- **Objective:** Building cyclical, stateful agent graphs.
- **State Management:** Defining the `TypedDict` that passes between nodes.
- **Nodes & Edges:** Routing logic based on intermediate model outputs (e.g., if parsing fails, route to a fallback OCR node).

**Lesson 7.3 (Lab 7.0): Tool-Use Evaluation and Tracing Guardrails**
- **Objective:** Instrumenting the graph to track execution paths and latency.
- **Deliverable:** **DG 8 Verification** (LangGraph Node Execution). Submission of a graph trace showing a successful multi-step retrieval and extraction task.

### Module 8: Biomedical Extraction Capstone (The Personalization Exemplar)

This module represents the culmination of the course, focusing on a modern Open Information Extraction (Open IE) pipeline.

**Lesson 8.1: Unstructured Parsing & Multimodal Ingestion**
- **Objective:** Taming noisy, heterogeneous source data.
- **Ingestion Tools:** OCR (Tesseract), PDF parsing (Camelot), and transcript extraction.
- **Tokenizer Stress Testing:** Handling non-standard vocabularies, severe noise, and highly specific subculture linguistics. Testing the pipeline's robustness when encountering out-of-distribution tokens—ranging from internet fandom terminology (e.g., *Fànquān*) to anomalous/eldritch string insertions (e.g., *CTHULHU*, *shoggoths*).

**Lesson 8.2: Ontology Grounding & Scientific Reasoning**
- **Objective:** Ensuring extracted data maps to scientifically meaningful structures.
- **The Substrate:** Using foundation models to align raw text against strict medical/chemical ontologies.
- **Validation:** Designing validation nodes that reject hallucinated entities or unsupported claims.

**Lesson 8.3 (Lab 8.0): The 7-Stage Extraction Pipeline**
- **Objective:** Deploying the full architecture against real-world data.
- **The Target:** Monitoring social media platforms (TikTok, YouTube, and Reddit) for drug misuse and abuse indicators.
- **Pipeline Execution:** 1. Ingest Video/Audio/Text.
  2. Parse (Whisper/OCR).
  3. Chunk & Embed.
  4. Retrieve (Qdrant).
  5. Extract (Strict JSON using Llama 3.3).
  6. Ground (Ontology alignment).
  7. Validate (Conflict detection).
- **Deliverables:** - Final Python Runbook committed to GitHub.
  - Evaluation Report (detailing Conflict Detection mechanisms and F1 extraction scores).
  - Finalized AI RMF Risk Register addressing the specific hazards of processing user-generated health data.
  
---

## Part 7.0: The 5x4 Term Project Matrix

While Module 8 provides the Biomedical Exemplar, students must execute their Capstone across one of the intersections in the 5x4 Project Matrix, tailored to their specific GRA funding or thesis requirements. 

### 7.1 Methodology Pillars (The 5)
- **[NL] Natural Language:** Advanced extraction, summarization, and reasoning.
- **[CV] Computer Vision:** Multimodal OCR, chart parsing, and vision-language mapping.
- **[RL] Reinforcement Learning:** DPO/PPO alignment and reward modeling for specialized outputs.
- **[ST] Spatiotemporal:** Time-series forecasting and geographic entity grounding.
- **[OA] Optimization & Agents:** Multi-agent routing, cost/latency optimization, and tool-use.

### 7.2 Category Tracks (The 4)
- **Track A: Clinical & Biomedical:** (e.g., extracting multiple myeloma survival rates from unstructured clinical PDFs; parsing social media for drug misuse).
- **Track B: Cyber-Physical & Security:** (e.g., parsing SCADA system logs and threat intelligence reports using agentic workflows).
- **Track C: Social & Subculture Discourse:** (e.g., entity tracking in highly specialized linguistic environments, such as correctly identifying and clustering *Fànquān* community structures and sentiment across heterogeneous text).
- **Track D: Fundamental Infrastructure:** (e.g., optimizing LoRA rank settings for minimum VRAM overhead while preserving recall on highly anomalous tokens).

### 7.3 Project Selection Matrix
Students must declare their `[Pillar] x [Track]` coordinate by Week 3 (e.g., `[NL] x [Track A]` maps directly to the baseline exemplar). The final runbook and schema design must strictly adhere to the declared coordinate.

---

## Part 8.0: Grading Rubrics & Docker Gate (DG) Verification

This course utilizes binary dependency gates. Partial credit is not awarded for broken infrastructure.

### 8.1 The Docker Gates (DG 0 - 8)
- **DG 0: Virtualization Ready:** WSL2/Linux kernel configured; Hyper-V active.
- **DG 1: Daemon Alive:** Docker Engine running and responsive.
- **DG 2: VRAM Passthrough:** `nvidia-smi` successfully executes *inside* the container, recognizing all allocated GPUs.
- **DG 3: Persistent Storage:** Named volumes successfully preserve weights across a `docker compose down && docker compose up` cycle.
- **DG 4: Endpoint Exposure:** Localhost port (e.g., 11434 for Ollama) accepts external `curl` requests.
- **DG 5: Multi-Node Orchestration:** `docker-compose.yml` successfully networks the Python workspace container with the Qdrant vector database container.
- **DG 6: HPC Migration:** Docker container successfully converted to Apptainer `.sif` and deployed via Slurm batch script on Beocat or PSC Bridges-2.
- **DG 7: vLLM Server Orchestration:** vLLM container successfully maps LoRA adapters and serves the OpenAI-compatible API endpoint.
- **DG 8: LangGraph Execution:** A multi-node agent graph compiles and completes a full execution trace without routing errors.

### 8.2 Final Capstone Grading Rubric
The final repository submission is evaluated against three strict criteria:
1. **Reproducibility (40%):** Does the GitHub repository contain the exact `docker-compose.yml`, `requirements.txt`, and Run Card necessary for the instructor to clone and run the pipeline without modifying code?
2. **Schema Rigor (30%):** Does the pipeline enforce strict Pydantic parsing? Are outputs cleanly mapped to standard ontology formats without markdown pollution or `JSONDecodeError`s?
3. **Evaluation Completeness (30%):** Does the submission include programmatic evaluation metrics (TruLens/Ragas scores, F1 extraction metrics) and an AI RMF Risk Register addressing the specific hazards of their dataset?