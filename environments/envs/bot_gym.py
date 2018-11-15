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

	dataWin = []
	data10Win = []
	dataRew = []
	data10Rew = []

	avgPer = 10

	def update(w, r):
		dataWin.append(w)
		dataRew.append(r)

		if len(dataWin) % avgPer == 0:
			data10Win.append(sum(dataWin[-avgPer:]) / avgPer)
			data10Rew.append(sum(dataRew[-avgPer:]) / avgPer)

		fig.clf()
		plt.subplot(2, 1, 1)
		plt.plot(np.arange(len(data10Win)) * avgPer, data10Win)
		plt.ylabel("win percent")

		plt.subplot(2, 1, 2)
		plt.plot(np.arange(len(data10Rew)) * avgPer, data10Rew)
		plt.ylabel("avg reward")

class BotGym(gym.Env):
	_seed =  42
	viewer = None

	avgReward = 0

	def __init__(self):
		self.max = 300
		self.speed = 2.0

		self.action_num = 2
		self.observation_num = 3

		self.avgReward = 0

		self.action_space = spaces.Box(low=-self.max, high=self.max, shape=(self.action_num, ), dtype=np.float32)
		self.observation_space = spaces.Box(low=-self.max, high=self.max, shape=(self.observation_num, ) , dtype=np.float32)

	def step(self, action):
		a0 = action[0] * self.speed / self.max
		a1 = action[1] * self.speed / self.max

		self.x += a0 * math.sin(math.radians(self.angle))
		self.y += a0 * math.cos(math.radians(self.angle))

		self.angle += a1

		distX = abs(self.x - self.target_x)
		distY = abs(self.y - self.target_y)

		#a1 = math.radians(90 - self.angle)
		#a2 = math.atan2(self.target_y - self.y, self.target_x - self.x)
		#a = math.atan2(math.sin(a1-a2), math.cos(a1-a2))
		#reward = -(a ** 2) * 10#-(distX ** 2 + distY ** 2) / 2500

		reward = -(distX ** 2 + distY ** 2) / 5000

		done = distX < 10 and distY < 10
		if done:
			reward = 10
			self.win = 1.0

		self.avgReward += reward
		return self.get_info(), reward, done, {}

	def reset(self):
		self.x = random.randint(10,490)
		self.y = random.randint(10,490)
		self.angle = 0#45

		self.target_x = 250
		self.target_y = 250

		if GRAPHING and self.viewer:
			update(self.win, self.avgReward / 200.0)

		self.avgReward = 0
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

		a1 = math.radians(90 - self.angle)
		a2 = math.atan2(self.target_y - self.y, self.target_x - self.x)

		angle_offset = math.atan2(math.sin(a1-a2), math.cos(a1-a2)) / math.pi * self.max

		return np.array([x, y, angle_offset])
