#First Step, getting the data into an array:
import matplotlib.pyplot as plt
import numpy as np

def hardSVM(pts):
    #Splitting the points by categories. We know that there are only Two categories.
    cat1Pts = pts[np.where(pts[:, 2] == -1)][:, :2]
    cat2Pts = pts[np.where(Points[:, 2] == 1)][:, :2]

    #Step One, finding the margins
    # Because we know that there are only 2 points in the initial grouping that 
    # margin will simply be the line between them. We also know that the other point is solo
    # So we can use the slope from the previous grouping
    pass

    #Step Two:  Ge



Points = np.asarray([[1, 1, 1], [-1, 1, -1], [1, -1, -1]])



#Dividing by grouping
redpts = np.where(Points[:, 2] == -1)
bluepts = np.where(Points[:, 2] == 1)

plt.scatter(Points[bluepts][:, 0], Points[bluepts][:, 1], color='blue')
plt.scatter(Points[redpts][:, 0], Points[redpts][:, 1], color='red')
plt.show()