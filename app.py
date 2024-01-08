from flask import Flask, render_template
import services.file_operations as Operations
import os

app = Flask(__name__)

@app.route('/')
def index():
    command = "dir /B /A:-D /N;"
    result = Operations.display_files(command)
    path = Operations.display_current_path()

    return render_template(
        'base.html',
        result=result,
        path=path
        )

if __name__ == '__main__':
    app.run(debug=True)
