# AI Workflow Note

AI assistants were used as an engineering accelerator, not as a substitute for product judgment.

## Where AI materially helped

- Generated initial FastAPI and React scaffolding.
- Accelerated repetitive CRUD, schema and API boilerplate.
- Helped identify validation and authorization edge cases.
- Drafted documentation structure and test scenarios.
- Helped troubleshoot dependency and deployment configuration issues.

## What I changed or rejected

The implementation was intentionally simplified after reviewing generated suggestions. In particular, document sharing is modeled as a separate `document_shares` relationship rather than putting a single shared-user field on the document. This supports multiple recipients and keeps authorization explicit.

I also rejected over-engineering around real-time collaboration and complex roles because those features would have consumed the assignment timebox without improving the required end-to-end workflow.

## Verification

Correctness was verified by reviewing API authorization paths, running automated tests, exercising login/create/edit/import/share flows manually, refreshing the browser to verify persistence, and checking invalid file and unauthorized access behavior.

## Human judgment

I selected the product scope, data model, access rules, supported file types, deployment strategy and tradeoffs. AI output was treated as a draft that needed review, not as an authoritative implementation.
