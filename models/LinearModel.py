import tensorflow as tf

class LinearModel():
	name = "LinearModel_V1"

	def __init__(self):
		self.input = tf.Variable(2)
		self.weight = tf.Variable(4)
		self.output = tf.multiply(self.input, self.weight)

		self.sess = tf.Session()
		self.sess.run(tf.global_variables_initializer())

	def train(self):
		self.sess.run(self.output, {self.input: x})

	def test(self, x):
		return self.sess.run(self.output, {self.input: x})