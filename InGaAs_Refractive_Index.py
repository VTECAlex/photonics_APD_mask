import numpy as np
import matplotlib.pyplot as plt

# Given empirical coefficients
A = 8.950
B = 2.054
C = 0.6245
Eggas = 1.424  # eV fundamental band gap of GaAs at room temperature (300K)

# Fraction of In in In_xGa_1-xAs alloy
x_values = [0.1, 0.3, 0.5, 0.7, 0.9]

# Wavelength range (in nanometers)
l = np.linspace(1, 2000, 2000)  # avoid division by zero by starting from 1 nm

plt.figure(figsize=(10, 6))

# Loop over each value of x and calculate the refractive index n
for x in x_values:
    Egx = Eggas - x * 1.501 + (x ** 2) * 0.436
    n = np.sqrt(A + B / (1 - (C * Eggas / (l * Egx)) ** 2))
    plt.plot(l, n, label=f'x = {x}')

# Plotting
plt.xlabel('Wavelength (nm)')
plt.ylabel('Refractive Index n')
plt.title('Refractive Index vs Wavelength for different x values')
plt.legend()
plt.grid(True)
plt.show()