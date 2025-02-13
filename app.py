from flask import Flask, request, render_template
import subprocess
import ast

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
    
    # Check for import issues
    import_issues = check_import_issues(code)
    if import_issues:
        formatted_code += f"\n\n{import_issues}"
    
    # Add other code evaluations here
    evaluation_report = evaluate_code(code)
    if evaluation_report:
        formatted_code += f"\n\n{evaluation_report}"
    
    return render_template('index.html', formatted_code=formatted_code)

def check_import_issues(code):
    try:
        tree = ast.parse(code)
        imported_modules = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imported_modules.add(alias.asname or alias.name)
            elif isinstance(node, ast.ImportFrom):
                imported_modules.add(node.module)
        
        used_modules = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
                used_modules.add(node.value.id)
        
        missing_imports = used_modules - imported_modules
        if missing_imports:
            return f"Error: The following modules are used but not imported: {', '.join(missing_imports)}"
    except SyntaxError as e:
        return f"Syntax error in code: {e}"
    
    return None

def evaluate_code(code):
    # Placeholder for additional code evaluations
    # You can add more checks here and return a report
    report = []
    
    # Example check: Check for TODO comments
    if 'TODO' in code:
        report.append("Note: There are TODO comments in the code.")
    
    return "\n".join(report) if report else None

@app.route('/sort-imports', methods=['POST'])
def sort_imports():
    code = request.form['code']
    confirm = request.form.get('confirm')
    
    if confirm != 'on':
        return render_template('index.html', sorted_code="Sorting imports not confirmed.")
    
    try:
        sorted_code = subprocess.run(['isort', '--stdout', '-'], input=code.encode(), capture_output=True, check=True).stdout.decode()
    except subprocess.CalledProcessError as e:
        sorted_code = f"Error sorting imports: {e}"
    
    return render_template('index.html', sorted_code=sorted_code)

if __name__ == '__main__':
    app.run(debug=True)