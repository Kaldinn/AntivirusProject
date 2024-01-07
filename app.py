from flask import Flask, render_template
from services.file_operations import display_files, display_current_path
import os

app = Flask(__name__)

@app.route('/')
def index():
    command = "dir /B /A:-D /N;"
    result = display_files(command)
    path = display_current_path()

    return render_template(
        'base.html',
        result=result,
        path=path
        )

if __name__ == '__main__':
    app.run(debug=True)
