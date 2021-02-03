from statistics import mean
import math

# y pred is defined by the line: y = 1.2x +2, always positive value
def get_pred(x,y):
    y_pred = 1.2 * x + 2
    dist = abs(y - y_pred)
    return dist

x_true = [2, 5, -4, -7, 8] #x points
y_true = [-2, 6, -4, 1, 14] #y points
y_pred = []
y_sqr = []

for i in range(len(x_true)):
    y_pred.append(get_pred(x_true[i], y_true[i]))

print('Y_PRED:')
print(y_pred)

for i in range(len(y_pred)):
    y_sqr.append(y_pred[i] ** 2)

print('Y_PRED SQUARE:')
print(y_sqr)

# Mean absolute error is the sum of the values of y_pred divided
# by the total of numbers (mean)
MAE_ERROR = mean(y_pred)

# Mean square error is the sum of the values of y_pred^2 divided
# by the total of numbers * 2 (mean / 2)
MSE_ERROR = mean(y_sqr) / 2

print('Error value using Mean Absolute Error:')
print(MAE_ERROR)

print('Error value using Mean Square Error:')
print(MSE_ERROR)
