'''
This is the main file of the program. It processes command line arguments
and runs different Flappy Bird agents.
'''

import os, sys
sys.path.append('.')
sys.path.append('./game')
sys.path.append('./agents')
sys.path.append('./utils')
import argparse
import time

from BaselineAgent import BaselineAgent
from QLearningAgent import QLearningAgent
from SARSAAgent import SARSAAgent   # We got rid of function approximation allgorithms for our project
# function to generate graphs from the score files
from generate_graph import generate_graph
from generate_boxplot import generate_boxplot

import warnings
warnings.filterwarnings('ignore')


agent_options = ['Baseline' ,'QLearning', 'SARSA']  # We got rid of function approximation allgorithms for our project
order_options = ['forward', 'backward']


def parseArgs():
    ''' Reads command line arguments. '''
    parser = argparse.ArgumentParser(description = 'An AI Agent for Flappy Bird.',
                                     formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--algo', type = str, default = 'QLearning',
                        help = 'Learning algorithm.', choices = agent_options)

    # Parameters for Q-learning
    parser.add_argument('--rounding', type = int, default = None,
                        help = 'Level of discretization.')
    parser.add_argument('--probFlap', type = float, default = 0.1,
                        help = 'Probability of flappingin epsilon-greedy policy.')
    parser.add_argument('--order', type = str, default = 'forward',
                        choices = order_options, help = 'Order of Q-value updates.')
    parser.add_argument('--discount', type = float, default = 1.,
                        help = 'Discount factor.')
    parser.add_argument('--numTrainIters', type = int, default = 10000,
                        help = 'Number of training iterations.')
    parser.add_argument('--numTestIters', type = int, default = 1000,
                        help = 'Number of testing iterations.')
    parser.add_argument('--evalPerIters', type = int, default = 250,
                        help = 'Frequency of running evaluation.')
    parser.add_argument('--epsilon', type = float, default = 0.,
                        help = 'Epsilon-greedy policy.')
    parser.add_argument('--lr', type = float, default = 0.1,
                        help = 'Learning rate.')
    parser.add_argument('--epsilonDecay', action = 'store_true',
                        help = 'Use epsilon decay or not.')
    parser.add_argument('--lrDecay', action = 'store_true',
                        help = 'Use learning rate decay or not.')
    parser.add_argument('--graph', action = 'store_true',
                        help = 'To generate graph for scores or not')
    parser.add_argument('--startIter', type = int, default = 0,
                        help = 'The iteration to start training with in case of continuing stopped experiment')


    args = parser.parse_known_args()[0]
    return args


def main():
    ''' Main program. '''
    print("Welcome to Flappy Bird.")
    args = parseArgs()

    start = time.time()

    if args.algo == 'Baseline':
        agent = BaselineAgent(actions = [0, 1], probFlap = args.probFlap)
        agent.train(numIters = args.numTrainIters, evalPerIters = args.evalPerIters,
                    numItersEval = args.numTestIters)

    elif args.algo == 'QLearning':
        agent = QLearningAgent(actions = [0, 1], rounding = args.rounding, probFlap = args.probFlap)
        if args.startIter != 0:
            print(f"Starting from iteration: {args.startIter}")
            agent.loadQValues(args.startIter)
        agent.train(order = args.order, numIters = args.numTrainIters, epsilon = args.epsilon,
                    discount = args.discount, eta = args.lr, epsilonDecay = args.epsilonDecay,
                    etaDecay = args.lrDecay, evalPerIters = args.evalPerIters,
                    numItersEval = args.numTestIters, startIter = args.startIter)
        if args.graph:  # generate graph if specified
            generate_graph(algo=args.algo, rounding=args.rounding, numTrainIters=args.numTrainIters,
                            interval=args.evalPerIters)

    elif args.algo == 'SARSA':
        agent = SARSAAgent(actions = [0, 1], rounding = args.rounding, probFlap = args.probFlap)
        if args.startIter != 0:
            print(f"Starting from iteration: {args.startIter}")
            agent.loadQValues(args.startIter)
        agent.train(order = args.order, numIters = args.numTrainIters, epsilon = args.epsilon,
                    discount = args.discount, eta = args.lr, epsilonDecay = args.epsilonDecay,
                    etaDecay = args.lrDecay, evalPerIters = args.evalPerIters,
                    numItersEval = args.numTestIters, startIter = args.startIter)
        if args.graph:
            generate_graph(algo=args.algo, rounding=args.rounding, numTrainIters=args.numTrainIters,
                            interval=args.evalPerIters)

    end = time.time()   # counts elapsed time
    print(f"Total of {end - start} seconds")
    print(f"{(end - start)//3600} hours, {((end - start)%3600)//60} minutes, {((end - start)%3600)%60} seconds")


if __name__ == '__main__':
    main()
