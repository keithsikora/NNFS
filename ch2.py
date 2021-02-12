'''inputs = [1,2,3, 2.5]

weights1 = [ 0.2, 0.8, -0.5,1] #Neuron 1
weights2 = [0.5, -0.91, 0.26, -0.5] #Neuron 2
weights3= [-0.26, -0.27, 0.17, 0.87]  #Neuron 3

# Each of the inputs are multipled by each of the weights in each neuron


bias1 = 2
bias2 = 3
bias3 = 0.5

outputs = [
# Neuron 1:
inputs[0] * weights1[0] +
inputs[1] * weights1[1] +
inputs[2] * weights1[2] +
inputs[3] * weights1[3] + bias1,

# Neuron 2:
inputs[0] * weights2[0] +
inputs[1] * weights2[1] +
inputs[2] * weights2[2] +
inputs[3] * weights2[3] + bias2,

# Neuron 3:

inputs[0] * weights3[0] +
inputs[1] * weights3[1] +
inputs[2] * weights3[2] +
inputs[3] * weights3[3] + bias3,

]

print(outputs)'''

# Doing the same thing with loops

inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1],
[0.5, -0.91, 0.26, -0.5],
[-0.26, -0.27, 0.17, 0.87]]

bias = [2,3,0.5]

# output = sum(inputs * weights) + bias1

layer_output = []

for neuron_weights, neuron_bias in zip(weights, bias):
    neuron_output = 0
    for n_inputs, weights in zip(inputs, neuron_weights):
        neuron_output += n_inputs * weights
    neuron_output += neuron_bias
    layer_output.append(neuron_output)

print(layer_output)
