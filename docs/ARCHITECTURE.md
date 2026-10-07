# Architecture Note

## Product slice

Ajaia Docs focuses on a reliable single-document lifecycle: authenticate, create/import, edit, persist, reopen and share. The assignment is timeboxed, so real-time collaboration and complex enterprise permissions were intentionally excluded.

## Frontend

React + TypeScript + Vite provides a small browser client. Authentication state is held in `AuthContext`; API calls are centralized in `services/api.ts`. The editor stores formatted HTML because HTML maps directly to the required browser formatting controls and can be persisted/reloaded without building a custom document model.

## Backend

FastAPI exposes REST endpoints. SQLAlchemy provides a database abstraction. JWT tokens identify the current user. Business authorization is separated into `services/documents.py`, while database access is kept in repository/model layers.

## Data model

`users` stores demo identities. `documents` stores title, HTML content and owner. `document_shares` is a join table with a permission field. The join table keeps ownership separate from sharing and leaves room for additional permission types later.

## Persistence

SQLite is the zero-setup local default. When `DATABASE_URL` points to PostgreSQL, the same SQLAlchemy models work against PostgreSQL for deployment.

## Authorization

Every document read checks whether the current user is the owner or has a share record. Edits require owner or editor access. Only owners can create shares or delete a document.

## File import

The core scope supports TXT and Markdown files up to 2 MB. Content is decoded as UTF-8 and safely escaped into paragraph HTML. Markdown is deliberately treated as text instead of attempting a full Markdown parser, reducing dependency and security surface while keeping the import workflow reliable.

## Tradeoffs

- HTML editor instead of a heavy collaborative editor framework: faster and sufficient for required formatting.
- Basic JWT auth instead of OAuth: appropriate for seeded assignment users.
- TXT/MD instead of DOCX: demonstrates the file workflow without spending the timebox on Office document parsing.
- No WebSockets: real-time conflict resolution would be a separate architectural problem.

## Next 2–4 hours

1. Add document version history.
2. Add comments and mentions.
3. Add Markdown/PDF export.
4. Add richer permission roles and share revocation.
5. Add browser E2E tests with Playwright.
