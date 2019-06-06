#!/usr/bin/python

"""
generate_trial_data.py

Use this module to generate trial data for the 2-armed bandit experiment with
fractals.
"""

import csv
import numpy as np

# Experiment parameters
NUM_TRIALS = 6
REWARD = 1
PROB_LOWER_BOUND = 0.25
PROB_UPPER_BOUND = 0.75
PROB_SIGMA = 0.03

fractals = np.random.choice(np.arange(1,21), 2, replace=False)
fractal_left = fractals[0]
fractal_right = fractals[1]

with open('trial_types.csv', 'w') as csvfile:
    fieldnames = ['trial', 'fractal_left', 'fractal_right', 'prob_left',
                  'prob_right', 'reward_left', 'reward_right']
    writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
    writer.writeheader()

    prob_left = np.random.uniform(PROB_LOWER_BOUND, PROB_UPPER_BOUND)
    prob_right = np.random.uniform(PROB_LOWER_BOUND, PROB_UPPER_BOUND)

    for trial in xrange(1, NUM_TRIALS + 1):
        writer.writerow({'trial': trial,
                         'fractal_left': 'fig/%d.jpg' % fractal_left,
                         'fractal_right': 'fig/%d.jpg' % fractal_right,
                         'prob_left': '%.3f' % prob_left,
                         'prob_right': '%.3f' % prob_right,
                         'reward_left': REWARD,
                         'reward_right': REWARD})

        noise = PROB_SIGMA * np.random.randn()
        prob_left += noise
        if not (PROB_LOWER_BOUND <= prob_left <= PROB_UPPER_BOUND):
            prob_left -= 2. * noise

        noise = PROB_SIGMA * np.random.randn()
        prob_right += noise
        if not (PROB_LOWER_BOUND <= prob_right <= PROB_UPPER_BOUND):
            prob_right -= 2. * noise
