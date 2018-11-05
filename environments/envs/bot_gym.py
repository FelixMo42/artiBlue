import numpy as np
import gym
from gym import spaces
import random
import matplotlib.pyplot as plt
import numpy as np
import math

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
		self.max = 300
		self.speed = 2.0

		self.action_num = 2
		self.observation_num = 3

		self.action_space = spaces.Box(low=-self.speed, high=self.speed, shape=(self.action_num, ), dtype=np.float32)
		self.observation_space = spaces.Box(low=-self.max, high=self.max, shape=(self.observation_num, ) , dtype=np.float32)

	def step(self, action):
		#self.x += action[0] * math.sin(math.radians(self.angle))
		#self.y += action[0] * math.cos(math.radians(self.angle))

		self.angle += action[1]

		distX = abs(self.x - self.target_x)
		distY = abs(self.y - self.target_y)

		a1 = math.radians(90 - self.angle)
		a2 = math.atan2(self.target_y - self.y, self.target_x - self.x)

		a = math.atan2(math.sin(a1-a2), math.cos(a1-a2))
		reward = -(a ** 2) * 10#-(distX ** 2 + distY ** 2) / 2500

		done = distX < 10 and distY < 10
		if done:
			self.win = 1

		return self.get_info(), -(action[1] ** 2), False, {}

	def reset(self):
		self.x = 50#random.randint(10,490)
		self.y = 50#random.randint(10,490)
		self.angle = 45

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

			bot = rendering.make_capsule(10,20)
			self.bot_transform = rendering.Transform()
			bot.add_attr(self.bot_transform)
			bot.set_color(0,0,255)
			self.viewer.add_geom(bot)

		self.target_transform.set_translation(self.target_x, self.target_y)
		self.bot_transform.set_rotation(math.radians(90 - self.angle))
		self.bot_transform.set_translation(self.x, self.y)

		return self.viewer.render(return_rgb_array = mode=='rgb_array')

	def get_info(self):
		x = max(min(self.target_x - self.x, self.max), -self.max)
		y = max(min(self.target_y - self.y, self.max), -self.max)

		angle_sin = math.sin( math.radians(self.angle) ) * self.max
		angle_cos = math.cos( math.radians(self.angle) ) * self.max

		angle_offset = math.radians(90 - self.angle) - math.atan2(self.target_y - self.y, self.target_x - self.x)

		return np.array([x, y, angle_offset])
