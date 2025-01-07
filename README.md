# Python Code Formatter

A web-based Python code formatter that allows users to format their Python code using different formatting styles. The available formatters are `black`, `autopep8`, `yapf`, and `isort`.

## Features

- Format Python code using `black`, `autopep8`, `yapf`, or `isort`.
- Simple web interface to input code and select formatting style.
- Display formatted code and formatting guidelines.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/python-code-formatter.git
    cd python-code-formatter
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install flask black autopep8 yapf isort
    ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open a web browser and go to `http://127.0.0.1:5000/`.

3. Enter your Python code in the provided textarea.

4. Select the desired formatting style from the dropdown menu.

5. Click the "Format Code" button to format your code.

6. The formatted code will be displayed below the form.

## Formatting Guidelines

- **Black**: The uncompromising code formatter. Formats code to PEP 8 standards.
- **Autopep8**: A tool that automatically formats Python code to conform to the PEP 8 style guide.
- **Yapf**: Yet another Python formatter from Google. Formats code to the best formatting that conforms to the style guide.
- **Isort**: A Python utility to sort imports alphabetically and automatically separate them into sections and by type.

## Directory Structure
