# Capstone Coordinate & Schema Declaration
**Status:** Canonical Exemplar
**Path:** `docs/project_matrix/capstone_schema_template.md`

**Student:** @mobimaMA (example - biomedical meta-research)
**Declared Coordinate:** [NL] x [KDD-04] (Natural Language x End-to-End Meta-Research Pipelines)

## 1. The Target Dataset
* **Source:** 5,000 unstructured clinical oncology PDFs, case reports, and PubMed abstracts detailing Multiple Myeloma survival rates, treatment regimens (e.g., VRd, Dara-RVd), and patient demographics.
* **Noise Profile:** Highly heterogeneous table structures across different clinical trial publishers, conflicting acronyms (e.g., "MM" representing Multiple Myeloma vs. Millimeter), and severe OCR artifacts from scanned legacy medical records.

## 2. The Pydantic Extraction Schema
Define the exact Python data structure your agent will be forced to output. The grammar-constrained endpoint will enforce this structure strictly.

```python
from pydantic import BaseModel, Field
from typing import List, Optional

class TreatmentRegimen(BaseModel):
    drug_combination: str = Field(description="Standardized acronym for the chemotherapy/immunotherapy combo (e.g., 'VRd', 'Dara-RVd')")
    duration_months: Optional[float] = Field(None, description="Duration of the treatment phase in months")

class SurvivalMetrics(BaseModel):
    median_pfs_months: Optional[float] = Field(None, description="Median Progression-Free Survival (PFS) in months")
    median_os_months: Optional[float] = Field(None, description="Median Overall Survival (OS) in months")

class MultipleMyelomaExtraction(BaseModel):
    document_id: str = Field(description="Unique identifier for the source PDF or PubMed ID")
    patient_cohort_size: int = Field(description="Total number of patients evaluated in the study or cohort")
    disease_stage: str = Field(description="ISS or R-ISS staging if specified (e.g., 'Stage II', 'R-ISS III')")
    treatments: List[TreatmentRegimen]
    outcomes: SurvivalMetrics
    extraction_confidence: float = Field(ge=0.0, le=1.0, description="Agent's internal confidence score for the extracted metrics")