from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/execute_script')
def execute_script():
    file = request.args.get('file')
    if file and os.path.exists(file):
        result = subprocess.run(['python', file], capture_output=True, text=True)
        return f"<pre>{result.stdout}</pre><pre>{result.stderr}</pre>"
    else:
        return "No script specified or file does not exist."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
