# Ajaia Docs Assignment Submission

## Live Application

Frontend: `https://ajaia-docs-three-zeta.vercel.app`

The application is deployed and available for browser-based testing.

## API

Backend: `https://ajaia-docs-backend.onrender.com`

API documentation: `https://ajaia-docs-backend.onrender.com/docs`

## Demo Credentials

### Owner

* Email: `mohim@ajaia.dev`
* Password: `Demo@123`

### Shared User

* Email: `jane@ajaia.dev`
* Password: `Demo@123`

## Product Overview

Ajaia Docs is a lightweight collaborative document editor focused on the core document workflow: creating, editing, importing, persisting, and sharing documents between users.

## Included

* React + TypeScript + Vite frontend
* FastAPI REST backend
* SQLAlchemy persistence layer
* PostgreSQL production database support
* SQLite local development support
* JWT authentication
* Rich document editor
* Bold, italic and underline formatting
* Headings
* Bulleted and numbered lists
* Document creation and renaming
* Document persistence and reopening
* TXT/Markdown file import
* Document ownership
* Document sharing
* Owned and shared document separation
* Backend authorization checks
* Input validation and error handling
* Automated authorization test
* Render deployment configuration
* README and architecture documentation
* AI workflow documentation

## Working Features

The mandatory product requirements are implemented and can be demonstrated through the deployed application:

1. User authentication
2. Document creation
3. Document renaming
4. Browser-based rich-text editing
5. Document saving and reopening
6. Persistence across refreshes
7. TXT/MD file import
8. Document ownership
9. Sharing with another user
10. Shared document access
11. Owned vs shared document distinction
12. Backend authorization for document access

## File Import

Supported file types:

* `.txt`
* `.md`

Maximum supported file size: 2 MB.

Imported content is converted into an editable document.

## Intentional Limitations

The following functionality was intentionally excluded from the core implementation to stay within the assignment timebox:

* TXT and Markdown are the only supported import formats.
* Sharing currently provides editor access.
* Real-time simultaneous editing is not implemented.
* Comments and suggestion mode are not implemented.
* Version history is not included in the core build.
* Enterprise-level permission management is outside the current scope.

These were deliberate scope decisions rather than unfinished core requirements.

## What I Would Build Next With Another 2–4 Hours

I would prioritize:

1. Document version history with restore capability.
2. Share revocation.
3. More granular sharing permissions such as viewer/editor.
4. Browser-level end-to-end tests.
5. Markdown/PDF export.

Real-time collaboration would be considered separately because it requires WebSockets, concurrent editing synchronization, conflict handling, and a more advanced document model.

## Deployment

* Frontend: Vercel
* Backend: Render
* Production database: Neon PostgreSQL
* Local development database: SQLite

## Source Code

The complete source code and project documentation are included in the submitted project folder.

## Automated Testing

The backend includes automated tests covering document authorization/sharing behavior.

## Walkthrough Video

The public walkthrough URL is provided separately in:

`VIDEO_URL.txt`
