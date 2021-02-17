from numpy import exp, array, random, dot
from convert import numberify

class NeuralNetwork():

	count = 0

	def __init__(self):
		random.seed(1)
		count = 0
		with open("array_list.txt", "r") as array_list:
			for i in array_list:
				count += 1
			self.synaptic_weights = 2 * random.random((count, 1)) - 1

	def __sigmoid(self, x):
		return 1 / (1 + exp(-x))

	def __sigmoid_derivative(self, x):
		return x * (1 - x)

	def train(self, training_set_inputs, training_set_outputs, its):
		for it in range(its):
			output = self.think(training_set_inputs)
			error = training_set_outputs - output
			adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))
			self.synaptic_weights += adjustment

	def think(self, inputs):
		return self.__sigmoid(dot(inputs, self.synaptic_weights))

if __name__ == "__main__":
	neural_network = NeuralNetwork()
	print("Random starting synaptic weights: \n" + str(neural_network.synaptic_weights))
	
	url_to_check = input("URL to check: ")

	converted_examples, outputs, converted_url = numberify(url_to_check)

	#training_set_inputs = array([[1, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 1], [1, 0, 0, 0, 1], [0, 1, 0, 1, 0]])
	#training_set_outputs = array([[0, 1, 1, 1, 0]]).T
	training_set_inputs = array(converted_examples)
	training_set_outputs = array([outputs]).T
	print(training_set_outputs)
	neural_network.train(training_set_inputs, training_set_outputs, 10000)

	print("New synaptic weights: ")
	print(str(neural_network.synaptic_weights))

	print(str(neural_network.think(array(converted_url))))
	#print("Considering new situation [1, 0, 0] -> ?: " + str(neural_network.think(array([1, 0, 0])))
