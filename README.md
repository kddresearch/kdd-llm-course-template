<div align="center">
  
# 🟣 Applied LLM Engineering
**K-State Knowledge Discovery in Databases (KDD) Lab**

[![Zone](https://img.shields.io/badge/Compute_Zone-1_(Local_Prototyping)-0056b3?style=for-the-badge)](https://k-state.instructure.com)
[![Status](https://img.shields.io/badge/Course_Status-Active-2e7d32?style=for-the-badge)](https://github.com/kddresearch/kdd-llm-course-template)
[![Protocol](https://img.shields.io/badge/Protocol-KEEP_FLYING-d64309?style=for-the-badge)](https://github.com/kddresearch/kdd-llm-course-template/issues)

*The execution substrate for CIS 530 / 730 Term Project Pathways.*

</div>

---

## 🎯 System Overview

This repository is the authoritative **Zone 1 Execution Substrate** for the Applied LLM Engineering short course. It contains the Docker DevContainer configurations, Python dependencies, and baseline Jupyter notebooks required to deploy and evaluate open-weight Large Language Models strictly on local hardware.

If you are a student in the course, your objective is to use this repository to establish a reproducible local environment, execute the sequential Lab requirements, and pass the resulting commit hashes through the artifact gates on Canvas.

## 🚀 Quick Start: The Execution Pipeline

To begin Unit 1, you must provision your local environment by following these steps:

1. **Fork the Substrate:** Click the `Fork` button at the top right of this page to create your own copy of this repository under your personal GitHub account.
2. **Clone Your Fork:** ```bash
   git clone [https://github.com/YOUR-USERNAME/kdd-llm-course-template.git](https://github.com/YOUR-USERNAME/kdd-llm-course-template.git)
   ```
3. **Open the Workspace:** Open the cloned directory in Visual Studio Code.
4. **Trigger the Build:** * Press `F1` (or `Ctrl+Shift+P` / `Cmd+Shift+P`).
   * Type and select: `Dev Containers: Rebuild and Reopen in Container`.
   * *Note: This will download the heavy PyTorch/Ollama base image. It may take 5–15 minutes depending on your bandwidth.*
5. **Clear the Gate:** Navigate to `labs/lab_1_0_baseline.ipynb` and execute the run card to verify your environment is stable.

## 📂 Repository Architecture

```text
kdd-llm-course-template/
├── .devcontainer/
│   ├── devcontainer.json    # VS Code environment and port mapping
│   └── Dockerfile           # System-level dependencies and LLM engine
├── labs/
│   ├── lab_1_0_baseline.ipynb   # DG 0-4 Environment Verification
│   └── lab_2_0_starter.ipynb    # Inference & Attention implementation
├── requirements.txt         # Python package dependencies (Pandas, Jupyter, etc.)
└── README.md
```

## 🛑 KEEP FLYING: Operations Policy

This course operates on an **Asynchronous, Dependency-Driven Pipeline**. You are the execution engine. If you encounter a hard blocker (e.g., Docker OOM Exit Code 137, library conflicts), you must adhere to the KEEP FLYING protocol:

> **dt = 24 Hours:** You must not remain blocked on a technical issue for more than 24 calendar hours without escalating.

1. **Check the Runbooks:** Consult the specific Canvas Runbook or Troubleshooting Guide for your current module.
2. **Execute Bounded Attempts:** Try to resolve the issue yourself up to 3 times. Document what you tried.
3. **File an ABR:** If the issue persists, go to the [Issues tab](../../issues) of the main repository and submit an **Access Blocker Report (ABR)**. 

*Do not use Canvas messaging for technical environment debugging. All execution issues must be tracked via GitHub.*