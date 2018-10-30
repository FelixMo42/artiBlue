import numpy as np
import gym
from gym import spaces
import random

class BotGym(gym.Env):
	_seed =  42
	viewer = None

	def __init__(self):
		self.max_speed = 8
		self.max_torque = 1.

		self.action_num = 1
		self.observation_num = 4

		self.action_space = spaces.Box(low=-self.max_torque, high=self.max_torque, shape=(self.action_num, ), dtype=np.float32)
		self.observation_space = spaces.Box(low=-self.max_speed, high=self.max_speed, shape=(self.observation_num, ) , dtype=np.float32)

	def step(self, action):
		self.x += action[0]

		dist = abs(self.x - self.target_x)
		reward = -dist
		done = dist < 10

	 	return self.get_info(), reward, done, {}

	def reset(self):
		self.x = random.randint(10,490)
		self.y = 50

		self.target_x = 250
		self.target_y = 50

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
		return np.array([self.x, self.target_x])