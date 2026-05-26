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

## ⚠️ The GitOps Mandate

This course operates on a strict dependency-driven pipeline. **We do not host code on Canvas.** 1. You must fork/clone this repository.
2. You must execute all assignments within the provided `.devcontainer`.
3. You must submit your completed work by providing the exact GitHub commit URL to Canvas. 

Canvas is strictly used for policy announcements and grade routing. Your code lives here.

## 🚀 Quick Start: The Execution Pipeline

To begin Unit 1, you must provision your local environment by following these steps:

1. **Fork the Substrate:** Click the `Fork` button at the top right of this page to create your own copy of this repository under your personal GitHub account.
2. **Clone Your Fork:** ```bash
   git clone [https://github.com/YOUR-USERNAME/kdd-llm-course-template.git](https://github.com/YOUR-USERNAME/kdd-llm-course-template.git)