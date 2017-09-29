import pandas
import numpy

# Read the data
data = pandas.read_csv('data.csv')

# Split the data into X and y
X = numpy.array(data[['x1', 'x2']])
y = numpy.array(data['y'])

# Import the SVM Classifier
from sklearn.svm import SVC

# TODO: Define your classifier.
# Play with different values for these, from the options above.
# Hit 'Test Run' to see how the classifier fit your data.
# Once you can correctly classify all the points, hit 'Submit'.
classifier = SVC(kernel = "rbf", degree = 3, gamma = 200, C = 1.0)

# Fit the classifier
classifier.fit(X,y)
