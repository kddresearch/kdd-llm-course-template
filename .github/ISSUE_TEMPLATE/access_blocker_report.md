# GitHub Operations Templates
**Status:** Canonical

The Gem must instruct students to use these exact structures when filing issues in their repository. These map to the files located in `.github/ISSUE_TEMPLATE/`.

## 1. Access Blocker Report (ABR)
**File:** `access_blocker_report.md`
**Trigger:** `dt = 24h` limit reached on a technical/infrastructure blocker.

**Title Format:** `[ABR] Module X: Brief description of blocker`

**Body:**
### 1. Execution Zone
[ ] Zone 1 (Local DevContainer / Ollama)
[ ] Zone 2 (Lab A40 Cluster / vLLM)
[ ] Zone 3 (Beocat / PSC / Slurm)

### 2. The Blocker
*State the exact problem in 1-2 sentences.*

### 3. Bounded Attempts
*List the 3 specific, distinct interventions you attempted to resolve this before filing.*
1. 
2. 
3. 

### 4. Exact Error Output
*Paste the exact terminal stack trace, logs, or Exit Code below. NO SCREENSHOTS OF TEXT.*
```text
[Paste logs here]