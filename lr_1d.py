import numpy as np
import matplotlib.pyplot as plot

# load the data
X = []
Y = []
for line in open("data_1d.csv"):
    x, y = line.split(",")
    X.append(float(x))
    Y.append(float(y))

# convert X and Y into numpy arrays
X = np.array(X)
Y = np.array(Y)

# plot to see what it looks like
plot.scatter(X, Y)
plot.show()

# apply the equations we learned to calculate a and b
denominator = X.dot(X) - X.mean()*X.sum()
a = ( X.dot(Y) - Y.mean()*X.sum() ) / denominator
b = ( Y.mean()*X.dot(X) - X.mean()*X.dot(Y) ) / denominator

Y_hat = a*X + b

# plot it
plot.scatter(X, Y)
plot.plot(X, Y_hat)
plot.show()

# calculate r-squared
d1 = Y - Y_hat
d2 = Y - Y.mean()

r2 = 1 - d1.dot(d1)/d2.dot(d2)

print "r-squared is: ", r2
