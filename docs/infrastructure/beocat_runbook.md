# Beocat HPC Runbook: Apptainer & Slurm Integration
**Status:** Placeholder / Draft
**Target:** K-State Beocat GPU Nodes (A100/L40S)

## 1. Container Conversion
Docker daemons are disabled on Beocat for security. You must convert your Zone 1 Docker image to an immutable Apptainer `.sif` file.
* [TODO: Insert `apptainer build` command migrating from Docker Hub/GHCR]

## 2. Slurm Workload Manager (`sbatch`)
To execute Axolotl fine-tuning on Beocat, use the following baseline Slurm script. Adjust memory and time limits based on your model's parameter count.

* [TODO: Insert verified Beocat `sbatch` header]
* [TODO: Insert node allocation constraints (e.g., `--gres=gpu:1`)]
* [TODO: Insert `apptainer exec --nv` command mapped to `/scratch`]

## 3. Storage Quotas & Weights & Biases
* **Warning:** Do not write checkpoints to your `/home` directory. All model outputs must stream to `/scratch` or `/bulk`.
* **Telemetry:** Ensure your `WANDB_API_KEY` is exported in the Slurm script prior to the Apptainer execution.