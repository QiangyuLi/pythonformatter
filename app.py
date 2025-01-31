from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/format', methods=['POST'])
def format_code():
    code = request.form['code']
    style = request.form['style']
    
    if style not in ['black', 'autopep8', 'yapf', 'isort']:
        return render_template('index.html', formatted_code="Invalid style selected.")
    
    try:
        if style == 'black':
            formatted_code = subprocess.run(['black', '-q', '-'], input=code.encode(), capture_output=True, check=True).stdout.decode()
        elif style == 'autopep8':
            formatted_code = subprocess.run(['autopep8', '-'], input=code.encode(), capture_output=True, check=True).stdout.decode()
        elif style == 'yapf':
            formatted_code = subprocess.run(['yapf'], input=code.encode(), capture_output=True, check=True).stdout.decode()
        elif style == 'isort':
            formatted_code = subprocess.run(['isort', '--stdout', '-'], input=code.encode(), capture_output=True, check=True).stdout.decode()
    except subprocess.CalledProcessError as e:
        formatted_code = f"Error formatting code: {e}"
    
    return render_template('index.html', formatted_code=formatted_code)

@app.route('/sort-imports', methods=['POST'])
def sort_imports():
    code = request.form['code']
    
    try:
        sorted_code = subprocess.run(['isort', '--stdout', '-'], input=code.encode(), capture_output=True, check=True).stdout.decode()
    except subprocess.CalledProcessError as e:
        sorted_code = f"Error sorting imports: {e}"
    
    return render_template('index.html', sorted_code=sorted_code)

if __name__ == '__main__':
    app.run(debug=True)