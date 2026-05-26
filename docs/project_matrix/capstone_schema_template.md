# Capstone Coordinate & Schema Declaration
**Status:** Template
**Path:** `docs/project_matrix/capstone_schema_template.md`

**Student:** [Your Full Name]
**Declared Coordinate:** [[Pillar]] x [[Stable ID]] 
## 1. The Target Dataset
* **Source:** [Describe the quantity, format, and origin of your data. E.g., 500 JSON scrapes from a specific subreddit, or 2,000 SCADA log text files.]
* **Noise Profile:** [What makes this extraction difficult? List specific anomalies your pipeline must overcome. E.g., OCR artifacts, specialized/out-of-distribution slang, conflicting acronyms, or missing table headers.]

## 2. The Pydantic Extraction Schema
```python
from pydantic import BaseModel, Field
from typing import List, Optional

# Add nested models as needed for your specific task
class [NestedEntityName](BaseModel):
    [variable_1]: [type] = Field(description="[Explicit definition and constraints for this variable]")
    [variable_2]: Optional[float] = Field(None, description="[Include examples of acceptable output if ambiguous]")

class [MainExtractionSchema](BaseModel):
    document_id: str = Field(description="Unique identifier for the source document/chunk")
    [target_entity_list]: List[[NestedEntityName]]
    extraction_confidence: float = Field(ge=0.0, le=1.0, description="Agent's internal confidence score for the extracted metrics")
    
    # [Add additional top-level fields required by your research domain]