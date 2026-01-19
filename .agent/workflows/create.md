---
description: Draft PRDs, Specs, and One-Pagers from context (Transcripts/Tasks).
---

# ✍️ Creation Playbook

This workflow guides the **Staff PM** to turn chaos (notes/transcripts) into order (files).

## Steps

1.  **Intent Classification**:
    - **PRD/Spec**: "Write a spec for feature X".
    - **One-Pager**: "Brief for the leadership team".
    - **Bug Report**: "Formalize this issue".

2.  **Context Mining (Crucial)**:
    - **Query**: "What existing files or transcripts should I reference?"
    - **Action**: Search `3. Meetings/transcripts/` for keywords related to the topic.
    - **Synthesis**: Summarize relevant points from the transcripts _before_ writing.

3.  **Template Application**:
    - Select the matching template from `.agent/templates/`.
    - using `prd-author` or `requirements-translator`.

4.  **Drafting**:
    - Write the file to `2. Products/[Product]/features/`.

5.  **Task Connection**:
    - Ask: "Should I add a task to track this doc's completion?"
    - If yes -> Trigger `/track`.
