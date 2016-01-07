import random as rand

class NeuralNetwork:
    hidden = []
    output = []

    def __init__(self, inputSize, hiddenSize, outputSize):
        self.inputSize = inputSize
        self.hiddenSize = hiddenSize
        self.outputSize = outputSize
        for i in range(0, hiddenSize):
            randomList = []
            for j in range(0, inputSize):
                randomList += [rand.random()];
            self.hidden += [randomList]


neural = NeuralNetwork(12, 3, 4)
print(neural.hidden)