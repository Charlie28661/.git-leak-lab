from flask import Flask, send_from_directory, request
import os

app = Flask(__name__)

BASE_DIR = os.path.abspath(".")

@app.route("/")
def index():
    return "這個網站似乎有些敏感資料被錯誤公開了 🤔"

@app.route("/.git/<path:filename>")
def git_leak(filename):
    """ 允許訪問 `.git/` 目錄，模擬 Git 洩露 """
    git_path = os.path.join(BASE_DIR, ".git")

    if not os.path.commonprefix([os.path.abspath(os.path.join(git_path, filename)), git_path]) == git_path:
        return "Access denied!", 403

    return send_from_directory(git_path, filename)

if __name__ == "__main__":
    app.run(debug=True)

