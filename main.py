from models.LinearModel import LinearModel as Model

model = Model()

model.train()

print(model.test(4))