# Ajaia Docs — AI Workflow Note

## Overview

AI tools were used as development accelerators throughout the assignment, particularly for scaffolding, debugging, implementation suggestions, test ideas, and documentation.

AI was used as an engineering assistant rather than as a replacement for product or technical judgment.

The final architecture, scope decisions, feature prioritization, integration decisions, testing, and verification remained my responsibility.

## AI Tools Used

* ChatGPT
* AI-assisted coding and debugging during implementation

## Where AI Materially Sped Up Development

### Project Scaffolding

AI helped accelerate the initial project structure and boilerplate for:

* React + TypeScript components
* FastAPI routes
* SQLAlchemy models
* Pydantic schemas
* Authentication flow
* API service functions

This reduced repetitive setup work and allowed more time to focus on the actual product workflow.

### Debugging

AI was used to reason through implementation errors and suggest likely causes and fixes.

Suggestions were not accepted blindly. Changes were tested locally after implementation.

### API and Validation

AI helped identify validation and error-handling cases such as:

* Invalid authentication
* Missing document data
* Unsupported file types
* Oversized files
* Unauthorized document access
* Invalid sharing targets

### Testing

AI was used to suggest meaningful test cases, particularly around document sharing and authorization.

The focus was on testing actual product behavior rather than only testing that endpoints returned successful responses.

### Documentation

AI helped structure and refine the README, architecture note, submission information, and this AI workflow note.

The final documentation was reviewed and adapted to match the implementation and actual deployment setup.

## Example of Engineering Judgment

One important design decision was keeping ownership and sharing separate.

A simpler implementation could have placed sharing information directly inside a document object. Instead, the implementation uses a separate `document_shares` relationship.

This was preferred because:

* One document can be shared with multiple users.
* Ownership remains distinct from shared access.
* Authorization logic remains easier to reason about.
* Additional permission types can be added later.

AI suggestions were treated as alternatives rather than automatically accepted implementation decisions.

## What I Changed or Rejected

Generated implementation suggestions were reviewed against the assignment requirements and the existing application architecture.

Where a suggestion introduced unnecessary complexity, additional dependencies, or functionality outside the timebox, it was simplified or rejected.

Examples include avoiding:

* A heavy collaborative editing framework for a basic editor requirement.
* Complex enterprise authentication; a lightweight JWT-based authentication flow is used for the demo.
* DOCX parsing when TXT/MD already demonstrates the required file workflow.
* Real-time collaboration before completing the mandatory document and sharing flows.

The goal was to maximize reliability and completeness within the 4–6 hour constraint.

## How Correctness Was Verified

AI-generated or AI-assisted code was verified through:

1. Local application execution.
2. Manual testing of the main user flows.
3. API testing through the backend.
4. Testing document persistence after refresh/reopen.
5. Testing file import behavior.
6. Testing sharing using separate demo users.
7. Testing unauthorized document access.
8. Running automated backend tests.
9. Testing the deployed frontend and backend after deployment.

## How UX Quality Was Verified

The main flows were manually tested from a user's perspective:

```text
Login
  ↓
Create document
  ↓
Rename
  ↓
Format content
  ↓
Save
  ↓
Reopen
  ↓
Import file
  ↓
Share document
  ↓
Login as another user
  ↓
Open shared document
```

The intent was to ensure that the application was not merely API-complete but also understandable and usable as a product.

## How AI Was Used Responsibly

AI output was treated as a starting point.

I verified:

* Whether the generated code matched the actual project structure.
* Whether API contracts matched frontend usage.
* Whether authorization rules were enforced on the backend.
* Whether database relationships were appropriate.
* Whether generated changes introduced unnecessary dependencies.
* Whether the implementation actually satisfied the assignment requirements.

When an AI-generated approach conflicted with the desired scope or architecture, it was modified or discarded.

## AI and Product Judgment

The most important decisions were made based on the assignment constraints rather than on how much functionality could be generated.

The main product decision was to prioritize a complete document lifecycle and reliable sharing over optional features such as real-time collaboration, comments, and version history.

This allowed the final product to remain focused, testable, deployable, and understandable within the available time.

## Future AI Usage

With additional development time, AI would continue to be useful for:

* Generating additional automated test cases
* Reviewing edge cases
* Improving accessibility
* Reviewing API security
* Generating browser end-to-end tests
* Refactoring repetitive code

Human review and testing would remain part of each of these workflows.
