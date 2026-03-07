---
description: Launch a product.
---

> **Compatibility Directive**: This component is optimized primarily for the Google Antigravity runtime, but gracefully degrades to support Gemini CLI, Claude Code, and Kilocode CLI.



# /launch - Go-to-Market Strategy

**Trigger**: User types `/launch` or asks for a GTM plan.

## Steps

1. **Parallel Context Analysis**:
   - **Action**: In a SINGLE turn, read `2. Products/` AND `grep_search` `3. Meetings/transcripts/` for "launch", "release", or "GTM".
   - **Goal**: Understand _what_ is launching and if dates were discussed.

2. **Define Audience & Channels**:
   - Who is this for? (Target Persona).
3. **Draft Plan**: Create a T-Minus schedule (Internal Comms, Beta, GA).
4. **Draft Assets**: Generate Value Prop, Blog Post, and Tweet thread.
