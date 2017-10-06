import numpy as np
import matplotlib.pyplot as plt

# Computer x and y coordinates for points on a sine curve
x = np.arange(0, 4 * np.pi, 0.05)
y = np.sin(x)
z = np.sin(x**2)

#Plot the points using matplotlib
plt.plot(x, y)
plt.plot(x, z)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Sine and Sine Squared')
plt.legend(['Sine', 'Sine Squared'])
plt.show()

