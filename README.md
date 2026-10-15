# Roast My Code

**Roast My Code** is a CLI (Command Line Interface) linter for Python, designed to identify and penalize common bad practices in source code. Unlike traditional linters that provide dry, technical error messages, this tool analyzes your .py files and exposes questionable programming decisions through a sarcastic and humorous approach.

## Features & Analysis Rules

The tool processes files line by line and utilizes regular expressions (regex) to identify various anti-patterns:

- **Single-letter variables:** Detects variables lacking semantic meaning (e.g., x = 5).
- **Bare exceptions (except:):** Penalizes global exception suppression without specific error handling.
- **pass statements:** Calls out incomplete logic abandoned in code blocks.
- **TODO comments:** Identifies forgotten "technical debt" left in comments.
- **Primitive debugging:** Detects the use of print() with debug strings like "test", "here", or "123".
- **Excessively long lines:** Identifies lines that exceed standard character limits, affecting readability.
- **Infinite loops:** Points out dangerous constructs like while True:.

## Technologies Used

- **Python 3** - Core application logic.
- **re (RegEx)** - Used for complex pattern matching and syntax extraction.
- **rich** - Third-party library used for terminal output formatting, color support, and rendering structured tables.

## Installation & Setup

1. **Clone the repository:**
git clone https://github.com/Lakaka2003/roast-my-code.git
cd roast-my-code

2. **Set up a virtual environment (recommended):**
python3 -m venv venv
source venv/bin/activate

3. **Install dependencies:**
pip install -r requirements.txt

## Usage

To initiate a static analysis on a Python file, run the main script passing the file path as a CLI argument:

python3 roast.py test.py

If any infractions are detected, the output will be displayed as a detailed table containing the affected line, the code snippet, and the corresponding roast.
