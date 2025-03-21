# Core Python Interview Questions

<br>

## 1.  Differences between Conda and Pip?
- **Conda** is a system package manager. **pip** is a Python package manager.
- Conda installs binary packages, which means the packages include compiled code. This can make the installation process faster and more reliable, especially for packages with complex dependencies. Pip, by contrast, often installs packages from the source, which means the code is compiled during the installation process.

## 2. What is PEP 8?
- PEP 8 is a coding convention, a set of recommendation, about how to write your Python code more readable.

## 3. What is the timer method in Python?
- Timer is a method available with Threading, and it helps to get the same functionality as Python time sleep.

```python 
from threading import Timer

print('Code Execution Started')

def display():
    print('Execute display function')

t = Timer(5, display)  
t.start()
```

## 4. What is Method overloading and overriding in Python?
- ### [ Method overloading and overridden](https://www.pickl.ai/blog/method-overriding-method-overloading-in-python/#:~:text=Note%20that%20method%20overloading%20is,previous%20ones%20will%20be%20overridden).


## 5. **Docstrings in Python**
- Docstrings are accessible from the doc attribute **`(__doc__)`**



