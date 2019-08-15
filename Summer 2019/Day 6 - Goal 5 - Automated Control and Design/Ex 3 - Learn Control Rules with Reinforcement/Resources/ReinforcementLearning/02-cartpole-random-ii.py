# This is a version of CartPole which creates trails or episodes.
import gym


ntrials = 50  # number of trials
nsteps = 1000   # max number of steps per trial
env = gym.make('CartPole-v0')  # create your environment here


for trial in range(1, ntrials+1):
    observation = env.reset() # prepare the environment for this trial / episode

    for step in range(1, nsteps+1):
        env.render()
        action = env.action_space.sample()  # choose a random action

        # get what was observed, the reward, if the trial was completed
        # and information about the run.
        observation, reward, done, info = env.step(action)

        # from before we know that the application can sometimes terminate before
        # the trial is complete. If that should occur, we want to stop.
        if done:
            print('Trial {0} finished after {1} timesteps.'.format(trial, step))
            break


# Unlike the previous case, we can now run the example as many times as we'd like,
# and, we don't have to worry about whether the example finishes prematurely or 
# not.
#
# However, random actions will not get us anywhere. We need to optimize the actions
# and how they are performed.
