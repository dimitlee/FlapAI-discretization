# Study of the impact of discretization in RL: Tradeoff between convergence and final performance in huge state spaces

This repository borrows code from https://github.com/taivu1998/FlapAI-Bird for reproduction of their Reinforcement Learning Experiment in Flappy-Bird environment. In our experiment we are focusing on discretization feature in order to find the balance between convergence and final performance.

## Installation

The project requires the following frameworks:

- Pygame: https://www.pygame.org

- PyGame Learning Environment: https://github.com/ntasfi/PyGame-Learning-Environment

- OpenAI Gym: https://gym.openai.com

- gym-ple: https://github.com/lusob/gym-ple

- PyTorch: https://pytorch.org

- OpenCV: https://opencv.org

## Train an Agent

There are a number of arguments that main.py accepts, some of them are:

* --algo - the RL algorithm you want to run ("Baseline", "QLearning", "SARSA", etc.)
* --order - how the Q-table is updated ("backward" or "forward")
* --rounding - Discretization level (smaller means higher state space and thus longer convergence)
* --epsilon - Exploration rate (probability of choosing random action)
* --lr - Learning rate (coefficient of a target value in Q-values update equation)
* --discount - Discount factor (coefficient of the next state's Q-value in the update equation)
* --probFlap - Probability to choose action 1 when choosing random action

We run the experiment using **Q-Learning** agent with **backward** updates and exploration rate of **0**. Below is an example of how the experiment can be started.

```bash
python3 main.py --algo QLearning --probFlap 0.1 --rounding 50 --lr 0.8 --order backward --epsilon 0
```
You can tweak the parameters as you want, try different algorithms by replacing "QLearning" with an algorithm from ('Baseline' ,'QLearning', 'SARSA', 'FuncApproxLR', 'FuncApproxDNN', 'FuncApproxCNN').

## Original Authors

* **Tai Vu** - Stanford University

* **Leon Tran** - Stanford University
