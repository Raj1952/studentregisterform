import os
import sqlite3
from pathlib import Path

from flask import Flask, flash, jsonify, redirect, render_template, request, url_for


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "local-development-key")
DATABASE_PATH = Path(os.environ.get("DATABASE_PATH", "data/students.db"))


def connect_db():
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_db():
    connection = connect_db()
    connection.execute(
        """CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL COLLATE NOCASE UNIQUE,
            course TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )"""
    )
    connection.commit()
    connection.close()


@app.get("/")
def index():
    query = request.args.get("q", "").strip()
    pattern = f"%{query}%"
    connection = connect_db()
    students = connection.execute(
        """SELECT * FROM students
           WHERE full_name LIKE ? OR email LIKE ? OR course LIKE ?
           ORDER BY created_at DESC, id DESC""",
        (pattern, pattern, pattern),
    ).fetchall()
    total = connection.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    connection.close()
    return render_template("index.html", students=students, query=query, total=total)


@app.post("/register")
def register():
    full_name = request.form.get("full_name", "").strip()
    email = request.form.get("email", "").strip().lower()
    course = request.form.get("course", "").strip()

    if not full_name or not email or not course:
        flash("Please complete every field.", "error")
        return redirect(url_for("index"))

    connection = connect_db()
    try:
        connection.execute(
            "INSERT INTO students (full_name, email, course) VALUES (?, ?, ?)",
            (full_name, email, course),
        )
        connection.commit()
    except sqlite3.IntegrityError:
        flash("That email address is already registered.", "error")
        return redirect(url_for("index"))
    finally:
        connection.close()

    flash(f"{full_name} is registered.", "success")
    return redirect(url_for("index"))


@app.post("/students/<int:student_id>/delete")
def delete_student(student_id):
    connection = connect_db()
    connection.execute("DELETE FROM students WHERE id = ?", (student_id,))
    connection.commit()
    connection.close()
    flash("Registration removed.", "success")
    return redirect(url_for("index"))


@app.get("/health")
def health():
    connection = connect_db()
    try:
        connection.execute("SELECT 1")
        return jsonify(status="ok"), 200
    except sqlite3.Error:
        return jsonify(status="error"), 503
    finally:
        connection.close()


initialize_db()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))