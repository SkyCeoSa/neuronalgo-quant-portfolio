"""
Example RL agent skeleton (pseudo-code)
This file is a starting point: not a production agent.
"""
import numpy as np

class SimpleRandomAgent:
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, obs):
        # random policy (baseline)
        return np.random.choice(self.action_space)

if __name__ == '__main__':
    from collections import namedtuple
    Step = namedtuple('Step', ['obs','reward','done'])
    env = None  # replace with your market sim env
    agent = SimpleRandomAgent(action_space=[-1,0,1])
    print("This is a skeleton - integrate with your env and training loop.")
