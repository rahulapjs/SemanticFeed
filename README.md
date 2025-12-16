# SemanticFeed

A full-stack news aggregator application built with FastAPI (Backend) and React/Vite (Frontend).

## Project Structure

-   `backend/`: FastAPI application with PostgreSQL, SQLAlchemy, and a background worker for scraping.
-   `frontend/`: React + TypeScript application with Redux Toolkit and a modern Glassmorphism UI.

## Getting Started

### Prerequisites

-   Docker & Docker Compose (Recommended)
-   Or: Python 3.11+, Node.js 20+, PostgreSQL

### Environment Setup

1.  Copy the root `.env.example` to `.env`:
    ```bash
    cp .env.example .env
    ```
2.  Update `.env` with your real keys (especially `GOOGLE_API_KEY`).

### Running with Docker (Easiest)

1.  Run the stack:
    ```bash
    docker-compose up --build
    ```
2.  Access the app:
    -   Frontend: [http://localhost](http://localhost)
    -   Backend API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

### Running Locally (Manual)

#### Backend

1.  Navigate to `backend`:
    ```bash
    cd backend
    ```
2.  Create virtual env and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    pip install -r requirements.txt
    ```
3.  Set up environment variables. You can set `DATABASE_URL` directly OR set the components:
    -   `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`, `POSTGRES_SERVER`, `POSTGRES_PORT`
4.  Run server:
    ```bash
    uvicorn app.main:app --reload
    ```

#### Frontend

1.  Navigate to `frontend`:
    ```bash
    cd frontend
    ```
2.  Install dependencies:
    ```bash
    npm install
    ```
3.  Set up `.env` (see `.env.example` in frontend folder).
4.  Start dev server:
    ```bash
    npm run dev
    ```

## Development

-   **Linting**: A GitHub Actions workflow (`.github/workflows/lint.yml`) runs on push to check code quality.
-   **Cleanup**: To delete old news (older than 7 days), run:
    ```bash
    cd backend
     python cleanup.py
    ```

## License

[MIT](LICENSE)
