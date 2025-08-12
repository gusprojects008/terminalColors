# terminalColors

A simple utility for printing colored text in the terminal.

## Installation

### 1) Create and activate a `venv`

```bash
python3 -m venv.venv
source .venv/bin/activate
```
### 2) Install directly from GitHub (always get the `main`/`default` branch)

```bash
pip install --update pip
pip install git+https://github.com/gusprojects008/terminalColors.git
```

### 3) Install a specific tag/version or commit

```bash
pip install git+https://github.com/gusprojects008/terminalColors.git@v0.0.0
```

### 4) Add `requirements.txt`

Place one of the lines below in your project's `requirements.txt`:

Always get the latest version of Repository

```text
git+https://github.com/gusprojects008/terminalColors.git
```
Or pin to a specific tag:

```text
git+https://github.com/gusprojects008/terminalColors.git@v0.0.0
```

Then, to install all dependencies:

```bash
pip install -r requirements.txt
```
---

## Usage

```python
from terminalColors import Colors
colors = Colors("", "")
print(Colors("blue", "Hello World"))
```
