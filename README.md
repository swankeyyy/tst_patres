# Library

This is a test task for Patres, implemented using FastAPI and SQLAlchemy with asynchronous support.

## Project Structure

- `app/main.py`: The main entry point of the application.
- `alembic.ini`: Configuration file for Alembic, used for database migrations.
- `pytest.ini`: Configuration file for pytest, used for running tests.
- `conftest.py`: Contains fixtures for setting up the test environment.

## Setup

1. **Clone the repository:**
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run database migrations:**
    ```sh
    alembic upgrade heads
    ```

## Running the Application

To start the FastAPI application, run:
```sh
uvicorn app.main:app --reload