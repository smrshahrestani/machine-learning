

#  hello

from dis import dis
from re import L
from joblib import PrintTime
import numpy as np
from regex import R, W

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
    entropy = np.round(entropy, round)
    return entropy

def hw(w0, w1, x):
    final = w0 + w1*x
    return final

def error(x,y,w0,w1):
    return y - hw(w0, w1 ,x)

def sumError(training_points, w0, w1):
    sum = 0
    for i in training_points:
        sum += error(i[0], i[1], w0, w1)
    return sum

def sumError2(training_points, w0, w1):
    sum = 0
    for i in training_points:
        sum += error(i[0], i[1], w0, w1) * i[0]
    return sum

def updateW0(training_points, w0 , w1, learning_rate):
    final = w0 + learning_rate * sumError(training_points, w0, w1)
    final = np.round(final,round)
    return final

def updateW1(training_points, w0, w1, learning_rate):
    final = w1 + learning_rate * sumError2(training_points, w0, w1)
    final = np.round(final,round)
    return final

def update_iteration(number_of_iterations, training_points, w0, w1, learning_rate):
    w0_new = 0
    w1_new = 0
    for i in range(number_of_iterations):
        w0_new = updateW0(training_points, w0, w1, learning_rate)
        w1_new =updateW1(training_points, w0, w1, learning_rate)

        print(f"iteration {i+1}: w0 = {w0_new}")
        print(f"iteration {i+1}: w1 = {w1_new}")
        print("--------------------------------")
        w0 = w0_new
        w1 = w1_new


    return w0_new, w1_new


training_points = [
    (1.5, 1),
    (3.5, 3),
    (3,2),
    (5,3),
    (2,2.5),
]

w0 = 0
w1 = 0
learning_rate = 0.01

# manhatDist(array, point)
# print("-----------------------------")
# euclidDist(array, point)

# euclidDist([
#     [(1,2)],
#     [(2,1)],
#     [(3,2)],
#     [(4,2)],
# ],
#     (1,1)
# )

# print(entropy(0.3))

update_iteration(3,training_points,w0, w1,learning_rate)
