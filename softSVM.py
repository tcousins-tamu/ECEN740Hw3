import matplotlib.pyplot as plt
import numpy as np


def graph(formula):
    x = np.array(range(-2, 2))
    y = formula(x)
    return y


def formula(x):
    return
# This is used to visualize the results from the had and soft SVM results.
# NO calculations are done in here, all calculations are done on paper and brought here


Points = np.asarray([[1, 1], [-1, 1], [1, -1]])
Groups = np.asarray([1, -1, -1])


# Dividing by grouping
redpts = Groups == 1
bluepts = Groups == -1

C = .5
# Figuring out how to plot the hyperplane..
# containing our results from hand calculations earlier
# alpha = np.asarray([1, .5, .5])
alpha = np.asarray([.5, .25, .25])
# alpha = np.asarray([.25, .125, .125])

#alpha = np.asarray([1, .25, .75])
# Recalculating
#alpha[alpha>C] = C

w = np.asarray([0, 0])
for idx, i in enumerate(Points):
    w = w + (i*alpha[idx]*Groups[idx])

# b = (1-2*C)
# #b = 1-2*C
vec = []
for idx1, j in enumerate(Points):
    sm = 0
    for idx2, i in enumerate(Points):
        sm = sm+alpha[idx2]*Groups[idx2]*np.dot(Points[idx2], Points[idx1])
    vec.append(Groups[idx1]-sm)

# making sure b is not from an alpha equivalent to C
for idx, i in enumerate(vec):
    if alpha[idx] < C:
        b = i
        break


print("########## w matrix ###########")
print(w)
print("########## b vector ###########")
print(b)

# deriving the new equation:
# Support Vector 1
x1 = np.arange(-2, 2, .5)
y1 = -(w[0]*x1+b-Groups[0])/w[1]

# Support Vector 2
x2 = np.arange(-2, 2, .5)
y2 = -(w[0]*x2+b-Groups[1])/w[1]

# Hyperplane fopr HARD SVM:
x3 = (x1+x2)/2
y3 = (y1+y2)/2

# Round One C=.5:
# [ 2.   1.5  1.   0.5  0.  -0.5 -1.  -1.5]
# Round 2:
# [ 0.  -0.5 -1.  -1.5 -2.  -2.5 -3.  -3.5]

plt.scatter(Points[bluepts][:, 0], Points[bluepts][:, 1], color='blue')
plt.scatter(Points[redpts][:, 0], Points[redpts][:, 1], color='red')
plt.plot(x1, y1, color="green")
plt.plot(x2, y2, color="green")
plt.plot(x3, y3, color="purple")
plt.grid()
plt.show()
