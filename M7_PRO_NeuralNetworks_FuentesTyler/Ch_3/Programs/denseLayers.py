# coding: utf-8
# Dense Layer Class
class Layer_Dense:
    
    #Layer Initialization
    def __init__(self, n_inputs, n_neurons):
        # Initialize weights and biases
        pass # using pass statement as a placeholder
    
# Forward pass
def forward(self, inputs):
    # Calculate output values from inputs, weights and biases
    pass # using pass statement as a placeholder
    
def __init__(self, n_inputs, n_neurons):
    self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
    self.biases = np.zeroes((1, n_neurons))
    
def __init__(self, n_inputs, n_neurons):
    self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
    self.biases = np.zeros((1, n_neurons))
    
    
# Dead neurons: It is possible for weights * inputs + biases not to meet the threshold of the step function, which means the neuron will output a 0. This becomes a problem if multiple neurons begin to do this, given your data
# np.random.randn produces a Gaussian distribution with a mean of 0 and a variance of 1, which means it will generate numbers at random, centered at zero and with the mean value close to zero.
import numpy as np
import nnfs
nnfs.init()
print(np.random.randn(2, 5))
# 2 x 5 array
# Zeroize array
print(np,zeros((2, 5)))
print(np.zeros((2, 5)))
import numpy as np
import nnfs
nnfs.init()
n_inputs = 2
n_neurons = 4
print(np.random.randn(n_inputs, n_neurons))
weights = 0.01 * np.random.randn(n_inputs, n_neurons)
biases = np.zeros((1, n_neurons))
print(weights)
print(biases)
# Update Forward method
def forward(self, inputs):
    self.output = np.dot(inputs, self.weights) + self.biases
    
def __init__(self, n_inputs, n_neurons):
    self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
    self.biases = np.zeros((1, n_neurons))
    
# Forward pass
def forward(self, inputs):
    self.output = np.dot(inputs, self.weights) + self.biases
    
# Create Dataset
X, y = spiral_data(samples=100, classes=3)
import numpy as np
import nnfs
from nnfs.datasets import spiral_data
nnfs.init()
class Layer_Dense:
    
    # Layer Initialization
    def __init__(self, n_inputs, n_neurons):
        #Initialize weights and biases
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        # Calculate output values from inputs, weights, and biases
        self.output = np.dot(inputs, self.weights) + self.biases
        
# Create dataset
X, y = spiral_data(samples=100, classes=3)
dense1 = Layer_Dense(2, 3)
dense1.forward(X)
# The statement above preforms a forward pass of our training data through that layer
# Let's see the output of the first few samples
print(dense1.output[:5])
# Supplementary material for this chapter can be found at the following website: https://nnfs.io/ch3 : chapter code, further resources, and eratta for this chapter.
get_ipython().run_line_magic('save', 'denseLayers 1-47')
