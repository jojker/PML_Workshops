#!/usr/bin/python

# ENVIRONMENT / WORLD DEFINITIONS

class world(object):
    def __init__(self):
        return

    def get_outcome(self):
        print("Abstract method, not implemented")
        return

    def get_all_outcomes(self):
        outcomes = {}
        for state in xrange(self.n_states):
            for action in xrange(self.n_actions):
                next_state, reward = self.get_outcome(state, action)
                outcomes[state, action] = [(1, next_state, reward)]
        return outcomes


class n_armed_bandit(world):
    """
    World: N-Armed bandit.
    Only one state, multiple actions.
    Each action returns different amount of reward.
    """
    def __init__(self):
        self.name = "n_armed_bandit"
        self.n_states = 1
        self.n_actions = 4
        self.dim_x = 1
        self.dim_y = 1

    def get_outcome(self, state, action):
        if not 0 <= action <= self.n_actions:
            print("Action must be between 0 and 3.")
            return None, None
        next_state = None  # session ends
        rewards = [0, 0.5, -0.5, 1]
        reward = rewards[action]
        return int(next_state) if next_state is not None else None, reward


class cheese_world(world):
    """
    World: Cheese world.
    4 states, 2 actions.
    States represent a one-dimensional track: 0 1 2 3
    0 is always the starting state.
    Actions 0, 1 correspond to move left and right.
    Moving left at state 0 stays at 0.
    Moving right at state 2 gets the reward.
    Moving right at state 3 stays at 3.
    """
    def __init__(self):
        self.name = "cheese_world"
        self.n_states = 4
        self.n_actions = 2
        self.dim_x = 4
        self.dim_y = 1

    def get_outcome(self, state, action):
        if state == 3:  # goal state
            reward = 0
            next_state = None
            return next_state, reward
        reward = 0  # default reward
        if action == 0:  # move left
            next_state = state - 1
            if state == 0:
                next_state = state
        elif action == 1:  # move right
            next_state = state + 1
            if state == 2:
                reward = 1
        else:
            print("Action must be between 0 and 1.")
            next_state = None
            reward = None
        return int(next_state) if next_state is not None else None, reward


class cliff_world(world):
    """
    World: Cliff world.
    40 states (4-by-10 grid world).
    The mapping from state to the grids are as follows:
    30 31 32 ... 39
    20 21 22 ... 29
    10 11 12 ... 19
    0  1  2  ...  9
    0 is the starting state (S) and 9 is the goal state (G).
    Actions 0, 1, 2, 3 correspond to right, up, left, down.
    Moving anywhere from state 9 (goal state) will end the session.
    Taking action down at state 11-18 will go back to state 0 and incur a
        reward of -100.
    Landing in any states other than the goal state will incur a reward of -1.
    Going towards the border when already at the border will stay in the same
        place.
    """
    def __init__(self):
        self.name = "cliff_world"
        self.n_states = 40
        self.n_actions = 4
        self.dim_x = 10
        self.dim_y = 4

    def get_outcome(self, state, action):
        if state == 9:  # goal state
            reward = 0
            next_state = None
            return next_state, reward
        reward = -1  # default reward value
        if action == 0:  # move right
            next_state = state + 1
            if state % 10 == 9:  # right border
                next_state = state
            elif state == 0:  # start state (next state is cliff)
                next_state = None
                reward = -100
        elif action == 1:  # move up
            next_state = state + 10
            if state >= 30:  # top border
                next_state = state
        elif action == 2:  # move left
            next_state = state - 1
            if state % 10 == 0:  # left border
                next_state = state
        elif action == 3:  # move down
            next_state = state - 10
            if state >= 11 and state <= 18:  # next is cliff
                next_state = None
                reward = -100
            elif state <= 9:  # bottom border
                next_state = state
        else:
            print("Action must be between 0 and 3.")
            next_state = None
            reward = None
        return int(next_state) if next_state is not None else None, reward


