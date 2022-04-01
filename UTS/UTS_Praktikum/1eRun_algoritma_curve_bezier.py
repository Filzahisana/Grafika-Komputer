from Bezier import Bezier
import numpy as np
from numpy import array as a
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#~~~#

fig = plt.figure(dpi=128)

t_points = np.arange(0, 1, 0.01)
test = a([[0, 5], [4, 10], [6, 10], [4, 0], [6, 0], [10, 5]])
test_set_1 = Bezier.Curve(t_points, test)

plt.subplot(2, 3, 6)
plt.xticks([i1 for i1 in range(-10, 10)]), plt.yticks([i1 for i1 in range(-10, 10)])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(b=True, which='major', axis='both')

plt.plot(test_set_1[:, 0], test_set_1[:, 1])
plt.plot(test[:, 0], test[:, 1], 'ro:')
#~~~#

plt.show()

help(Bezier)