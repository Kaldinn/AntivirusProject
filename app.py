from flask import Flask, render_template, request, jsonify
from services.operations import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/scan', methods=['POST'])
def scan():
    uploaded_file = request.files['file']
    file_content = uploaded_file.read()
    
    file_hash = calculate_file_hash(file_content)
    scan_result = scan_file_content(file_content)

    return jsonify(
        {
            'status': 'success',
            'file_name': uploaded_file.filename,
            'hash': file_hash,
            'scan_result': scan_result,
            'file_content': file_content.decode('utf-8')
        })

if __name__ == '__main__':
    app.run(debug=True)
