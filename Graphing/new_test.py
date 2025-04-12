import numpy as np
import matplotlib.pyplot as plt

var = 3

x = np.linspace(-var, var, 100)

y_pos = np.sqrt(var**2 - x**2)
y_neg = -np.sqrt(var**2 - x**2)

plt.figure(figsize=(6, 6))
plt.plot(x, y_pos, color='green')
plt.plot(x, y_neg, color='green')

plt.axvline(x=0, color='black', label='Vertical Axis')  # Add label
plt.axhline(y=0, color='black', label='Horizontal Axis')  # Add label

plt.title('Circle')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()
plt.grid(True)
plt.show()
