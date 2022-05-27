

#  hello

from dis import dis
from re import L
import numpy as np

# round 3 decimal points
round = 3 

# number of clusters
k = 3

# [(x,y), class]
array = [
    [(12,12), 1],
    [(2,2), 1],
    [(1,3), 1],
    [(4,2), 1],
    [(1,6), 2],
    [(2,4), 2],
    [(2,5), 2],
    [(3,4), 2],
    [(5,4), 2],
]

point = (3,1)



def assignClassToPoints(array):
    dict = {}
    list = []
    # for val in array:
    #     if list.index(val[1] - 1) == -1:

    #     list[val[1] - 1] = val[0]

    return list


# The Manhattan Distance between set of points to a single point
def manhatDist(array, point):
    allDist = []
    print(assignClassToPoints(array))
    for i, val in enumerate(array):
        val = val[0]
        distance = abs(val[0] - point[0]) + abs(val[1] - point[1])
        distance = np.round(distance, round)

        allDist.append(distance)

        print(f"{i}. The Manhattan distance between point {val} and point {point} is: {distance}")



# The Euclidean Distance between set of points to a single point
def euclidDist(array, point):
    for i, val in enumerate(array):
        val = val[0]
        distance = np.power(val[0] - point[0], 2) + np.power(val[1] - point[1], 2)
        distance = np.sqrt(distance)
        distance = np.round(distance, round)
        print(f"{i}. The Euclidean distance between point {val} and point {point} is: {distance}")



def entropy(q):
    entropy = -(q * np.log2(q) + (1-q) * np.log2(1-q))
    return entropy













# manhatDist(array, point)
# print("-----------------------------")
# euclidDist(array, point)

euclidDist([
    [(1,2)],
    [(2,1)],
    [(3,2)],
    [(4,2)],
],
    (1,1)
)