# ## EUCLIDEAN DISTANCE PYTHON

import math

def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def minDistance(points):
    n = len(points)
    min_dist = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            dist = euclideanDistance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist

points = [(15, 18), (24, 59)]
distance = minDistance(points)
print("En kısa mesafe:", distance)





