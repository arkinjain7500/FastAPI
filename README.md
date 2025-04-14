# FastAPI Project

## Overview

This is a FastAPI application that serves as a template for building APIs quickly and efficiently. FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

## Features

- Fast to code: Increase the speed to develop features by about 200% to 300%.
- Fewer bugs: Reduce about 40% of human (developer) induced errors.
- Intuitive: Great editor support. Completion everywhere.
- Easy: Learning path for new developers.
- Short: Minimize code duplication.
- Robust: Get production-ready code with automatic interactive documentation.

## Requirements

- Python 3.6 or higher
- FastAPI
- Uvicorn (for serving the application)

## Installation

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. Install FastAPI and Uvicorn:
   ```bash
   pip install "fastapi[all]"
   ```

## Running the Application

To run the application, use the following command:

```bash
uvicorn main:app --reload
```

## Accessing the API

Once the server is running, you can access the API at:

- **Root Endpoint**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Interactive API Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative Docs**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Example Usage

You can test the API using tools like Postman or directly from the interactive documentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
