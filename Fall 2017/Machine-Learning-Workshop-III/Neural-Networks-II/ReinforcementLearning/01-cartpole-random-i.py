# This is a version of CartPole which tests that the environment works.
import gym


nsteps = 1000  # change this value
env = gym.make('CartPole-v0')  # create your environment here
env.reset()  # prepare the environment for use

i_stop=0;
for i in range(nsteps):
    env.render()  # display the environment at this step
    action = env.action_space.sample()  # choose a random action
    result=env.step(action)  # now loop through the action (more on this later)
    if result[2]:
        print('out of bounds after '+str(i-i_stop+1)+' steps')
        env.reset()
        i_stop=i


# Because we're making some random actions, chances are that the CartPole will go out of bounds
# during this time, and the game will be marked as "done" during that time.
#
# So, to allow for more fine-grained control, we examine the results returned by `action`.
