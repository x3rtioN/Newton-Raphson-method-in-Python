import math

def newtons_method(x0, tol=1e-3):
    def f(x):
        return math.exp(x) + x**2 - 2.78
    
    def f_prime(x):
        return math.exp(x) + 2*x
    
    x_n = x0
    iteration = 0
    
    while True:
        x_next = x_n - f(x_n) / f_prime(x_n)
        if abs(x_next - x_n) < tol:
            break
        x_n = x_next
        iteration += 1
    
    return x_next, iteration

initial_guess = 0.5
solution, iterations = newtons_method(initial_guess)
print(f"Root: {solution:.6f}, Iterations: {iterations}")
