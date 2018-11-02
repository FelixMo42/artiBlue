import numpy as np
import gym
from gym import spaces
import random

class BotGym(gym.Env):
	_seed =  42
	viewer = None

	def __init__(self):
		self.max_observation = 2
		self.max_action = 2.

		self.action_num = 2
		self.observation_num = 2

		self.action_space = spaces.Box(low=-self.max_action, high=self.max_action, shape=(self.action_num, ), dtype=np.float32)
		self.observation_space = spaces.Box(low=-self.max_observation, high=self.max_observation, shape=(self.observation_num, ) , dtype=np.float32)

	def step(self, action):
		self.x += action[0]
		#self.y += action[1]

		distX = abs(self.x - self.target_x)
		distY = abs(self.y - self.target_y)

		done = distX < 10 and distY < 10
		if done:
			reward = 50
		else:
			reward = -(distX ** 2 + distY ** 2) / 10000

		return self.get_info(), reward, done, {}

	def reset(self):
		self.x = 10#random.randint(10,490)
		self.y = 250#random.randint(10,490)

		self.target_x = 250
		self.target_y = 250

		return self.get_info()

	def render(self, mode='human', close=False):
		if self.viewer is None:
			from gym.envs.classic_control import rendering
			
			self.viewer = rendering.Viewer(500,500)
			
			target = rendering.make_circle(10)
			self.target_transform = rendering.Transform()
			target.add_attr(self.target_transform)
			target.set_color(0,255,0)
			self.viewer.add_geom(target)

			bot = rendering.make_circle(10)
			self.bot_transform = rendering.Transform()
			bot.add_attr(self.bot_transform)
			bot.set_color(0,0,255)
			self.viewer.add_geom(bot)

		self.target_transform.set_translation(self.target_x, self.target_y)
		self.bot_transform.set_translation(self.x, self.y)

		return self.viewer.render(return_rgb_array = mode=='rgb_array')

	def get_info(self):
		return np.array([(self.target_x - self.x) / (25 * 5), (self.target_y - self.y) / (25 * 5)])