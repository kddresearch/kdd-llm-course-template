# KEEP FLYING: Operations & Communications Policy

## 1. The Core Directive
Hardware fails. Dependencies break. CUDA runs out of memory. This is the reality of applied LLM engineering. The primary operational directive of the KDD Lab is **Keep Flying**. If you hit a hard technical blocker, you do not stall. You document the blocker, pivot immediately to an offline conceptual task (schema design, literature review, data curation), and keep moving forward.

## 2. The dt = 24h Escalation Rule
- **Maximum Blocked Time:** You are strictly forbidden from remaining blocked on a single technical issue (e.g., container build failures, environment pathing) for more than 24 calendar hours (`dt = 24h`).
- **Anti-Thrashing Protocol:** Endlessly regenerating Docker builds or tweaking Python virtual environments without understanding the underlying error is "thrashing."
- **Action at Limit:** Once `dt = 24h` is reached, you must stop thrashing, commit your current (broken) state to GitHub, and formally file an Access Blocker Report (ABR).

## 3. The Access Blocker Report (ABR)
When the 24-hour limit is reached, file an Issue on your GitHub repository using the ABR template, then notify the instructor.

**Required ABR Fields:**
1. **Zone:** [1 (Local DevContainer) / 2 (Lab GPU/vLLM) / 3 (HPC/Beocat/PSC)]
2. **Blocker:** [A concise, 1-sentence description of what is stopping execution]
3. **Bounded Attempts:** [List the 3 specific, distinct interventions you attempted to resolve it]
4. **Exact Error:** [Paste the exact terminal output, stack trace, or log snippet. NO SCREENSHOTS OF TEXT.]

## 4. Communication Tiers (Class A vs. Class B)

### Class A: Asynchronous (Default)
- **Use Case:** Code reviews, ABR submissions, architectural questions, and standard grading gates.
- **Protocol:** Pushed via GitHub Issues or email. The instructor will respond asynchronously. You must continue executing your offline "Pivot" tasks while awaiting resolution.

### Class B: Interactive (Live Troubleshooting)
- **Use Case:** Complete local environment corruption, unrecoverable Git state conflicts, or Slurm node allocation lockouts.
- **Protocol:** Requires the **2-Window Handshake**. The student must have their terminal/code open in one screen/window, and the communication channel open in the other, ready to execute live commands.
- **The "READY" ACK:** When the instructor signals availability for a Class B live session, the student has exactly 2 minutes to respond with the `[ACK-READY]` macro. If missed, the ticket reverts immediately to Class A status.

## 5. The 4 Communication Macros
To maintain high signal-to-noise in course communications, use these exact subject line prefixes in your emails or direct messages to the instructor:

1. **`[ABR-FILED]`**: Use when notifying the instructor that a formal Access Blocker Report has been committed to your repo's Issue tracker.
2. **`[SYNC-REQ]`**: Use to request a Class B Interactive session *only after* an ABR has failed to resolve the issue asynchronously.
3. **`[ACK-READY]`**: The mandatory response within 2 minutes of the instructor confirming a Class B session time slot.
4. **`[GATE-CLEARED]`**: Use to notify the instructor that a specific Docker Gate (DG 0-8) run card has been pushed to GitHub and is ready for verification.