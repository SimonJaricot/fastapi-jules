# FastAPI Project

This is a simple project to demonstrate the features of FastAPI.

## About FastAPI

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.12+ based on standard Python type hints.

The key features are:
- **Fast**: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic).
- **Fast to code**: Increase the speed to develop features by about 200% to 300%.
- **Fewer bugs**: Reduce about 40% of human-induced errors.
- **Intuitive**: Great editor support. Completion everywhere. Less time debugging.
- **Easy**: Designed to be easy to use and learn. Less time reading docs.
- **Short**: Minimize code duplication. Multiple features from each parameter declaration.
- **Robust**: Get production-ready code. With automatic interactive documentation.
- **Standards-based**: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

## Installation

To run this project, you need to have Python 3.12+ and `uv` installed.

### Installing uv

`uv` is a fast Python package installer and resolver, written in Rust.

**macOS and Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Project Dependencies

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Create a virtual environment and install the dependencies using `uv`:
   ```bash
   uv venv
   uv pip sync pyproject.toml
   ```

## How to run the application

To run the application, first activate the virtual environment:

**macOS and Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```powershell
.venv\Scripts\activate
```

Then, run the application using `uvicorn`:

```bash
uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## Running Tests

To run the tests, you first need to install the test dependencies. Note that this command will also install the project in editable mode:

```bash
uv pip install -e .[test]
```

Once the dependencies are installed, you can run the tests using `pytest`:

```bash
pytest
```

## Available API Endpoints

The application has the following endpoints:

- **`GET /`**: Returns a greeting message.
  - **Response:** `{"message": "Hello, World!"}`

- **`GET /items/{item_id}`**: Returns a message with the item ID.
  - **`item_id`** (integer, path parameter): The ID of the item.
  - **Response:** `{"item_id": 123}` (for `item_id=123`)

- **`GET /items`**: Returns a list of items.
  - **Response:** `{"items": ["item1", "item2", "item3"]}`

You can also access the interactive API documentation (Swagger UI) at `http://127.0.0.1:8000/docs`.
