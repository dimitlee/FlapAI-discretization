# FlapAI-Bird - Discretization

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

We run the experiment using Q-Learning agent with backward updates and exploration rate of 0. Below is an example of how the experiment can be started.

- Q-Learning Agent.

```bash
python3 main.py --algo QLearning --probFlap 0.1 --rounding 50 --lr 0.8 --order backward --epsilon 0
```

## Original Authors

* **Tai Vu** - Stanford University

* **Leon Tran** - Stanford University
