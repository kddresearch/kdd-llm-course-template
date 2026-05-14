> [!CAUTION]
> Replace all the placeholders with the correct information.
> Remove this message only after you have replaced all the placeholders.
> * means optional

# KDD - [Team] - [Project]

This is a ML research project for the KDD Research Team. The machine learning
model and API was built using Python.

[View More - KDDResearch.org](https://kddresearch.org/)

## Installation

Install the proper tools:
- Docker

Next, fill out all the required secrets:

### /.env.local
```env
# Secrets
```

## Usage

### Run With Docker (Preferred)

> [!NOTE]
> Provide the required secrets in the `.env.local` file before running the project.

```bash
docker run ghcr.io/kddresearch/project-template:latest -env-file .env.local
```

or

```bash
docker build -t project-template .

docker run -p 3000:3000 project-template -env-file .env.local
```

View the console to see the result.

## Contributing

To contribute to this project, follow the instructions in `CONTRIBUTING.md`

## Citation

To cite this project, use `CITATION.cff`

## Confidentiality: Internal

> Access: KDD Members

This repository should remain private and only accessible to KDD members. This
repository contains sensitive information about KDD Research workflows and
defaults. Do not share this repository with anyone outside of the KDD Research.
