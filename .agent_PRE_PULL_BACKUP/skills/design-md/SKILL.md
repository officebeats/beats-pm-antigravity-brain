---
name: design-md
description: Analyzes Stitch projects and generates comprehensive DESIGN.md files documenting design systems.
triggers:
  - "/design"
  - "/document-design"
version: 1.0.0 (Stitch Import)
author: Google Labs (Imported to Beats PM Brain)
---

# Stitch DESIGN.md Skill

> **Role**: Design Archaeologist. Extract design tokens -> Synthesize into natural language.

## 1. Native Interface

- **Inputs**: Component code, UI screenshots, CSS files, Tailwind configs.
- **Tools**: `view_file`, `visual_processor` (if images provided), `grep_search`.

## 2. Cognitive Protocol

1.  **Extract Project Identity**: Read `package.json` or project root to find the product name.
2.  **Define the Atmosphere**: Analyze CSS/Markdown to describe the mood (e.g., "minimalist", "vibrant", "dense").
3.  **Map the Color Palette**: Find hex codes in configs/CSS. Assign functional roles (Primary, Secondary, Error).
4.  **Translate Geometry**: Identify border-radius, spacing, and elevation (shadows).
5.  **Output Guidelines**:
    - Use descriptive design terminology (e.g., "Ocean-deep Cerulean" vs "blue").
    - Explain the "why" behind decisions.
    - Follow the `DESIGN.md` structure exactly.

## 3. Output Format (DESIGN.md)

```markdown
# Design System: [Project Title]

## 1. Visual Theme & Atmosphere

(Description of the mood, density, and aesthetic philosophy.)

## 2. Color Palette & Roles

(List colors by Descriptive Name + Hex Code + Functional Role.)

## 3. Typography Rules

(Font families, weights, and hierarchy.)

## 4. Component Stylings

- **Buttons**: (Shape, color, hover state).
- **Cards**: (Rounding, shadow, background).
- **Inputs**: (Stroke, focus state).

## 5. Layout Principles

(Whitespace strategy, margins, grid alignment.)
```
