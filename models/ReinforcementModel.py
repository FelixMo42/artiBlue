import tensorflow as tf
import gym

class ReinforcementModel():
	name = "ReinforcementModel"

	def __init__(self, shape):
		self.input = tf.placeholder(tf.float32, [None, shape[0]], name="input")
		layer = self.input
		for i in range(1,len(shape) - 1): 
				layer = tf.layers.dense(layer, units=shape[i], name="hidden_" + str(i))
		self.output = tf.layers.dense(layer, units=shape[-1], name="output")

		self.sess = tf.Session()
		self.sess.run(tf.global_variables_initializer())

	def run(self,game):
		env = gym.make(game)
		env = env.unwrapped

		for episode in range(3):
			observation = env.reset()

			step = 0

			while True:
				env.render()

				action = self.sess.run(self.output,{self.input: [observation]})
				_observation, reward, done, info = env.step(action)
				observation = [_observation[0][0],_observation[1][0],_observation[2][0]]				

				step += 1

				if done or step > 200:
					break