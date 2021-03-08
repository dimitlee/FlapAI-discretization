import os, sys
sys.path.append('.')
sys.path.append('./game')
sys.path.append('./agents')
sys.path.append('./utils')
from BaselineAgent import BaselineAgent
from QLearningAgent import QLearningAgent
from SARSAAgent import SARSAAgent

agent = QLearningAgent(actions = [0, 1], rounding = 50, probFlap = 0.1)
agent.loadQValues()
for i in range(10):
    agent.test(1000)
