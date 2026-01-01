# 📂 Product Contexts (Director Mode)

> This folder is the "Brain" of the "Brain". It defines your product portfolio.

## How It Works

1.  **Create a file** for each product (e.g., `mobile-app.md`, `data-platform.md`).
2.  **Use the Template**: Copy from `TEMPLATES/product-context.md`.
3.  **Define Keywords**: When Antigravity sees "checkout", "API", or "dashboard", it checks these files to know which product you're talking about.

## Example Structure

```
PRODUCTS/
├── mobile-app.md       (Keywords: checkout, ios, android, login)
├── data-platform.md    (Keywords: api, pipeline, aws, ingestion)
├── internal-tools.md   (Keywords: cli, support portal, scripts)
└── README.md           (This file)
```

## Why This Matters

- **Zero-Context Routing**: You paste a screenshot of an error. Antigravity sees "502 Bad Gateway" + "API". It checks `data-platform.md`, sees "API" is a keyword, and logs the bug to the Data Platform.
- **Multi-Product Meetings**: You paste a transcript covering 3 different products. The `Meeting Synthesizer` splits the action items by product automatically.

---

**Tip**: The more specific your keywords in these files, the smarter the routing becomes.
