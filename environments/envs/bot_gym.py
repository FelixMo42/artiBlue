import numpy as np
import gym
from gym import spaces
import pyglet

class BotGym(gym.Env):
	_seed =  42
	window = None

	def __init__(self):
		self.max_speed = 8
		self.max_torque = 1.

		self.action_num = 1
		self.observation_num = 4

		self.action_space = spaces.Box(low=-self.max_torque, high=self.max_torque, shape=(self.action_num, ), dtype=np.float32)
		self.observation_space = spaces.Box(low=-self.max_speed, high=self.max_speed, shape=(self.observation_num, ) , dtype=np.float32)

	def step(self, action):
		self.x += action[0]

		reward = self.x - self.target_x
		done = self.x > self.target_x

	 	return self.get_info(), reward, done, {}

	def reset(self):
		self.x = 10
		self.y = 10

		self.target_x = 110
		self.target_y = 10

		return self.get_info()

	def render(self, mode='human', close=False):
		if self.window is None:
			self.window = pyglet.window.Window(400,400)

	def get_info(self):
		return np.array([self.x, self.y, self.target_x, self.target_y])