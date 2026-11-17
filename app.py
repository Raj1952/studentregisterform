import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path

from flask import Flask, flash, jsonify, redirect, render_template, request, url_for


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "local-development-key")
DATABASE_PATH = Path(os.environ.get("DATABASE_PATH", "data/students.db"))


@contextmanager
def get_db():
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()


def initialize_db():
    with get_db() as connection:
        connection.execute(
            """CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                email TEXT NOT NULL COLLATE NOCASE UNIQUE,
                course TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )"""
        )


@app.get("/")
def index():
    query = request.args.get("q", "").strip()
    with get_db() as connection:
        if query:
            pattern = f"%{query}%"
            students = connection.execute(
                """SELECT * FROM students
                   WHERE full_name LIKE ? OR email LIKE ? OR course LIKE ?
                   ORDER BY created_at DESC, id DESC""",
                (pattern, pattern, pattern),
            ).fetchall()
        else:
            students = connection.execute(
                "SELECT * FROM students ORDER BY created_at DESC, id DESC"
            ).fetchall()
        total = connection.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    return render_template("index.html", students=students, query=query, total=total)


@app.post("/register")
def register():
    full_name = request.form.get("full_name", "").strip()
    email = request.form.get("email", "").strip().lower()
    course = request.form.get("course", "").strip()

    if not full_name or not email or not course:
        flash("Please complete every field.", "error")
        return redirect(url_for("index"))

    try:
        with get_db() as connection:
            connection.execute(
                "INSERT INTO students (full_name, email, course) VALUES (?, ?, ?)",
                (full_name, email, course),
            )
    except sqlite3.IntegrityError:
        flash("That email address is already registered.", "error")
        return redirect(url_for("index"))

    flash(f"{full_name} is registered.", "success")
    return redirect(url_for("index"))


@app.post("/students/<int:student_id>/delete")
def delete_student(student_id):
    with get_db() as connection:
        connection.execute("DELETE FROM students WHERE id = ?", (student_id,))
    flash("Registration removed.", "success")
    return redirect(url_for("index"))


@app.get("/health")
def health():
    try:
        with get_db() as connection:
            connection.execute("SELECT 1")
        return jsonify(status="ok"), 200
    except sqlite3.Error:
        return jsonify(status="error"), 503


initialize_db()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))