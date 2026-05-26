<div align="center">
  
# 🟣 Applied LLM Engineering
**K-State Knowledge Discovery in Databases (KDD) Lab**

[![Zone](https://img.shields.io/badge/Compute_Zone-1_(Local_Prototyping)-0056b3?style=for-the-badge)](https://k-state.instructure.com/courses/32258/pages/llm-short-course)
[![Status](https://img.shields.io/badge/Course_Status-Active-2e7d32?style=for-the-badge)](https://github.com/kddresearch/kdd-llm-course-template)
[![Protocol](https://img.shields.io/badge/Protocol-KEEP_FLYING-d64309?style=for-the-badge)](https://github.com/kddresearch/kdd-llm-course-template/issues)

*The execution substrate for foundation model-based projects of the K-State KDD Lab - research, independent study, and course term projects.*

</div>

---

## 🎯 System Overview

Welcome! This repository is your foundational workspace (Zone 1) for Applied LLM Engineering. It contains the Docker DevContainer configurations, Python dependencies, and baseline Jupyter notebooks you will need to deploy and evaluate open-weight Large Language Models strictly on local hardware.

Your objective is to use this repository to establish a reproducible local environment, work through the Lab requirements, and pass the resulting commit hashes through the artifact gates on Canvas. 

## ⚠️ The GitOps Mandate

To keep our workflows industry-standard, **we do not host code on Canvas.**

1. **Fork & Clone:** You will fork this repository and do all your work in your own copy.
2. **Containerize:** You will execute all assignments within the provided `.devcontainer`.
3. **Commit & Submit:** You will submit your completed work by providing the exact GitHub commit URL to Canvas. 

Canvas is used for policy announcements and grading. Your actual code and engineering work lives here.

## 🚀 Quick Start: The Execution Pipeline

Let's get your local environment running for Unit 1:

1. **Fork the Substrate:** Click the `Fork` button at the top right of this page to create your own copy of this repository under your personal GitHub account.
2. **Clone Your Fork:** ```bash
   git clone [https://github.com/YOUR-USERNAME/kdd-llm-course-template.git](https://github.com/YOUR-USERNAME/kdd-llm-course-template.git)

## 🛑 KEEP FLYING: Operations Policy

In applied LLM engineering, hardware fails and CUDA crashes. That is a normal part of the process! If you encounter a hard blocker (like a Docker OOM Exit Code 137 or a library conflict), please follow the KEEP FLYING protocol:

**dt = 24 Hours:** Please do not remain stuck on a technical issue for more than 24 calendar hours without escalating it.

1. **Check the Runbooks:** Consult the specific Canvas Runbook or Troubleshooting Guide for your current module.
2. **Execute Bounded Attempts:** Try to resolve the issue yourself up to 3 times, and take note of what you tried.
3. **Pause & Commit:** Stop troubleshooting, and commit your current (even if broken) state to GitHub.
4. **File an ABR:** Go to the Issues tab of your repository and submit an **Access Blocker Report (ABR)** using the provided template so we can help you fix it.
5. **Pivot:** Immediately pivot to offline conceptual work (like designing your schemas or reading literature). Keep your momentum going!

*Note: Do not use Canvas messaging for technical environment debugging. All execution issues must be tracked via GitHub.*