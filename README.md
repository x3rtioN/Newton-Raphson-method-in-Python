# Newton-Raphson Method in Python

This is a simple Python implementation of the **Newton-Raphson method** for finding roots of a nonlinear equation.  
The function used in this script is:

f(x) = eˣ + x² - 2.78

The root is approximated using Newton's iterative formula:

xₙ₊₁ = xₙ - f(xₙ) / f'(xₙ)

---

## 📌 Features

- Implements Newton's method using custom tolerance
- Tracks number of iterations until convergence
- Outputs the approximated root and total iterations

---

## 🔧 Requirements

- Python 3.x
- No external libraries required (only `math` module)

---

## ▶️ Usage

You can run the script directly:

```bash
python pythoncode.py
