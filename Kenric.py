import numpy as np
import matplotlib.pyplot as plt


# Seed for reproducibility
np.random.seed(0)

# Generate random coefficients a, b, and c for the parabola y = ax^2 + bx + c
a = np.random.rand() * 10 - 5  # Random value between -5 and 5
b = np.random.rand() * 10 - 5  # Random value between -5 and 5
c = np.random.rand() * 10 - 5  # Random value between -5 and 5

# Define the parabolic function
def parabola(x, a, b, c):
    return a * x ** 2 + b * x + c

# Choose three different x values
x_values = np.array([-2, 0, 2])

# Calculate the corresponding y values
y_values = parabola(x_values, a, b, c)

# Print the parabolic function and the three points
print(f"Parabolic function: y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}")
print(f"Three points on the parabola: {list(zip(x_values, y_values))}")

# Calculate the best-fit line using numpy's polyfit with degree 1 (Linear)
coefficients = np.polyfit(x_values, y_values, 1)

# Calculate the best-fit parabola using numpy's polyfit with degree 2 (Parabolic)
coefficients = np.polyfit(x_values, y_values, 2)

# Extracting a, b, and c of the best-fit parabola: y = ax^2 + bx + c
a, b, c = coefficients

# Print the parabolic function
print(f"Parabolic Function: y = {a}x^2 + {b}x + {c}")

# Plotting the points and the parabola
plt.scatter(x_values, y_values, color='red', label='Data Points')
x_line = np.linspace(min(x_values)-1, max(x_values)+1, 400)
plt.plot(x_line, a * x_line ** 2 + b * x_line + c, label=f'Best-fit Parabola: y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}')
plt.legend()
plt.show()