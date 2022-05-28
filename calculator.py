# @author: Seyed Mohammad Reza Shahrestani
# @Date: 27/05/2022

import numpy as np
from regex import P

# The Manhattan Distance between set of points to a single point
def manhatDist(array, point, print_time=False):
    list = []
    if print_time: 
        print("----Manhattan Distance----")
    for i, val in enumerate(array):
        if isinstance(val, type(list)):
            val = val[0]
        distance = abs(val[0] - point[0]) + abs(val[1] - point[1])
        distance = np.round(distance, round)
        list.append(distance)
        if print_time: 
            print(f"{i}. The Manhattan distance between point {val} and point {point} is: {distance}")
    
    if print_time: 
        print("================================")
    return(list)

# The Euclidean Distance between set of points to a single point
def euclidDist(array, point, print_time=False):
    list = []
    if print_time:
        print("----Euclidean Distance----")
    for i, val in enumerate(array):
        if isinstance(val, type(list)):
            val = val[0]
        distance = np.power(val[0] - point[0], 2) + np.power(val[1] - point[1], 2)
        distance = np.sqrt(distance)
        distance = np.round(distance, round)
        list.append(distance)
        if print_time:
            print(f"{i}. The Euclidean distance between point {val} and point {point} is: {distance}")
    if print_time:
        print("================================")
    return list

# The Manhattan Distance between 2 set of points
def man_distance(array, points, print_time=True):
    if print_time: 
        print("----Manhattan Distance----")
    manhattan_list = []
    count = 0
    for i, point in enumerate(points):
        manhattan_list.append(manhatDist(array, point))

    for i, man in enumerate(manhattan_list):
        for j, x in enumerate(man):
            count += 1
            if print_time:
                if isinstance(array[i], type(manhattan_list)):
                    point_x = array[j][0]
                else: point_x = array[j]
                print(f"{count}. The Manhattan distance between point {point_x} and point {points[i]} is: {x}")
    if print_time:
        print("================================")

# The Euclidean Distance between 2 set of points
def euc_distance(array, points, print_time=True):
    if print_time:
        print("----Euclidean Distance----")
    euclidean_list = []
    count = 0
    for i, point in enumerate(points):
        euclidean_list.append(euclidDist(array, point))

    for i, man in enumerate(euclidean_list):
        for j, x in enumerate(man):
            count += 1
            if print_time:
                if isinstance(array[i], type(euclidean_list)):
                    point_x = array[j][0]
                else: point_x = array[j]
                print(f"{count}. The Euclidean distance between point {point_x} and point {points[i]} is: {x}")
    if print_time:
        print("================================")

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
    print("----Batch Gradient Descend----")
    w0_new = 0
    w1_new = 0
    for i in range(number_of_iterations):
        w0_new = updateW0(training_points, w0, w1, learning_rate)
        w1_new =updateW1(training_points, w0, w1, learning_rate)

        print("--------------------------------")
        print(f"iteration {i+1}: w0 = {w0_new}")
        print(f"iteration {i+1}: w1 = {w1_new}")
        w0 = w0_new
        w1 = w1_new
    print("================================")
    return w0_new, w1_new

vector1 = [1,2,3]
vector2 = [4,5,6]
vector = [vector1, vector2]

# input: [[1,2,3,...], [4,5,6,...], ...]
def dot_product(vector, print_time= True):
    if print_time:
        print("----Dot Product----")
    dot_product = []
    for j in range(len(vector[0])):
        col = []
        for i in range(len(vector)):
            col.append(vector[i][j])
        prod_col = np.prod(col)
        dot_product.append(prod_col)
    sum_dot_product = np.sum(dot_product)
    
    if print_time:
        print(f"input vector: {vector}, => dot product = {sum_dot_product}")
        print("================================")
    return sum_dot_product

    
dot_product(vector)
dot_product([[1,2,3],[4,2,3]])

# print settings
# 

# round 3 decimal points
round = 3 


# batch gradient descend
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
number_of_iterations = 2
update_iteration(number_of_iterations,training_points,w0, w1,learning_rate)


# Distances from a set of points to a single point
# KNN - not ready
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

# manhatDist(array, point, True)

# euclidDist(array, point, True)

# euclidDist([
#     [(1,2)],
#     [(2,1)],
#     [(3,2)],
#     [(4,2)],
# ],
#     (1,1)
# ,True)


# Calculate entropy
# print(entropy(0.3))
    

# man_distance(array, [(2,1), (2,3),(12,32),(1,3)])
# euc_distance(array, training_points)
# manhatDist(array, (2,3), True)


new = [
    (5,8),
    (6,7),
    (6,4),
    (5,7),
    (5, 5),
    (6, 5),
    (1, 7),
    (7, 5),
    (6, 5),
    (6, 7),
]

man_distance(new,[(7, 5), (9, 7) , (9, 1)])
# euc_distance(new, training_points)


