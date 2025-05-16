import numpy as np
def f(x):
    return x**2 - np.log(x)
def f_prime(x):
    return 2 * x - (1 / x)
x0 = 1.5
tolerance = 1e-6
max_iterations = 1000
x_new = x0
for _ in range(max_iterations):
    x_old = x_new
    x_new = x_old - f(x_old) / f_prime(x_old)
    if abs(x_new - x_old) < tolerance:
        break
print(x_new)
