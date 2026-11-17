# Student Registration Demo Guide

## Short introduction

> I built a simple student registration app using Flask and SQLite. First, I made a form to add students and a page to search and view registrations. Then I packaged the app in Docker and used a persistent volume for its data. Finally, I pushed the source code to GitHub so changes can be tracked and shared.

## Run the demo

1. Open Docker Desktop and wait for it to finish starting.
2. In VS Code, open the project folder and a PowerShell terminal.
3. Start the app:

   ```powershell
   docker compose up --build -d
   ```

4. Open Docker Desktop's **Containers** page. Find the `devops-lab` project and its `student-registration` container. Show that it is running; expand it to view logs if asked.
5. Open <http://localhost:5000> in a browser. Add a fictional student, search for the student, and show the result in the list. Delete only the sample record you just added.

## Show version control

1. Open <https://github.com/Raj1952/studentregisterform> and show the `main` branch and its commit history.
2. In VS Code's Source Control view, show the project files. In the terminal, run:

   ```powershell
   git status
   git log --oneline -3
   git remote -v
   ```

3. Explain the normal update process: edit a file, review it with `git diff`, then save and publish the version:

   ```powershell
   git add README.md
   git commit -m "Update project documentation"
   git push
   ```

   For a real example, make a small README edit before running these commands. Then refresh GitHub to show the new commit.

## Finish

Stop the app when the demo is over:

```powershell
docker compose down
```

This stops the container but keeps the database volume. Do not use `docker compose down --volumes` during the demo; that deletes the stored registrations.