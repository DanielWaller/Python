import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)

class NeuralNetwork:
    def __init__(self, x, y):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1],4)
        self.weights2 = np.random.rand(4,1)
        self.y = y
        self.output = np.zeros(y.shape)
        
    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))
    
    def backprop(self):
        # Need to apply chain rule to use gradient descent
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with loss function slope
        self.weights1 += d_weights1
        self.weights2 += d_weights2
        
# Example data
data_in = np.array([[0,0,1],
                  [0,1,1],
                  [1,0,1],
                  [1,1,1]])
data_class = np.array([[0],[1],[1],[0]])
data_class[1] = 1
data_class[2] = 1

NN1 = NeuralNetwork(data_in, data_class)

print(sigmoid_derivative(0.5))

for i in range(1500):
    NN1.feedforward()
    NN1.backprop()
    
print (NN1.output)
    

