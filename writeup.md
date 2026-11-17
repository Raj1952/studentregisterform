# Student Registration Project Write-up

## Aim
- Build a simple app to register, search, and remove students.
- Run it in Docker and keep its records in persistent storage.
- Track the source code with Git and GitHub.

## Process
- Created the app using Python, Flask, and SQLite.
- Added a web form and a table to manage student registrations.
- Added a Dockerfile and Docker Compose configuration.
- Connected the local Git repository to GitHub.

## Basic Commands
- Start the app: `docker compose up --build -d`
- Check container status: `docker compose ps`
- View container logs: `docker compose logs -f`
- Stop the app: `docker compose down`
- Check code changes: `git status`
- Save a version: `git add .` then `git commit -m "Describe the change"`
- Send it to GitHub: `git push`

## Results
- Registration, search, duplicate-email handling, deletion, and health checks passed.
- The Docker container ran successfully and stored data in a named volume.
- The initial source and demo guide are on [GitHub](https://github.com/Raj1952/studentregisterform).
- Check `git status`; if the local branch is ahead, run `git push` to publish the newer commits.

## Conclusion
- The project demonstrates a basic web application, Docker containerization, persistent data, and Git version control.