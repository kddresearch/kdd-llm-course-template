# PSC Bridges-2 Runbook: Extreme Scale Compute
**Status:** Placeholder / Draft
**Target:** Pittsburgh Supercomputing Center (Bridges-2 GPU Nodes)

## 1. Environment Activation
Unlike Beocat, PSC utilizes a strict module system. You must load the Apptainer and CUDA modules before execution.
* [TODO: Insert `module load apptainer/1.x`]
* [TODO: Insert `module load cuda/12.x`]

## 2. Neocortex / V100 / A100 Routing
Depending on your XSEDE/ACCESS allocation, you must route your job to the correct partition.
* [TODO: Insert partition routing logic for `sbatch -p GPU-shared`]

## 3. The Execution Script
* [TODO: Insert PSC-specific `sbatch` script for distributed data parallel (DDP) training across multiple nodes]