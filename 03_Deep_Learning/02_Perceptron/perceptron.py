import numpy as np

class Perceptron(object):

    #we initialize the perceptron with a given rate, threshold and number of inputs
    def __init__(self, no_of_inputs, threshold=100, learning_rate=0.01):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs + 1)
        print("Initializing Threshold:", threshold)
        print("Initializing Learning Rate:", learning_rate)
        print("Initializing Weights:", np.zeros(no_of_inputs + 1))

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        if summation > 0:
          activation = 1
        else:
          activation = 0
        return activation

    def train(self, training_inputs, labels):
        print("")
        print("Beginning Training...", end='')
        for _ in range(self.threshold):
            for inputs, label in zip(training_inputs, labels):
                print('.', end='')
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)
        print("...\nTraining Complete!")
