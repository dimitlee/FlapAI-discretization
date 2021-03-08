import json
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def generate_graph(algo, rounding, numTrainIters, interval):
    if rounding == None:
        rounding = 1
    iter = interval
    maxScore = [0]
    avgScore = [0]
    stdev = [0]
    x = [0]
    while iter <= numTrainIters:
        # Open json file with scores
        with open(f'scores/scores_{iter}.json') as f:
            data = json.load(f)

        # Put all data into a simple list
        data_list = []
        for key in data:
            for i in range(data[key]):
                data_list.append(int(key))

        # Put max, avg and stdev into lists
        maxScore.append(np.amax(data_list))
        avgScore.append(np.mean(data_list))
        stdev.append(pow(np.var(data_list), 0.5))
        x.append(iter)

        # Repeat for next Testing phase
        iter += interval


    plt.plot(x, maxScore, label="Max Score")
    plt.plot(x, avgScore, label="Avg Score")
    print(maxScore)
    print(avgScore)

    plt.ylabel("Score")
    plt.xlabel("Iteration")

    plt.legend()
    plt.title(f"{algo}_{rounding}")

    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
    plt.savefig(f"MaxAvg_{algo}_{rounding}_{dt_string}.png")
    plt.close()

    plt.plot(x, stdev, label="Standard Deviation")

    plt.ylabel("Standard deviation")
    plt.xlabel("Iteration")

    plt.legend()

    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
    plt.savefig(f"Stdev_{algo}_{rounding}_{dt_string}.png")
    plt.close()
