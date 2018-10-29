from models.DDPG import DDPG

model = DDPG("BotGym-v0")

model.train(RENDER=True)