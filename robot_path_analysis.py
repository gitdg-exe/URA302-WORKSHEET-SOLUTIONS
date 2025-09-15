import numpy as np

data = np.genfromtxt("robot_path.csv", delimiter=",", skip_header=1)
x = data[:,0]
y = data[:,1]

dist = np.sqrt(np.diff(x)**2 + np.diff(y)**2).sum()
print("Total distance traveled:", dist)

d_from_origin = np.sqrt(x**2 + y**2)
i = np.argmax(d_from_origin)
print("Farthest point:", x[i], y[i], "distance =", d_from_origin[i])

pts = list(zip(x, y))
revisited = len(pts) != len(set(pts))
print("Robot revisited a position:", revisited)
