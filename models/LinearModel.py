import tensorflow as tf

class LinearModel():
	name = "LinearModel_V1"
	learning_rate = .1

	def __init__(self):
		with tf.variable_scope(self.name):
			self.input = tf.placeholder(tf.float32, (None), name="input")
			self.weight = tf.Variable(1.0, name="weight")
			self.bias = tf.Variable(2.0, name="bias")

			o1 = tf.multiply(self.input, self.weight, name="output_1")
			self.output = tf.add(o1, self.bias, name="output")

			self.expected = tf.placeholder(tf.float32, (None), name="expected")

			self.loss = tf.squared_difference(self.expected, self.output)
			self.optimizer = tf.train.AdamOptimizer(self.learning_rate, epsilon=.01)
			self.trainer = self.optimizer.minimize(self.loss)

			self.sess = tf.Session()
			self.sess.run(tf.global_variables_initializer())

	def train(self, data, expected):
		print(self.sess.run(self.trainer, {
			self.input: data,
			self.expected: expected
		}))

	def test(self, x):
		return self.sess.run(self.output, {self.input: [x]})