# Student Registration Project Write-up

## Aim
- Build a simple app to register, search, and remove students.
- Run it in Docker and keep its records in persistent storage.
- Track the source code with Git and GitHub.

## Process
- Created the app using Python and Flask, with SQLite to store student details.
- Built a form to enter each student's name, email, and course.
- Added routes to register students, show and search the list, and delete a record.
- Prevented empty fields and duplicate email addresses.
- Created a Dockerfile to package the app and a Compose file to run it on port 5000.
- Added a named Docker volume so the database remains after the container stops.
- Started the container and checked the app page, health endpoint, and registration actions.
- Initialized a Git repository, committed the source, and pushed it to GitHub.

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