# Student Registration

A small student registration app built with Flask and SQLite. It supports adding, searching, and removing student registrations. Docker Compose runs the application in its own container and keeps records in a persistent named volume.

## Requirements

- Git
- Docker Desktop (includes Docker Compose)
- A GitHub account to publish the source

## Run with Docker

Open a terminal in this project folder and build/start the app:

```powershell
docker compose up --build -d
```

Open <http://localhost:5000>. Check the container and health status with:

```powershell
docker compose ps
docker compose logs -f
```

Stop the app and container:

```powershell
docker compose down
```

The `student-data` Docker volume retains registrations when the container stops or is recreated. To permanently delete the database too, run `docker compose down --volumes`.

## Run locally (without Docker)

Python 3.12 or newer is recommended.

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Then visit <http://localhost:5000>. The local SQLite database is created at `data/students.db`.

## Publish the source to GitHub

Create an empty repository on GitHub (do not initialize it with a README), then from this project folder run:

```powershell
git init
git add .
git commit -m "Initial student registration app"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the remote URL with the HTTPS URL shown by GitHub. GitHub may ask you to authenticate through a browser or credential manager. Future source updates can be published with:

```powershell
git add .
git commit -m "Describe your change"
git push
```

## Configuration

Compose maps port `5000` on your computer to port `5000` in the container. Change the left-hand port in `compose.yaml` if 5000 is already in use, for example `8080:5000`, then open `http://localhost:8080`.

For deployment, set a private `SECRET_KEY` environment variable rather than using the development default. This starter is intended for local development and demonstrations; add authentication, HTTPS, backups, and appropriate privacy controls before handling real student records.