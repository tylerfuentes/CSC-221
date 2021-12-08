# coding: utf-8
# Chapter 3 ---- Adding Layers: Beginning this chapter, I will be simply providing the resources and code Animation links at the end of the file, for cleanliness and organization.
import numpy as np 
inputs= [[1, 2, 3, 2.5],
         [2., 5., -1., 2],
         [-1.5, 2.7, 3.3, -0.8]]
weights = [[0.2, 0.8, -0.5, 1],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]
weights2 = [[0.1, -0.14, 0.5],
            [-0.5, 0.12, -0.33],
            [-0.44, 0.73, -0.13]]
biases2 = [-1, 2, -0.5]
layered1_outputs = np.dot(inputs, np.array(weights).T) + biases
layered2_outputs = np.dot(layered1_outputs, np.array(weights2).T) + biases2
print(layered2_outputs)
# This section begins to delve into neurons containing hidden layers. These layers are accessible between endpoints and are not necessarily dealt with directly, hence the name "hidden."
# See figure 3.02
# Here we had to install a package called nnfs using the "pip install nnfs" method
from nnfs.datasets import spiral_data
# A great supplementary resource for this topic is the spiral data function, slightly modified from https://cs231n.github.io/neural-networks-case-study/
import numpyimport numpy as np
import numpy as np
import nnfs
# I did not need tgo import these libraries again but did so for clarity
nnfs.init()
# This function does 3 things 1) sets random seed to 0. 2) Creates a float32 dtype defaultand 3) overrides the original dot product from numpy. All of these are meant to measure repeatable results for the following sections.
import matplotlib.pyplot as plt
x, y = spiral_data(samples=100, classes=3)
X, y = spiral_data(samples=100, classes=3)
# A correction was made here to raise the x-value to an uppercase format
plt.scatter(X[:, 0], X[:, 1])
plt.show()
# We will add color to the scatter plot to determine all three classes separately. This will make things more clear.
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='brg')
plt.show()
# This coloration is made for the reader of the code but the neural network will not recognize the difference as there are no class encodings. Each dot is the feature, and its coordinates are samples that form the dataset. The "Classification" for that dot has to do with which sprial it is a part of. THese colors would then be assigned to a class model to fit to, like 0, 1, and 2.
# Dense Layer Class subsection
class Layer_Dense:
    
    #Layer initialization
    def__init__(self, n_inputs, n_neurons):
        # Initialize weights and biases
class Layer_Dense:
    
    #Layer initialization
    def__init__(self, n_inputs, n_neurons):
        # Initialize weights and biases
# I will be moving to create another file for this subsection. Hopefully this resolves any issues I am having
get_ipython().run_line_magic('save', 'addingLayers_TrainingData 1-36')
