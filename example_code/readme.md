# Simple Tutorial on Debugging a Python Program in VS Code

Debugging is an essential skill in programming, and VS Code provides a powerful built-in debugger for Python. Here’s a step-by-step tutorial to debug a Python program using VS Code.

---

## **1. Set Up Your Python Environment**
1. **Install Python Extension**: Ensure you have the Python extension installed in VS Code.
   - Go to the **Extensions Marketplace** (Ctrl+Shift+X or Cmd+Shift+X on Mac).
   - Search for "Python" and install the extension published by Microsoft.

2. **Select Python Interpreter**:
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open the Command Palette.
   - Search for **Python: Select Interpreter** and select the Python version you want to use.

3. **Prepare a Sample Python Program**:
   Create a Python file (e.g., `example.py`) with the following code:

   ```python
   def add(a, b):
       return a + b

   def subtract(a, b):
       return a - b

   def main():
       x = 10
       y = 5
       print("Addition:", add(x, y))
       print("Subtraction:", subtract(x, y))

   if __name__ == "__main__":
       main()
   ```

---

## **2. Add Debugging Configuration**
1. Open the Debug view by clicking the **Run and Debug** icon on the left sidebar or pressing `Ctrl+Shift+D` (Cmd+Shift+D on Mac).
2. Click on **Create a launch.json file**.
3. Select **Python File** as the configuration.

This will generate a basic `launch.json` file in the `.vscode` folder, enabling debugging for Python files.

---

## **3. Set Breakpoints**
- **What is a Breakpoint?**
   A breakpoint pauses program execution so you can examine variables and the program's state.

- To set a breakpoint:
   - Click on the left margin next to the line number in the editor.
   - For example, set a breakpoint on the `x = 10` line in the `main` function.

---

## **4. Start Debugging**
1. Click the **Run and Debug** button (green play button) in the Debug view.
2. Alternatively, press `F5` to start debugging.

---

## **5. Debugging Actions**
When the program hits the breakpoint, the execution pauses. Use the Debug toolbar to control execution:

- **Continue (F5)**: Resume execution until the next breakpoint.
- **Step Over (F10)**: Execute the current line and move to the next line in the same scope.
- **Step Into (F11)**: Enter the function or method on the current line.
- **Step Out (Shift+F11)**: Exit the current function and return to the caller.
- **Restart (Ctrl+Shift+F5)**: Restart debugging.
- **Stop (Shift+F5)**: Stop debugging.

---

## **6. Inspect Variables**
- Use the **Variables pane** in the Debug view to see the values of variables.
- Hover over variables in the code editor to see their current value.
- Add expressions to the **Watch** panel to monitor specific variables or expressions.

---

## **7. Debug Console**
- The **Debug Console** allows you to execute Python commands in the current context.
- For example, while paused at a breakpoint, type `x + y` in the Debug Console to see the sum.

---

## **8. Modify and Test**
- Modify code as needed based on your findings and restart the debugger to test changes.

---
# Unit Testing/Pytest
- Create Venv
   -  Command Palette
      -  View/Python Create Environment OR
      -  Terminal
```bash
# create venv
python -m venv .venv

# activate venv/windows
.venv\Scripts\activate
```

- Install dependencies
```bash
pip install -r requirements.txt
```
>[!NOTE]
>Create requirments.txt
```bash
pip freeze > requirements.txt
```
>Install pytest
```bash
pip install pytest
```
----------------------
## Project Structure
```
example_code/
├── example.py
├── requirements.txt
├── test/
│   ├── __init__.py
│   └── test_example.py

```
## Create the structure and the tests

```python
# test/test_example.py

from example import add, subtract

def test_add():
    """Test addition function."""
    assert add(2, 3) == 5  # Test addition
    assert add(-1, 1) == 0  # Test with negative number
    assert add(0, 0) == 0  # Test with zeros

def test_subtract():
    """Test subtraction function."""
    assert subtract(5, 3) == 2  # Test subtraction
    assert subtract(0, 3) == -3  # Test with zero
    assert subtract(-1, -1) == 0  # Test with negatives
```
## When successful run pytest

```
Running pytest with args: ['-p', 'vscode_pytest', '--rootdir=d:\\example_code', 'd:\\example_code\\test\\test_example.py::test_add', 'd:\\example_code\\test\\test_example.py::test_subtract']
============================= test session starts =============================
platform win32 -- Python 3.12.6, pytest-8.3.4, pluggy-1.5.0
rootdir: d:\example_code
collected 2 items

test\test_example.py ..                                                  [100%]

============================== 2 passed in 0.01s ==============================
Finished running tests!
```
