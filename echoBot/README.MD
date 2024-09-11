
# Python Application with Docker

This project demonstrates how to run a Python application using Docker and Docker Compose, as well as running it locally without Docker.

## Project Structure

```
.
├── Dockerfile
├── docker-compose.yml
├── run.py
├── requirements.txt
└── README.md
```

## Prerequisites

Before you start, make sure you have the following installed:

- Python 3.9 or higher (if running without Docker)
- Docker
- Docker Compose

---

## Running the Application

### 1. Running with Docker Compose

#### Steps:

1. Clone this repository or download the project files.
2. Inside docker-compose change API_TOKEN value   
3. Build and start the Docker container:
   ```bash
   docker-compose up --build
   ```

4. Docker Compose will build the image, install dependencies from `requirements.txt`, and run the application.

5. The app should be accessible as specified in `run.py`. If it's a web app, check `localhost:8000`.

#### Stopping the Application:
To stop the app, use:
```bash
docker-compose down
```

---

### 2. Running without Docker

If you want to run the project locally without Docker, follow these steps:

#### Steps:

1. Clone the repository or download the project files.

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   export API_TOKEN=BOT_TOKEN
   For windows:
   set API_TOKEN=BOT_TOKEN
 
   python run.py
   ```

#### Stopping the Application:
To stop the app, press `CTRL + C` in your terminal.

---

## How to Generate `requirements.txt`

If you've installed new packages and want to update `requirements.txt`, run the following command:

```bash
pip freeze > requirements.txt
```

This command will list all installed packages in your environment and their versions, saving them to the `requirements.txt` file.

---