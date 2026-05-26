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