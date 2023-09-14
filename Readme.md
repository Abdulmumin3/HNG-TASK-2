# FastAPI Person API

The FastAPI Person API is a web application that provides CRUD (Create, Read, Update, Delete) operations for managing information about people. It is built using FastAPI and SQLAlchemy and provides the following endpoints:

- `POST: http://localhost:8000/api`: Add new people to the database.
- `GET: http://localhost:8000/api/{user_id}`: Retrieve a person's information based on their unique id.
- `PATCH: http://localhost:8000/api/{user_id}`: Update a person's data by their id.
- `DELETE: http://localhost:8000/api/{user_id}`: Delete a person's data based on the entered id.

## Getting Started

To run the FastAPI Person API on your local machine, follow these steps:

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repo.git

   ```

2. Change to the project directory:

   ```bash
   cd your-repo

   ```

3. Create a virtualenv with any env tool of your choice

4. Install the required Python packages:
   ```bash
   pip install -r requirements.txt

   ```

Usage

1. Start the FastAPI application:

   ```bash
   uvicorn app:app --reload

   ```

2. Access the API using the provided endpoints:

- To add a new person: POST: http://localhost:8000/api
- To get a person by id: GET: http://localhost:8000/api/{user_id}
- To update a person's data by id: PATCH: http://localhost:8000/api/{user_id}
- To delete a person by id: DELETE: http://localhost:8000/api/{user_id}

## Example 1

    POST: http://localhost:8000/api
    JSON: {
        "name": "John Doe"
        "age": 27
        "track": "Backend"
    }

### Response

    {
        "name": "John Doe"
        "age": 27
        "track": "Backend"
    }

## Example 2

    GET: http://localhost:8000/api/John Doe

### Response

    {
    "name": "John Doe"
    "age": 27
    "track": "Backend"
    }

## API Endpoints

### POST /api

    Use this endpoint to add new people to the database. Send a POST request with JSON data containing the person's information .

### GET /api/{user_id}

    Retrieve a person's information based on their unique id. Replace {id} in the URL with the person's actual id.

### PATCH /api/{user_id}

    Update a person's data by their id. Replace {id} in the URL with the person's actual id. Send a PUT request with JSON data containing the updated information.

### DELETE /api/{user_id}

    Delete a person's data based on the entered id. Replace {id} in the URL with the person's actual id.

### Acknowledgments

- FastAPI: https://fastapi.tiangolo.com/
- SQLAlchemy: https://www.sqlalchemy.org/
- Feel free to customize this README to include your specific project details, such as repository links, installation instructions, and any additional information about your project's usage, contributors, or deployment instructions.
  GET /api/{id}
  Retrieve a person's information based on their unique id. Replace {id} in the URL with the person's actual id.
  PATCH /api/{id}
  Update a person's data by their id. Replace {id} in the URL with the person's actual id. Send a PUT request with JSON data containing the updated information.
  DELETE /api/{id}
  Delete a person's data based on the entered id. Replace {id} in the URL with the person's actual id.