class quentins_world(world):
    """
    World: Quentin's world.
    100 states (10-by-10 grid world).
    The mapping from state to the grid is as follows:
    90 ...       99
    ...
    40 ...       49
    30 ...       39
    20 21 22 ... 29
    10 11 12 ... 19
    0  1  2  ...  9
    54 is the start state.
    Actions 0, 1, 2, 3 correspond to right, up, left, down.
    Moving anywhere from state 99 (goal state) will end the session.
    Landing in red states incurs a reward of -1.
    Landing in the goal state (99) gets a reward of 1.
    Going towards the border when already at the border will stay in the same
        place.
    """
    def __init__(self):
        self.name = "quentins_world"
        self.n_states = 100
        self.n_actions = 4
        self.dim_x = 10
        self.dim_y = 10

    def get_outcome(self, state, action):
        if state == 99:  # goal state
            reward = 0
            next_state = None
            return next_state, reward
        reward = 0  # default reward value     
        if action == 0:  # move right
            next_state = state + 1
            if state == 98:  # next state is goal state
                reward = 1
            elif state % 10 == 9:  # right border
                next_state = state
            elif state in [11, 21, 31, 41, 51, 61, 71,
                           12, 72,
                           73,
                           14, 74,
                           15, 25, 35, 45, 55, 65, 75]:  # next state is red
                reward = -1
        elif action == 1:  # move up
            next_state = state + 10
            if state == 89:  # next state is goal state
                reward = 1
            if state >= 90:  # top border
                next_state = state
            elif state in [2, 12, 22, 32, 42, 52, 62,
                           3, 63,
                           64,
                           5, 65,
                           6, 16, 26, 36, 46, 56, 66]:  # next state is red
                reward = -1
        elif action == 2:  # move left
            next_state = state - 1
            if state % 10 == 0:  # left border
                next_state = state
            elif state in [17, 27, 37, 47, 57, 67, 77,
                           16, 76,
                           75,
                           14, 74,
                           13, 23, 33, 43, 53, 63, 73]:  # next state is red
                reward = -1
        elif action == 3:  # move down
            next_state = state - 10
            if state <= 9:  # bottom border
                next_state = state
            elif state in [22, 32, 42, 52, 62, 72, 82,
                           23, 83,
                           84,
                           25, 85,
                           26, 36, 46, 56, 66, 76, 86]:  # next state is red
                reward = -1
        else:
            print("Action must be between 0 and 3.")
            next_state = None
            reward = None
        return int(next_state) if next_state is not None else None, reward

    
