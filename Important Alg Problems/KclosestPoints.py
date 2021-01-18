import math


def kClosest(points, K):
    distances = []
    for point in points:
        distances.append([point, math.sqrt((point[0] ** 2) + (point[1] ** 2))])

    distances = sorted(distances, key=lambda item:item[1])
    for i in range(K):
        distances[i] = distances[i][0]

    return distances[:K]


print(kClosest([[1,3], [-2,2]], 1))