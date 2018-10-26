'''from models.LinearModel import LinearModel

model = LinearModel()

for i in range(5000):
	model.train([i], [i * 2 + 3])

print("4 * 2 + 3 =", model.test(4))'''

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
model.dump()