class windy_cliff_grid(world):
    """
    World: Windy grid world with cliffs.
    84 states(6-by-14 grid world).
    4 possible actions.
    Actions 0, 1, 3, 4 correspond to right, up, left, down.
    Each action returns different amount of reward.
    """
    def __init__(self):
        self.name = "windy_cliff_grid"
        self.n_states = 168
        self.n_actions = 4
        self.dim_x = 14
        self.dim_y = 12

    def get_outcome(self, state, action):
        """
        Obtains the outcome (next state and reward) obtained when taking
            a particular action from a particular state.
        Args:
            state: int, current state.
            action: int, action taken.
        Returns:
            the next state (int) and the reward (int) obtained.
        """
        next_state = None
        reward = 0
        if state in [53, 131]:  # end of MDP
            return next_state, reward
        if action == 0:  # move right
            next_state = state + 1
            if state == 38:  # goal state 1
                next_state = 53
                reward = 100
            elif state == 158:  # goal state 2
                next_state = 131
                reward = 100
            elif state == 1:  # cliff
                next_state = None
                reward = -100
            elif 7 <= state <= 51 and (state % 14 == 7 or state % 14 == 8 or state % 14 == 9):  # room 1 wind
                next_state = state + 29
            elif state in [63, 64, 65]:  # room 1 wind
                next_state = state + 15
            elif 10 <= state <= 68 and (state % 14 == 10 or state % 14 == 11 or state % 14 == 12):  # room 1 wind
                next_state = state + 15
            elif 113 <= state <= 157 and (state % 14 == 1 or state % 14 == 2 or state % 14 == 3):  # room 2 wind
                next_state = state - 13
            elif 130 <= state <= 160 and (state % 14 == 4 or state % 14 == 5 or state % 14 == 6):  # room 2 wind
                next_state = state - 27
            elif state in [116, 117, 118]:  # room 2 wind
                next_state = state - 13
            elif 19 <= state <= 75 and state % 14 == 5:  # room 1 left border
                next_state = state
            elif 105 <= state <= 161 and state % 14 == 7:  # room 2 right border
                next_state = state
            elif state % 14 == 13:  # world right border
                next_state = state
        elif action == 1:  # move up
            next_state = state - 14
            if state in [16, 17, 18, 84]:  # cliff
                next_state = None
                reward = -100
            elif 21 <= state <= 65 and (state % 14 == 7 or state % 14 == 8 or state % 14 == 9):  # room 1 wind
                next_state = state + 14
            elif state in [7, 8, 9]:  # room 1 wind
                next_state = state + 28
            elif state in [77, 78, 79]:  # room 1 wind
                next_state = state
            elif 24 <= state <= 82 and (state % 14 == 10 or state % 14 == 11 or state % 14 == 12):  # room 1 wind
                next_state = state
            elif state in [10, 11, 12]:  # room 1 wind
                next_state = state + 14
            elif 127 <= state <= 157 and (state % 14 == 1 or state % 14 == 2 or state % 14 == 3):  # room 2 wind
                next_state = state - 28
            elif 144 <= state <= 160 and (state % 14 == 4 or state % 14 == 5 or state % 14 == 6):  # room 2 wind
                next_state = state - 42
            elif state in [130, 131, 132]:  # room 2 wind
                next_state = state - 28
            elif 90 <= state <= 97:  # room 1 bottom border
                next_state = state
            elif 99 <= state <= 105:  # room 2 top border
                next_state = state
            elif 0 <= state <= 13:  # world top border
                next_state = state
        elif action == 2:  # move left
            next_state = state - 1
            if state == 40:  # goal state 1
                next_state = 53
                reward = 100
            elif state == 160:  # goal state 2
                next_state = 131
                reward = 100
            elif state in [29, 43, 57, 71, 5]:  # cliff
                next_state = None
                reward = -100
            elif 7 <= state <= 51 and (state % 14 == 7 or state % 14 == 8 or state % 14 == 9):  # room 1 wind
                next_state = state + 27
            elif state in [63, 64, 65]:  # room 1 wind
                next_state = state + 13
            elif 10 <= state <= 68 and (state % 14 == 10 or state % 14 == 11 or state % 14 == 12):  # room 1 wind
                next_state = state + 13
            elif 113 <= state <= 157 and (state % 14 == 1 or state % 14 == 2 or state % 14 == 3):  # room 2 wind
                next_state = state - 15
            elif state == 99:  # room 2 wind
                next_state = state - 15
            elif 130 <= state <= 160 and (state % 14 == 4 or state % 14 == 5 or state % 14 == 6):  # room 2 wind
                next_state = state - 29
            elif state in [116, 117, 118]:  # room 2 wind
                next_state = state - 15
            elif 20 <= state <= 76 and state % 14 == 6:  # room 1 left border
                next_state = state
            elif 106 <= state <= 162 and state % 14 == 8:  # room 2 right border
                next_state = state
            elif state % 14 == 0:  # world left border
                next_state = state
        elif action == 3:  # move down
            next_state = state + 14
            if state == 25:  # goal state 1
                next_state = 53
                reward = 100
            elif state == 145:  # goal state 2
                next_state = 131
                reward = 100
            elif state == 14:  # cliff
                next_state = None
                reward = -100
            elif 7 <= state <= 37 and (state % 14 == 7 or state % 14 == 8 or state % 14 == 9):  # room 1 wind
                next_state = state + 42
            elif state in [49, 50, 51]:  # room 1 wind
                next_state = state + 28
            elif 99 <= state <= 143 and (state % 14 == 1 or state % 14 == 2 or state % 14 == 3):  # room 2 wind
                next_state = state
            elif state in [155, 156, 157]:  # room 2 wind
                next_state = state - 14
            elif 116 <= state <= 146 and (state % 14 == 4 or state % 14 == 5 or state % 14 == 6):  # room 2 wind
                next_state = state - 14
            elif state in [102, 103, 104]:  # room 2 wind
                next_state = state
            elif state in [158, 159, 160]:  # room 2 wind
                next_state = state - 28
            elif 76 <= state <= 83:  # room 1 bottom border
                next_state = state
            elif 85 <= state <= 91:  # room 2 top border
                next_state = state
            elif 154 <= state <= 167:  # world bottom border
                next_state = state
        else:
            print("Action must be between 0 and 3.")
            next_state = None
            reward = None
        return int(next_state) if next_state is not None else None, reward


