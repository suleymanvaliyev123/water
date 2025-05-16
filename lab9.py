import numpy as np
x_values = np.linspace(1.0, 2.0, 1000)
solutions = []
for x_val in x_values:
    if np.isclose(x_val**2 - np.log(x_val), 0, atol=1e-6):
        solutions.append(x_val)
print(solutions)
