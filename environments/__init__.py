import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='BotGym-v0',
    entry_point='environments.envs:BotGym',
)