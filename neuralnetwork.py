import random as rand
import math

class NeuralNetwork:
    hidden = []
    output = []

    inputSize = 0
    hiddenSize = 0
    outputSize = 0

    def __init__(self, inputSize, hiddenSize, outputSize):
        self.inputSize = inputSize
        self.hiddenSize = hiddenSize
        self.outputSize = outputSize
        for i in range(0, hiddenSize):
            randomList = []
            for j in range(0, inputSize+1): # +1 for bias
                randomList += [rand.random()]
            self.hidden += [randomList]

        for i in range(0, outputSize):
            randomList = []
            for j in range(0, hiddenSize+1): # +1 for bias
                randomList += [rand.random()]
            self.output += [randomList]

    def train(self, input, outputTarget):
        self

    def run(self, input):
        result = []
        inputWithBias = input + [1]
        for o in range(0, self.outputSize):
            hiddenSum = 0
            for h in range(0, self.hiddenSize):
                inputSum = 0
                for i in range(0, self.inputSize+1): # bias
                    inputSum += inputWithBias[i] * self.hidden[h][i]
                hiddenSum += activate(inputSum) * self.output[o][h]
            hiddenSum += self.output[o][self.hiddenSize] # bias
            result += [activate(hiddenSum)]
        return result

def activate(x):
    return 1.0/(1.0+math.exp(-x))

neural = NeuralNetwork(2, 3, 4)
print(neural.run([0.5, 0.2]))
print(neural.hidden)