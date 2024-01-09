from flask import Flask, render_template, request, jsonify
from services.operations import *

app = Flask(__name__)

@app.route('/')
def index():
    x = scan_directory("C:/")
    print(x)
    return render_template('base.html')
    

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    directory_to_scan = data.get('directory', '/path/to/default/directory')

    try:
        scan_results = scan_directory(directory_to_scan)
        return jsonify({'status': 'success', 'results': scan_results})
    except Exception as e:
        return jsonify({'status': 'error', 'error_message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
