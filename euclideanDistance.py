import math
def euclideanDistance(point1, point2):
    distance = ((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2)
    return math.sqrt(distance)

points = [(1,2), (8,9), (4,5), (10,7)]

distances = []

for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

print(min(distances))