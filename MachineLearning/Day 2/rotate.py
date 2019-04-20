import math
import matplotlib.pyplot as plt

def rotate(x,y, a):
	a = math.radians(a)
	a_p = math.asin(y)
	#print(math.degrees(a_p))

	m = math.hypot(x,y)
	x_r = m*math.cos(a + a_p)
	y_r = m*math.sin(a + a_p)

	return x_r, y_r


points = []
for i in range(0,360, 45):
	points.append(rotate(1,0, i))


plt.scatter([p[0] for p in points], [p[1] for p in points])
plt.show()
