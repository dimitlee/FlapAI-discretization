# Study of the Impact of Discretization in RL: Tradeoff Between Convergence and Final Performance in Huge State Spaces

This repository borrows code from https://github.com/taivu1998/FlapAI-Bird for reproduction of their Reinforcement Learning Experiment in Flappy-Bird environment. In our experiment we are focusing on discretization feature in order to find the balance between convergence and final performance. You can also look at the report of our reproduction: https://drive.google.com/file/d/1vbh8JXSwGYI8TdeiTGPt1x0vrCPgWuq4/view?usp=sharing


## Installation

Before installing PyGame library go to [link](https://www.pygame.org/wiki/Compilation) choose your operating system and follow the instructions to install the required dependencies for PyGame.

To install PyGame run:
```bash
pip install pygame==1.9.6
```
 
Gym:
```bash
pip install gym==0.15.4
```
 
Torch, torchvision and torchaudio:
```bash
!pip install torch==1.5.0 torchvision==0.6.0 -f https://download.pytorch.org/whl/torch_stable.html
```
 
Gym-ple:
```
pip install gym-ple
```
 
PLE:
```bash
git clone https://github.com/ntasfi/PyGame-Learning-Environment.git
cd PyGame-Learning-Environment
pip install -e .
```

MatPlotLib:
```
pip install matplotlib
```

Seaborn:
```
pip install seaborn
```

## Train an Agent

There are a number of arguments that main.py accepts, some of them are:

* **--algo** - the RL algorithm you want to run ("Baseline", "QLearning", "SARSA", etc.)
* **--order** - how the Q-table is updated ("backward" or "forward")
* **--rounding** - Discretization level (smaller means higher state space and thus longer convergence)
* **--epsilon** - Exploration rate (probability of choosing random action)
* **--lr** - Learning rate (coefficient of a target value in Q-values update equation)
* **--discount** - Discount factor (coefficient of the next state's Q-value in the update equation)
* **--probFlap** - Probability to choose action 1 when choosing random action

We run the experiment using **Q-Learning** agent with **backward** updates and exploration rate of **0**.
To run the **50x50** d.l. experiment run the following line:
```bash
python3 main.py --algo QLearning --probFlap 0.1 --rounding 50 --lr 0.8 --order backward --epsilon 0
```
For **20x20** run:
```bash
python3 main.py --algo QLearning --probFlap 0.1 --rounding 20 --lr 0.8 --order backward --epsilon 0
```
For **10x10** run:
```bash
python3 main.py --algo QLearning --probFlap 0.1 --rounding 10 --lr 0.8 --order backward --epsilon 0
```

You can tweak the parameters as you want, try **forward** update order by running:
```bash
python3 main.py --algo QLearning --probFlap 0.1 --rounding 10 --lr 0.8 --order forward --epsilon 0
```

You can also run other agents, for instance **SARSA**:
```bash
python3 main.py --algo SARSA --probFlap 0.1 --rounding 10 --lr 0.8 --order forward --epsilon 0
```

Or you can try different **exploration rate**:
```bash
python3 main.py --algo QLearning --probFlap 0.1 --rounding 10 --lr 0.8 --order forward --epsilon 0.1
```

The training process takes several days, assuming the max score is high enough (~1000), so you can stop the program at any time, since the program saves the Q-values as json files. Then you can continue the training by specifying the iteration from which to start training (Q-values are saved at each testing phase, so it should be a multiple of 250, or other number if you changed evalPerIter value). The program will load the corresponding Q-value and continue from this iteration.

For example if you stopped at iteration 2500, run the following line to continue the experiment:
```bash
python3 main.py --algo QLearning --probFlap 0.1 --rounding 50 --lr 0.8 --order backward --epsilon 0 --startIter 2500
```

## Evaluating performance

After some time (250 iterations by default) algorithms start a testing phase, during which scores (number of tubes passed) are recorded and then written into a json file, where the name of the file represents at which iteration the testing began. You can generate graphs of maximum score and average score over several such testing phases. Below is an example of how you can do that in console:

```bash
python graph.py --algo QLearning --rounding 50
```

You can also see the distribution of scores by generating boxplots and barcharts. The code will generate these graphs for each testing phase and for the whole run.

```bash
python boxplot.py --algo QLearning --rounding 50
```

```bash
python bargraph.py --algo QLearning --rounding 50
```

## Original Authors

* **Tai Vu** - Stanford University

* **Leon Tran** - Stanford University
