import os, sys
sys.path.append('.')
sys.path.append('./game')
sys.path.append('./agents')
sys.path.append('./utils')
import argparse

from generate_graph import generate_graph


agent_options = ['Baseline' ,'QLearning', 'SARSA']

def parseArgs():
    ''' Reads command line arguments. '''
    parser = argparse.ArgumentParser(description = 'Graph generator for scores from Flappy Bird.',
                                     formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--algo', type = str, default = 'QLearning',
                        help = 'Learning algorithm.', choices = agent_options)
    parser.add_argument('--rounding', type = int, default = None,
                        help = 'Level of discretization.')
    parser.add_argument('--lastIter', type = int, default = 10000,
                        help = 'Number of the last scores_iter file to read')
    parser.add_argument('--interval', type = int, default = 250,
                        help = 'Space between numbers of the files')

    args = parser.parse_known_args()[0]
    return args

def main():
    args = parseArgs()

    generate_graph(algo=args.algo, rounding=args.rounding, numTrainIters=args.lastIter, interval=args.interval)

if __name__ == '__main__':
    main()
