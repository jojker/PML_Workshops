import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from pylab import *

# Import definitions of the environments.
import RL_worlds as worlds

# Import helper functions for plotting.
from plot_util import *

Data = pd.read_csv('g_2017_Jul_16_1609.csv')
print Data.head()



reward = Data['reward']
action = Data['response.keys']

action[action=='left'] = 0
action[action=='right'] = 1

print action


def softmax(state, value, beta):
    """
    Softmax policy: selects action probabilistically depending on the value.
    Args:
        state: an integer corresponding to the current state.
        value: a matrix indexed by state and action.
        params: a dictionary containing the default parameters.
    Returns:
        an integer corresponding to the action chosen according to the policy.
    """
    value_now = value[state,:]
    prob = exp(value_now * beta)  # beta is the inverse temperature
    prob = prob / sum(prob)  # normalize
    cum_prob = cumsum(prob)  # cummulation summation
    action = where(cum_prob > rand())[0][0]
    return action[0]

def neg_likelihood (alpha, beta, gamma):
    for


