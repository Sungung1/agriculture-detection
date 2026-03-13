from __future__ import annotations

from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

PROJECT_ROOT = Path(__file__).resolve().parents[2]
UPLOAD_FOLDER = PROJECT_ROOT / "data" / "uploads"


def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder=str(PROJECT_ROOT / "templates"),
        static_folder=str(PROJECT_ROOT / "static"),
    )
    UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
    app.config["UPLOAD_FOLDER"] = str(UPLOAD_FOLDER)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/startpoint")
    def startpoint():
        return render_template("startpoint.html")

    @app.route("/upload", methods=["GET", "POST"])
    def upload():
        if request.method == "GET":
            return render_template("upload.html")

        file = request.files.get("file")
        if file is None or file.filename == "":
            return redirect(request.url)

        file.save(UPLOAD_FOLDER / secure_filename(file.filename))
        return redirect(url_for("upload"))

    @app.route("/<path:name>")
    def static_page(name: str):
        return render_template(name)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
