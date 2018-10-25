from models.LinearModel import LinearModel

model = LinearModel()

for i in range(2000):
	model.train([i], [i * 2])

print("4 * 2 =", model.test(4))