class windy_cliff_grid_2(windy_cliff_grid):
    def get_outcome(self, state, action):
        """
        Obtains the outcome (next state and reward) obtained when taking
            a particular action from a particular state.
        Args:
            state: int, current state.
            action: int, action taken.
        Returns:
            the next state (int) and the reward (int) obtained.
        """
        next_state = None
        reward = 0
        if state in [53, 131]:  # end of MDP
            return next_state, reward
        if action == 0:  # move right
            next_state = state + 1
            if state == 38:  # goal state 1
                next_state = 53
                reward = 100
            elif state == 158:  # goal state 2
                next_state = 131
                reward = 100
            elif state == 1:  # cliff
                next_state = None
                reward = -100
            elif 7 <= state <= 51 and (state % 14 == 7 or state % 14 == 8 or state % 14 == 9):  # room 1 wind
                next_state = state + 29
            elif state in [63, 64, 65]:  # room 1 wind
                next_state = state + 15
            elif 10 <= state <= 68 and (state % 14 == 10 or state % 14 == 11 or state % 14 == 12):  # room 1 wind
                next_state = state + 15
            elif 113 <= state <= 157 and (state % 14 == 1 or state % 14 == 2 or state % 14 == 3):  # room 2 wind
                next_state = state - 13
            elif 130 <= state <= 160 and (state % 14 == 4 or state % 14 == 5 or state % 14 == 6):  # room 2 wind
                next_state = state - 27
            elif state in [116, 117, 118]:  # room 2 wind
                next_state = state - 13
            elif 5 <= state <= 75 and state % 14 == 5:  # room 1 left border
                next_state = state
            elif 105 <= state <= 147 and state % 14 == 7:  # room 2 right border
                next_state = state
            elif state % 14 == 13:  # world right border
                next_state = state
        elif action == 1:  # move up
            next_state = state - 14
            if state in [16, 17, 18, 84]:  # cliff
                next_state = None
                reward = -100
            elif 21 <= state <= 65 and (state % 14 == 7 or state % 14 == 8 or state % 14 == 9):  # room 1 wind
                next_state = state + 14
            elif state in [7, 8, 9]:  # room 1 wind
                next_state = state + 28
            elif state in [77, 78, 79]:  # room 1 wind
                next_state = state
            elif 24 <= state <= 82 and (state % 14 == 10 or state % 14 == 11 or state % 14 == 12):  # room 1 wind
                next_state = state
            elif state in [10, 11, 12]:  # room 1 wind
                next_state = state + 14
            elif 127 <= state <= 157 and (state % 14 == 1 or state % 14 == 2 or state % 14 == 3):  # room 2 wind
                next_state = state - 28
            elif 144 <= state <= 160 and (state % 14 == 4 or state % 14 == 5 or state % 14 == 6):  # room 2 wind
                next_state = state - 42
            elif state in [130, 131, 132]:  # room 2 wind
                next_state = state - 28
            elif 90 <= state <= 96:  # room 1 bottom border
                next_state = state
            elif 98 <= state <= 105:  # room 2 top border
                next_state = state
            elif 0 <= state <= 13:  # world top border
                next_state = state
        elif action == 2:  # move left
            next_state = state - 1
            if state == 40:  # goal state 1
                next_state = 53
                reward = 100
            elif state == 160:  # goal state 2
                next_state = 131
                reward = 100
            elif state in [29, 43, 57, 71, 5]:  # cliff
                next_state = None
                reward = -100
            elif 7 <= state <= 51 and (state % 14 == 7 or state % 14 == 8 or state % 14 == 9):  # room 1 wind
                next_state = state + 27
            elif state in [63, 64, 65]:  # room 1 wind
                next_state = state + 13
            elif 10 <= state <= 68 and (state % 14 == 10 or state % 14 == 11 or state % 14 == 12):  # room 1 wind
                next_state = state + 13
            elif 113 <= state <= 157 and (state % 14 == 1 or state % 14 == 2 or state % 14 == 3):  # room 2 wind
                next_state = state - 15
            elif state == 99:  # room 2 wind
                next_state = state - 15
            elif 130 <= state <= 160 and (state % 14 == 4 or state % 14 == 5 or state % 14 == 6):  # room 2 wind
                next_state = state - 29
            elif state in [116, 117, 118]:  # room 2 wind
                next_state = state - 15
            elif 6 <= state <= 76 and state % 14 == 6:  # room 1 left border
                next_state = state
            elif 106 <= state <= 148 and state % 14 == 8:  # room 2 right border
                next_state = state
            elif state % 14 == 0:  # world left border
                next_state = state
        elif action == 3:  # move down
            next_state = state + 14
            if state == 25:  # goal state 1
                next_state = 53
                reward = 100
            elif state == 145:  # goal state 2
                next_state = 131
                reward = 100
            elif state == 14:  # cliff
                next_state = None
                reward = -100
            elif 7 <= state <= 37 and (state % 14 == 7 or state % 14 == 8 or state % 14 == 9):  # room 1 wind
                next_state = state + 42
            elif state in [49, 50, 51]:  # room 1 wind
                next_state = state + 28
            elif 99 <= state <= 143 and (state % 14 == 1 or state % 14 == 2 or state % 14 == 3):  # room 2 wind
                next_state = state
            elif state in [155, 156, 157]:  # room 2 wind
                next_state = state - 14
            elif 116 <= state <= 146 and (state % 14 == 4 or state % 14 == 5 or state % 14 == 6):  # room 2 wind
                next_state = state - 14
            elif state in [102, 103, 104]:  # room 2 wind
                next_state = state
            elif state in [158, 159, 160]:  # room 2 wind
                next_state = state - 28
            elif 76 <= state <= 82:  # room 1 bottom border
                next_state = state
            elif 84 <= state <= 91:  # room 2 top border
                next_state = state
            elif 154 <= state <= 167:  # world bottom border
                next_state = state
        else:
            print("Action must be between 0 and 3.")
            next_state = None
            reward = None
        return int(next_state) if next_state is not None else None, reward


