from models.DDPG import DDPG

model = DDPG("Pendulum-v0", [2,4,1])

'''
import random

from models.BasicModel import BasicModel

model = BasicModel([2,1])

iterations = 2000
batch = 100
for i in range(iterations):
	i = []
	e = []
	for j in range(batch):
		n1 = random.randint(1,10)
		n2 = random.randint(1,10)
		i.append([n1,n2])
		e.append([n1 * n2])
	model.train(i, e)

print(model.test([4, 3]))
'''