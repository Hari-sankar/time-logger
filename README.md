# Time Logger

An AI-powered timesheet assistant built with FastAPI and LangChain, using tool-calling agents to log work, validate inputs, and send reminders.

## About The Project

This project is a conversational AI agent that helps users log their work hours for different tasks and projects. It uses a WebSocket-based chat interface for real-time, stateful communication. The agent is built with LangChain's tool-calling capabilities, allowing it to perform actions like logging time, validating user inputs, and checking for similar tasks.

The key features include:

*   **Conversational Time Logging**: A user-friendly chat interface to log time.
*   **Real-Time Interaction**: WebSocket connection for immediate feedback.
*   **Intelligent Validation**: The agent enforces rules, such as daily hour limits.
*   **Extensible Tools**: Easily add new capabilities to the agent.
*   **In-Memory Chat History**: Ensures privacy by storing chat history in memory for the session's duration.

## Project Structure

```
.
├── app
│   ├── agents
│   │   └── chat_agent.py         # LangGraph agent definition
│   ├── core
│   │   └── config.py             # Application configuration
│   ├── db
│   │   ├── init.sql              # Database initialization script
│   │   ├── migration.py          # Database migration logic
│   │   └── session.py            # Database session management
│   ├── routes
│   │   ├── auth_routes.py        # Authentication routes
│   │   └── chat_routes.py        # WebSocket chat routes
│   ├── schemas
│   │   ├── auth.py               # Pydantic schemas for auth
│   │   └── response.py           # Pydantic schemas for responses
│   ├── services
│   │   ├── auth_service.py       # Authentication logic
│   │   └── chat_service.py       # Chat handling logic
│   ├── shared
│   │   └── constants.py          # Application constants
│   ├── tools
│   │   ├── project_management.py # Tools for project management
│   │   ├── task_managemet        # Tools for task management
│   │   └── time_entry            # Tools for time entry
│   ├── utils
│   │   ├── jwt.py                # JWT handling
│   │   ├── password_handler.py   # Password hashing
│   │   └── ws_auth.py            # WebSocket authentication
│   └── main.py                   # FastAPI application entry point
├── .env.example                  # Example environment variables
├── .gitignore
├── Makefile
├── pyproject.toml                # Project dependencies
├── README.md
└── uv.lock
```

## Getting Started

### Prerequisites

*   Python 3.12+
*   `uv` for package management
*   PostgreSQL database

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/time-logger.git
    cd time-logger
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    uv sync
    or
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**
    Copy the `.env.example` file to `.env` and update it with your database credentials and a secret key.
    ```bash
    cp .env.example .env
    ```

### Running the Application

1.  **Set up the database:**
    Make sure your PostgreSQL server is running and the database specified in your `.env` file exists.

2.  **Run database migrations:**
    The application will automatically run migrations on startup if `MIGRATION` is set to `True` in your `.env` file.

3.  **Start the FastAPI server:**
    ```bash
    uvicorn app.main:app --reload
    ```
    The application will be available at `http://127.0.0.1:8000`.

## Usage

1.  **Register a new user:**
    Send a `POST` request to `/register` with a username and password.

2.  **Log in:**
    Send a `POST` request to `/login` to get a JWT token.

3.  **Connect to the WebSocket:**
    Connect to the `/ws` endpoint with the JWT token in the `Authorization` header (e.g., `ws://127.0.0.1:8000/ws?token=YOUR_TOKEN`).

4.  **Chat with the agent:**
    Start sending messages to the agent to log your time. For example:
    *   "Log 2 hours on the 'API development' task for the 'Time Logger' project."
    *   "What tasks have I logged today?"
