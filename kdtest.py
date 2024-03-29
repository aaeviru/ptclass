import numpy as np
from scipy import spatial
x, y, z = np.mgrid[0:5, 2:8, 2:3]
data = zip(x.ravel(), y.ravel(), z.ravel())
tree = spatial.KDTree(data)
print 'ball', [data[i] for i in tree.query_ball_point(np.array([1,2,2]), 1)]
distance, index = tree.query(np.array([[2, 2, 2.2]]))
print 'query', distance, index, data[index[0]]
pts = np.array([[2, 2, 2.2]])

print tree.query(pts)


