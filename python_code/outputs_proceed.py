import numpy as np
import matplotlib.pyplot as plt

# Define the range for x
x = np.linspace(-5, 5, 100)

# Define the function (x + a)^+
def positive_part(x, a):
    return np.maximum(x + a, 0)

# Values of a to plot
a_values = [-2, 0, 2]
colors = ['blue', 'green', 'red']
labels = [f'a = {a}' for a in a_values]

# Create the plot
plt.figure(figsize=(8, 6))
for a, color, label in zip(a_values, colors, labels):
    y = positive_part(x, a)
    plt.plot(x, y, label=label, color=color)

# Add labels and title
plt.xlabel('x')
plt.ylabel('(x + a)^+')
plt.title('Plot of (x + a)^+ for Different Values of a')
plt.grid(True)
plt.legend()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Show the plot
plt.show()