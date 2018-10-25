import tensorflow as tf

class LinearModel():
	name = "LinearModel_V1"
	learning_rate = .01

	def __init__(self):
		with tf.variable_scope(self.name):
			self.input = tf.placeholder(tf.float32, (None), name="input")
			self.weight = tf.Variable(4.0, name="weight")
			self.output = tf.multiply(self.input, self.weight, name="output")

			self.expected = tf.placeholder(tf.float32, (None), name="expected")

			self.loss = tf.squared_difference(self.expected, self.output)
			self.optimizer = tf.train.AdagradOptimizer(self.learning_rate)
			self.trainer = self.optimizer.minimize(self.loss)

			self.sess = tf.Session()
			self.sess.run(tf.global_variables_initializer())

	def train(self):
		for i in range(2000):
			self.sess.run(self.trainer, {
				self.input: [i],
				self.expected: [i * 3]
			})

	def test(self, x):
		return self.sess.run(self.output, {self.input: [x]})