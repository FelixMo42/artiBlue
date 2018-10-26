import tensorflow as tf
import matplotlib.pyplot as plt

class BasicModel():
	name = "BasicModel_V1"
	learning_rate = .001
	losses = []

	def __init__(self, shape):
		with tf.variable_scope(self.name):
			self.input = tf.placeholder(tf.float32, [None, shape[0]], name="input")
			layer = self.input
			for i in range(1,len(shape) - 1): 
				layer = tf.layers.dense(layer, units=shape[i], name="hidden_" + str(i))
			self.output = tf.layers.dense(layer, units=shape[-1], name="output")

			self.expected = tf.placeholder(tf.float32, [None, shape[-1]], name="expected")

			self.loss = tf.losses.mean_squared_error(self.expected, self.output)
			self.optimizer = tf.train.AdamOptimizer(self.learning_rate, epsilon=.001)
			#self.optimizer = tf.train.AdagradOptimizer(self.learning_rate)
			self.trainer = self.optimizer.minimize(self.loss)

			self.sess = tf.Session()
			self.sess.run(tf.global_variables_initializer())

	def train(self, data, expected):
		self.losses.append(self.sess.run([self.loss, self.trainer], {
			self.input: data,
			self.expected: expected
		})[0])

	def test(self, x):
		return self.sess.run(self.output, {self.input: [x]})

	def dump(self):
		plt.plot(self.losses)
		plt.ylabel('loss')
		plt.xlabel('epoch')
		plt.show()