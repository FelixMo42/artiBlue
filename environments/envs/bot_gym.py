import numpy as np
import gym
from gym import spaces
import random
import matplotlib.pyplot as plt
import numpy as np

GRAPHING = True

if GRAPHING:
	plt.ion()
	fig = plt.figure()
	data = []
	data10 = []

	def update(d):
		global data10

		data.append(d)
	
		if len(data) % 10 == 0:
			data10.append(sum(data[-10:]) / 10.0)

		fig.clf()
		plt.plot(np.arange(len(data10)) * 10, data10)

		data10 = data10[-100:]

class BotGym(gym.Env):
	_seed =  42
	viewer = None

	def __init__(self):
		self.max = 1

		self.action_num = 2
		self.observation_num = 2

		self.action_space = spaces.Box(low=-self.max, high=self.max, shape=(self.action_num, ), dtype=np.float32)
		self.observation_space = spaces.Box(low=-self.max, high=self.max, shape=(self.observation_num, ) , dtype=np.float32)

	def step(self, action):
		self.x += action[0] / self.max
		self.y += action[1] / self.max

		distX = abs(self.x - self.target_x)
		distY = abs(self.y - self.target_y)

		done = distX < 10 and distY < 10
		if done:
			self.win = 1
			reward = 10
		else:
			reward = -(distX ** 2 + distY ** 2) / 5000

		return self.get_info(), reward, False, {}

	def reset(self):
		self.x = random.randint(10,490)
		self.y = random.randint(10,490)

		self.target_x = 250
		self.target_y = 250

		if GRAPHING and self.viewer:
			update(self.win)

		self.win = 0

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
		x = min((self.target_x - self.x), self.max)
		x = max((self.target_x - self.x), -self.max)
		y = min((self.target_y - self.y), self.max)
		y = max((self.target_y - self.y), -self.max)
		return np.array([x, y])