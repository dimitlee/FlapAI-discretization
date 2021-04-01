import os, sys
sys.path.append('.')
sys.path.append('./game')
sys.path.append('./agents')
sys.path.append('./utils')
import argparse

from generate_bargraph import generate_bargraph


agent_options = ['Baseline' ,'QLearning', 'SARSA']

def parseArgs():
    ''' Reads command line arguments. '''
    parser = argparse.ArgumentParser(description = 'Bargraph generator for scores from Flappy Bird.',
                                     formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--algo', type = str, default = 'QLearning',
                        help = 'Learning algorithm.', choices = agent_options)
    parser.add_argument('--rounding', type = int, default = None,
                        help = 'Level of discretization.')

    args = parser.parse_known_args()[0]
    return args

def main():
    args = parseArgs()

    generate_bargraph(algo=args.algo, rounding=args.rounding)

if __name__ == '__main__':
    main()
