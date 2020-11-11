# Study of the Impact of Discretization in RL: Tradeoff Between Convergence and Final Performance in Huge State Spaces

This repository borrows code from https://github.com/taivu1998/FlapAI-Bird for reproduction of their Reinforcement Learning Experiment in Flappy-Bird environment. In our experiment we are focusing on discretization feature in order to find the balance between convergence and final performance.

## Google Colab

You can walk through a [Google Colab notebook](https://colab.research.google.com/drive/1lMExzNABtF8oMpOh3EqbLdoTjHE_09fG?authuser=1#scrollTo=XB0YesYbfMvx) to check out the process of working with this project.

## Installation

The project requires the following frameworks:

- Pygame: https://www.pygame.org

- PyGame Learning Environment: https://github.com/ntasfi/PyGame-Learning-Environment

- OpenAI Gym: https://gym.openai.com

- gym-ple: https://github.com/lusob/gym-ple

- PyTorch: https://pytorch.org

- OpenCV: https://opencv.org

- MatPlotLib: https://matplotlib.org/3.3.2/index.html

## Train an Agent

There are a number of arguments that main.py accepts, some of them are:

* **--algo** - the RL algorithm you want to run ("Baseline", "QLearning", "SARSA", etc.)
* **--order** - how the Q-table is updated ("backward" or "forward")
* **--rounding** - Discretization level (smaller means higher state space and thus longer convergence)
* **--epsilon** - Exploration rate (probability of choosing random action)
* **--lr** - Learning rate (coefficient of a target value in Q-values update equation)
* **--discount** - Discount factor (coefficient of the next state's Q-value in the update equation)
* **--probFlap** - Probability to choose action 1 when choosing random action

We run the experiment using **Q-Learning** agent with **backward** updates and exploration rate of **0**. Below is an example of how the experiment can be started.

```bash
python3 main.py --algo QLearning --probFlap 0.1 --rounding 50 --lr 0.8 --order backward --epsilon 0
```

You can tweak the parameters as you want, try different algorithms by replacing "QLearning" with an algorithm from ('Baseline' ,'QLearning', 'SARSA', 'FuncApproxLR', 'FuncApproxDNN', 'FuncApproxCNN').

## Evaluating performance

After some time (250 iterations by default) algorithms start a testing phase, during which scores (number of tubes passed) are recorded and then written into a json file, where the name of the file represents at which iteration the testing began. You can generate graphs of maximum score and average score over several such testing phases. Below is an example of how you can do that in console:

```bash
python graph.py --algo QLearning --rounding 50 --lastIter 2500 --interval 250
```

* **--lastIter** here represents the caption of the last score.json file. In this case it would be named: *score_2500.json*
* **--interval** represents the interval which separates two subsequent testing phases. In other words names' captions would be separated by this value. E.g *score_250.json*, *score_500.json*, *score_750.json*, ...

Alternatively you can append *--graph* argument with value *True* to the call of main.py:

```bash
python3 main.py --algo QLearning --probFlap 0.1 --rounding 50 --lr 0.8 --order backward --epsilon 0
```

In this case the graph will be generated at the end of training.
## Original Authors

* **Tai Vu** - Stanford University

* **Leon Tran** - Stanford University
