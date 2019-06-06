# This is a version of CartPole which uses a NN to find the best motions which balance the pole.
import gym
import random
import numpy as np
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from statistics import median, mean
from collections import Counter


LR = 1e-3
num_games = 50    # number of trials / episodes
goal_steps = 200  # number of steps per trial
score_requirement = 50  # the minimum score to achieve
initial_games = 10000   # number of games to use for training
env = gym.make('CartPole-v0')  # create your environment here
env.reset()


def initial_population():
    # [OBS, MOVES]
    training_data = []
    # all scores:
    scores = []
    # just the scores that met our threshold:
    accepted_scores = []
    # iterate through however many games we want:
    for _ in range(initial_games):
        score = 0
        # moves specifically from this environment:
        game_memory = []
        # previous observation that we saw
        prev_observation = []
        # for each frame in 200
        for _ in range(goal_steps):
            # choose random action (0 or 1)
            action = random.randrange(0,2)
            # do it!
            observation, reward, done, info = env.step(action)

            # notice that the observation is returned FROM the action
            # so we'll store the previous observation here, pairing
            # the prev observation to the action we'll take.
            if len(prev_observation) > 0 :
                game_memory.append([prev_observation, action])
            prev_observation = observation
            score+=reward
            if done: break

        # IF our score is higher than our threshold, we'd like to save
        # every move we made
        # NOTE the reinforcement methodology here.
        # all we're doing is reinforcing the score, we're not trying
        # to influence the machine in any way as to HOW that score is
        # reached.
        if score >= score_requirement:
            accepted_scores.append(score)
            for data in game_memory:
                # convert to one-hot (this is the output layer for our neural network)
                if data[1] == 1:
                    output = [0,1]
                elif data[1] == 0:
                    output = [1,0]
                # saving our training data
                training_data.append([data[0], output])

        # reset env to play again
        env.reset()
        # save overall scores
        scores.append(score)

    # just in case you wanted to reference later
    training_data_save = np.array(training_data)
    np.save('saved.npy',training_data_save)

    # some stats here, to further illustrate the neural network magic!
    print('Average accepted score:',mean(accepted_scores))
    print('Median score for accepted scores:',median(accepted_scores))
    print(Counter(accepted_scores))

    return training_data



# Create a simple multilayer perceptron model
def neural_network_model(input_size):
    # our input layer which will be dependent on the number of inputs
    # we want to create
    network = input_data(shape=[None, input_size, 1], name='input')

    # our first hidden layer
    network = fully_connected(network, 128, activation='relu')
    network = dropout(network, 0.8)

    # our second hiddent layer
    network = fully_connected(network, 256, activation='relu')
    network = dropout(network, 0.8)

    # our third hidden layer
    network = fully_connected(network, 512, activation='relu')
    network = dropout(network, 0.8)

    # our fourth hidden layer
    network = fully_connected(network, 256, activation='relu')
    network = dropout(network, 0.8)

    # our fifth hidden layer
    network = fully_connected(network, 128, activation='relu')
    network = dropout(network, 0.8)

    # the output layer
    network = fully_connected(network, 2, activation='softmax')
    network = regression(network, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')
    model = tflearn.DNN(network, tensorboard_dir='log')

    return model


def train_model(training_data, model=False):
    X = np.array([i[0] for i in training_data]).reshape(-1,len(training_data[0][0]),1)
    y = [i[1] for i in training_data]

    if not model:
        model = neural_network_model(input_size = len(X[0]))

    model.fit({'input': X}, {'targets': y}, n_epoch=5, snapshot_step=500, show_metric=True, run_id='openai_learning')
    return model


training_data = initial_population()
model = train_model(training_data)

scores = list()
choices = list()

for trial in range(1, num_games+1):
    score = 0
    game_memory = list()
    prev_observations = list()
    env.reset() # prepare the environment for this trial / episode

    for step in range(1, goal_steps+1):
        env.render()

        # previously, we performed a random action:
        # `action = env.action_space.sample()`
        #
        # now, we're going to say that if the angle is positive, move right (1)
        # otherwise, move left (0)
        if len(prev_observations) == 0:
            # create a random action between 0 and 1
            action = random.randrange(0, 2)
        else:
            action = np.argmax(model.predict(prev_observations.reshape(-1, len(prev_observations), 1))[0])

        choices.append(action)

        # get what was observed, the reward, if the trial was completed
        # and information about the run.
        new_observation, reward, done, info = env.step(action)
        prev_observations = new_observation

        game_memory.append([new_observation, action])
        score += reward


        # from before we know that the application can sometimes terminate before
        # the trial is complete. If that should occur, we want to stop.
        if done:
            print('Trial {0} finished after {1} timesteps. Score: {2}'.format(trial, step, score))
            break
    scores.append(score)


print('Average Score:',sum(scores)/float(len(scores)))
print('choice 1:{}  choice 0:{}'.format(choices.count(1)/len(choices),choices.count(0)/len(choices)))
print(score_requirement)
