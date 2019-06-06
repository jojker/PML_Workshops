#!/usr/bin/python

# HELPER FUNCTIONS FOR PLOTTING

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve as conv


def plot_state_action_values(env, value):
    """
    Generate plot showing value of each action at each state.
    """
    fig = plt.figure()
    for a in range(env.n_actions): 
        plt.plot(range(env.n_states), value[:,a], marker='o', linestyle='--')
    plt.xlabel('States')
    plt.ylabel('Value')
    if env.name == 'n_armed_bandit':
        plt.legend(['0','1','2','3'], loc='lower right')
    elif env.name == 'cheese_world':
        plt.legend(['L','R'], loc='lower right')
    else:
        plt.legend(['R','U','L','D'], loc='lower right')
    return fig


def plot_quiver_max_action(env, action_matrix):
    """
    Generate plot showing action of maximum value or maximum probability at
      each state (not for n-armed bandit or cheese_world).
    """
    if env.name == 'n_armed_bandit' or env.name == 'cheese_world':
        print("Quiver plot can only be generated for 2-dimensional "
              "grid worlds.")
        return None

    X = np.tile(np.arange(env.dim_x),[env.dim_y,1]) + 0.5
    Y = np.tile(np.arange(env.dim_y)[::-1][:,np.newaxis], [1,env.dim_x]) + 0.5
    which_max = np.reshape(action_matrix.argmax(axis=1), (env.dim_y,env.dim_x))
    if env.name != 'windy_cliff_grid':
        which_max = which_max[::-1,:]
    U = np.zeros(X.shape)
    V = np.zeros(X.shape)
    U[which_max==0] = 1
    V[which_max==1] = 1
    U[which_max==2] = -1
    V[which_max==3] = -1
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.quiver(X, Y, U, V)
    plt.xlim([-0.5, env.dim_x+0.5])
    plt.ylim([-0.5, env.dim_y+0.5])
    plt.title('Maximum value/probability actions')
    ax.set_xticks(np.linspace(0.5, env.dim_x-0.5, num=env.dim_x))
    ax.set_xticklabels(["%d" % x for x in np.arange(env.dim_x)])
    ax.set_xticks(np.arange(env.dim_x+1), minor=True)
    ax.set_yticks(np.linspace(0.5, env.dim_y-0.5, num=env.dim_y))
    ax.set_yticklabels(
        ["%d" % y for y in np.arange(0, env.dim_y*env.dim_x, env.dim_x)])
    if env.name == 'windy_cliff_grid':
        ax.set_yticklabels(
            ["%d" % y for y in np.arange(
                0, env.dim_y*env.dim_x, env.dim_x)][::-1])
    ax.set_yticks(np.arange(env.dim_y+1), minor=True)
    ax.grid(which='minor',linestyle='-')
    return fig


def plot_heatmap_max_val(env, value):
    """
    Generate heatmap showing maximum value at each state (not for n-armed
      bandit).
    """
    if env.name == 'n_armed_bandit':
        print("Heatmap can only be generated for grid worlds.")
        return None
    if value.ndim == 1:
        value_max = np.reshape(value, (env.dim_y,env.dim_x))
    else:
        value_max = np.reshape(value.max(axis=1), (env.dim_y,env.dim_x))
    if env.name != 'windy_cliff_grid':
        value_max = value_max[::-1,:]
    fig = plt.figure()
    plt.title('Maximum value per state')
    ax = fig.add_subplot(111)
    im = ax.imshow(value_max, interpolation='none', cmap='afmhot')
    ax.set_xticks(np.linspace(0, env.dim_x-1, num=env.dim_x))
    ax.set_xticklabels(["%d" % x for x in np.arange(env.dim_x)])
    ax.set_yticks(np.linspace(0, env.dim_y-1, num=env.dim_y))
    ax.set_yticklabels(
        ["%d" % y for y in np.arange(0, env.dim_y*env.dim_x, env.dim_x)])
    if env.name != 'windy_cliff_grid':
        ax.set_yticklabels(
            ["%d" % y for y in np.arange(
                0, env.dim_y*env.dim_x, env.dim_x)][::-1])
    fig.colorbar(im)
    return fig


def plot_rewards(n_episodes, rewards, average_range=10):
    """
    Generate plot showing total reward accumulated in each episode.
    """
    smoothed_rewards = (conv(rewards, np.ones(average_range), mode='same')
                        / average_range)
    fig = plt.figure()
    plt.plot(range(0, n_episodes, average_range),
             smoothed_rewards[0:n_episodes:average_range],
             marker='o', linestyle='--')
    plt.xlabel('Episodes')
    plt.ylabel('Total reward')
    return fig


