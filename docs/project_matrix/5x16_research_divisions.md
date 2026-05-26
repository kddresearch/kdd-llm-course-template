# The 5x16 Capstone Project Matrix
**Status:** Canonical

To graduate from this course, your Module 8 Capstone pipeline must map to one intersection of the 5 Lab Divisions (The Pillars) and the 16 Core Research Ideas. 

## The 5 Methodology Pillars (Lab Divisions)
1. **[NL] Natural Language:** Language modeling, extraction, summarization, and text reasoning.
2. **[CV] Computer Vision:** Spatial OCR, scene graphs, vision-language explanations.
3. **[RL] Reinforcement Learning:** Reward modeling, alignment, causal/probabilistic inference.
4. **[ST] Secure & Trustworthy ML:** Epistemic grounding, factuality, AI safety guardrails, uncertainty estimation.
5. **[OA] Other Applied AI:** Topic modeling, affect/sentiment analysis, automated meta-research.

## The 16 Core Research Ideas (The "Where")
*Students must select a research domain corresponding to their GRA funding or thesis topic. Stable IDs must be used for all cross-project citations and GitHub tagging.*

1. **KDD-01: Efficient Foundation Models for Sustainable ML:** Quantization, pruning, distillation, and cramming across pretraining/finetuning. (Tags: NL, CV, RL, ST)
2. **KDD-02: Information Trust and World-Model Grounding:** Evaluating trust, reliability, and epistemic grounding of extracted information. (Tags: NL, ST)
3. **KDD-03: Mostly-Unsupervised Few-Shot Temporal Topic Modeling:** Dynamic topic modeling with minimal supervision and explicit topic drift. (Tags: NL, OA)
4. **KDD-04: End-to-End Meta-Research Pipelines from Literature:** Automating extraction, deduplication, and aggregation from scientific document collections. (Tags: NL, ST, OA)
5. **KDD-05: Trust-Weighted Inference and Evidence Aggregation:** Weighting sources and posterior estimates by trust, uncertainty, and evidentiary support. (Tags: NL, ST)
6. **KDD-06: Part–Whole Hierarchies for Qualitative and Mixed Reasoning:** Using mereotopological representations to support hybrid reasoning over structured knowledge. (Tags: NL, CV, ST)
7. **KDD-07: Hierarchy-Aware Vision–Language Explanation:** Vision systems exploiting part-whole hierarchies for reliable captions and diagrams. (Tags: CV, NL)
8. **KDD-08: Multimodal Ontology Learning Systems:** Jointly learning ontologies from text and vision; structure induction and representation learning. (Tags: NL, CV, ST)
9. **KDD-09: End-to-End Trusted Multimodal Learning Systems:** Integrating trust, attribution, and knowledge graphs into active perception and never-ending learning. (Tags: NL, CV, RL, ST)
10. **KDD-10: Value Alignment Guardrails vs. IE Completeness:** Analyzing safety guardrails and their unintended impacts on information extraction fidelity. (Tags: ST)
11. **KDD-11: Sentic and Affective Downstream Modeling:** Sentiment, tone control, reading level adaptation, and emotionally-aware generation. (Tags: NL, OA)
12. **KDD-12: Neurosymbolic and Ontology-Aware Reasoning:** Combining neural models with symbolic logic for argumentation, disambiguation, and role attribution. (Tags: NL, ST)
13. **KDD-13: Causal and Counterfactual Probabilistic Reasoning:** Causal inference via Bayesian/decision networks informed by extracted priors. (Tags: RL, ST)
14. **KDD-14: Multimodality as a Unifying Constraint:** How multimodal signals jointly inform grounding, trust estimation, and reasoning. (Tags: NL, CV, RL, ST, OA)
15. **KDD-15: Rich Representations for Reward, Value, and Policy Learning:** Capturing roles, context shifts, and nonstationarity in interaction/dialogue. (Tags: RL, ST)
16. **KDD-16: Multiresolution Gradients for Saliency and Explanation:** Hierarchies of gradients and multiscale attribution to improve interpretability. (Tags: NL, CV, ST)

## Matrix Declaration
You must declare your `[Pillar] x [Stable ID]` coordinate (e.g., `[NL] x KDD-04`) by Module 3. Note that your chosen Stable ID must be natively compatible with your chosen Pillar according to the tags listed above. Your final Pydantic schemas and Vector DB structure must strictly adhere to this declared domain.