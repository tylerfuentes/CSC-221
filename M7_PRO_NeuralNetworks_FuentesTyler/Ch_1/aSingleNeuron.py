# coding: utf-8
import numpy as np
import matplotlib as plt
inputs = [1, 2, 3]
weights = [0.2, 0.8, -0.5]
bias = 2
output = (inputs[0]*weights[0]+inputs[1]*weights[1]+inputs[2]*weights[2] + bias) #Visualizing the code that    makes up the math of a basic neuron. This action can be viewed at https://nnfs.io/bkr
print(output)
# Here we will be adding values to the weights and biases:
inputs = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2
# This action can be viewed at https://nnfs.io/djp
output = (inputs[0]*weights[0]+inputs[1]*weights[1]+inputs[2]*weights[2] + inputs[3]*weights[3] + bias) 
print(output)
# We are continuing to add to the neuron which can be visualized at https://nnfs.io/djp
# The next step of the tutorial can be viewed at https://nnfs.io/mxo
inputs = [1.0, 2.0, 3.0, 2.5]
weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5] 
weights3 = [-0.26, -0.27, 0.17, 0.87]
bias1 = 2
bias2 = 3
bias3 = 0.5
#As you can see, 2 weights and 2 biases have been added to the original sets in order to form two new neurons for a total now of 3. The output is going to be a list of 3 values instead of just one like our single neuron.
'''neuron 1'''output = [inputs[0]*weights1[0]+inputs[1]*weights1[1]+inputs[2]*weights1[2] + inputs[3]*weights1[3] + bias1,'''neuron 2''' inputs[0]*weights2[0]+inputs[1]*weights2[1]+inputs[2]*weights2[2] + inputs[3]*weights2
[3] + bias2, inputs[0]*weights3[0]+inputs[1]*weights3[1]+inputs[2]*weights3[2] + inputs[3]*weights3
[3] + bias3] 
outputs = [inputs[0]*weights1[0]+inputs[1]*weights1[1]+inputs[2]*weights1[2] + inputs[3]*weights1[3] + bias1, inputs[0]*weights2[0]+inputs[1]*weights2[1]+inputs[2]*weights2[2] + inputs[3]*weights2
[3] + bias2, inputs[0]*weights3[0]+inputs[1]*weights3[1]+inputs[2]*weights3[2] + inputs[3]*weights3
[3] + bias3] 
print(outputs)
#The visualization of this additon can be viewed at hhtps://nnfs.io/mxo
'''In this code there are 3 weights and 3 biases, making up 3 neurons. According to the authors of "Neural Networks from Scratch in Python" This is an example of a fully connected network, which means that every layer in the neural network is connected to every layer from the previous network. the next example will attempt to take this project 'to scale'.'''
inputs = [1.0, 2.0, 3.0, 2.5]
weights = [[0.2, 0.8, -0.5, 1], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]
layer_outputs = []
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    #For each input and weight in the neuron
    for n_input, weight in zip(inputs, neuron_weights):
        #Multiply this input by its associated weight and add to the neuron's output variable
        neuron_output += n_input*weight
        #Add the bias
        neuron_output += neuron_bias
        #Put the neuron's result to the layer's output list
        layer_outputs.append(neuron_output)
        
print(layer_outputs)
inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
for neuron_weights, neuron_bias in zip(weights, biases):
    #Zeroed output of given neuron
    neuron_output = 0
    #For each input and weight in the neuron
    for n_input, weight in zip(inputs, neuron_weights):
        #Multiply this input by its associated weight and add to the neuron's output variable
        neuron_output += n_input*weight
    #Add the bias
    neuron_output += neuron_bias
    #Put the neuron's result to the layer's output list
    layer_outputs.append(neuron_output)
    
        
print(layer_outputs)
inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]
layer_outputs = []
for neuron_weights, neuron_bias in zip(weights, biases):
    #Zeroed output of given neuron
    neuron_output = 0
    #For each input and weight in the neuron
    for n_input, weight in zip(inputs, neuron_weights):
        #Multiply this input by its associated weight and add to the neuron's output variable
        neuron_output += n_input*weight
    #Add the bias
    neuron_output += neuron_bias
    #Put the neuron's result to the layer's output list
    layer_outputs.append(neuron_output)
    
        
print(layer_outputs)
''' Here you can see a couple attempts to get this code written correctly. The print statement in line 39 was the result of taking shortcuts. On the first iteration,
    I forgot to properly indent the statements addition to bias and the append to the output list. While still receiving the same logic error, I found that on 
    the retry, I had forgotten to initialize the list layer_outputs as well as restatement of the biases. Correcting this resolved the issue. 
    This program was essentially the same as the first network written, only a practice of doing it to scale. The implementation of the '[zip]' commands
    allowed the calculations to be expected simultaneously, speeding up the execution process.'''
''' Here you can see a couple attempts to get this code written correctly. The print statement in line 39 was the result of taking shortcuts.
    On the first iteration, I forgot to properly indent the statements addition to bias and the append to the output list. 
    While still receiving the same logic error, I found that on the retry, I had forgotten to initialize the list layer_outputs as well as 
    restatement of the biases. Correcting this resolved the issue. 
    
    This program was essentially the same as the first network written, only a practice of doing it to scale. The implementation of the '[zip]' commands
    allowed the calculations to be expected simultaneously, speeding up the execution process.'''
# I will need to practice more on doc statements in iPython. Please address the input statement for clarity.
get_ipython().run_line_magic('save', 'aSingleNeuron 1-49')
