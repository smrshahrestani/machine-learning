import numpy as np

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
  
# round 3 decimal points
round = 3 
    
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
number_of_iterations = 3

update_iteration(number_of_iterations,training_points,w0, w1,learning_rate)