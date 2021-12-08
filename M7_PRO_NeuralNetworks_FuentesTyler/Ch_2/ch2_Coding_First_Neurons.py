# coding: utf-8
a = [1, 2, 3]
b =[2, 3, 4]
dot_product = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
print(dot_product)
# The above is a clean segway into the dot product and vector addition module
# The animation illustrating this math can be found at https://nnfs.io/xpo
# A single neuron implemented with numpy
import numpy as np
inputs = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2.0
outputs = np.dot(weights, inputs) + bias
print(outputs)
# https://nnfs.io/blq
#Below: A layer of neurons with numpy
# Before, this was executed with lists. Using numpy, we will be using matrices, or two-dimensional arrays
inputs = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0],
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]] 
biases = [2.0, 3.0, 0.5]
layer_outputs = np.dot(weights, inputs) + biases
print(layer_outputs)
# Now the same information we utilized before in list format has been presented as an array
# Arrays are more versatile for use in programming, data collection, and mathematics and used to scale
# Anim 2.09-2.10: hhtps://nnfs.io/cyx
# Our goals with these functions is to pass a list of neuron weights. As you can see, this we will continue 
# to expand upon the (inputs * weights) + bias equation to get a list of neuron outputs
'''The numbers we have used so far for the inputs, [1, 2, 3, 2.5], has been an example to represent a sample  of observations called a feature set'''
# Animation 2.11: https://nnfs.io/lqw
# Animation 2.12: hhtps://nnfs.io/vyu
# Animation 2.13: https://nnfs.io/lqw
# Over the next few pages these animations will be posted to track the path of information provided by this textbook
# Matrix Product
# An operation in which we have 2 matrices, and we are performing dot producs of all combinations of rows from the first matrix and columns of the second matrix of those atomic dot products
# Animation 2.14 https://nnfs.io/jei
# Above illustrates the full calulation of each event in the resulting Matrix Product
a = [1 2 3]
# a = [1 2 3] <---row vector
# b = [2
#      3
#      4] <---Column vector
# For better clarity, refer to Animation 2.15: https://nnfs.io/bkw
# Transposition of the matrix product
# TRansposition modifies the product to where the rows become columns and the columns become rows
# https://nnfs.io/qut
# Animation 2.17 https://nnfs.io/pnq
np.array([[1, 2, 3]])
a = [1, 2, 3]
print(np.array([a]))
# Note we encased the variable a in brackets before converting to an array in this case. Next we'll use numpy
print(np.expand_dims(np.array(a), axis=0))
# np.expands_dims adds a new dimension at the index of the axis. The array shape is technically now (n, 1) or now two dimensional
# We will be turning vector b into row vector b using numpy
# The same will be done with vector a using numpy
a = [1, 2, 3]
b = [2, 3, 4]
a = np.array([a])
b = np.array([b]).T
# The "T" denotes the transposition to make column vector b
print(np.dot(a, b))
# We have achieved the same result as the dot product of two vectors, but performed on matrices and returning a matrix
# A Layer of Neurons & Batch Data w/ Numpy
# Animation 2.18-2.19: https://nnfs.io/crq
# Animation 2.20: https://nnfs.io/gjw
import numpy as np
inputs = [[1.0, 2.0, 3.0, 2.5],
           2.0, 5.0, -1.0, 2.0],
inputs = [[1.0, 2.0, 3.0, 2.5],
           [2.0, 5.0, -1.0, 2.0],
           [-1.5, 2.7, 3.3, -0.8]]
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
biases = [2.0, 3.0, 0.5]
layered_outputs = np.dot(inputs, np.array(weights).T) + biases
print(layered_outputs)
# As you can see, our neural network takes in a group of samples (inputs) and outputs a group of predictions. If you've used any on the deep learning libraries, this is why you pas in a list of inputs (even if it's just one feature set) and are returnes a list of predictions, even if there's only one prediction.
# Supplementary Material: https://nnfs.io/ch2 <---Chapter code, resources, and erattafor this chapter
get_ipython().run_line_magic('save','ch2_Coding_First_Neurons 1-74')
