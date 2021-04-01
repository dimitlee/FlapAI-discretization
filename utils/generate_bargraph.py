import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import json
import os
from os import walk
from datetime import datetime

def generate_bargraph(algo, rounding):
    if rounding == None:
        rounding = 1
    dirpath, _, filenames = next(walk("scores"))
    if not os.path.exists("bargraphs"):
        os.mkdir("bargraphs")
    # array for recording all scores from every iteration
    scores_all = []
    for filename in filenames:
        iter = filename.split("_")[1]
        iter = iter.split(".")[0]

        # open the file with scores
        with open(f'{dirpath}/{filename}') as f:
            data = json.load(f)
        # put scores into the array
        scores = []
        for key in data:
            for i in range(data[key]):
                scores_all.append(int(key))
                scores.append(int(key))
        # plot the bargraph for the iteration
        plt.hist(scores, bins=50, weights=np.ones(len(scores)) / len(scores))
        # save figure
        plt.title(f"Bargraph for {algo} r{rounding}_iter{iter}")
        plt.savefig(f"bargraphs/bargraph_{iter}")
        plt.close()
    # plot the bargraph for the whole run and for the latest iteration
    plt.hist(scores_all, bins=50, weights=np.ones(len(scores_all)) / len(scores_all))
    # save figure
    plt.title(f"Bargraph for {algo} r{rounding}_all iterations")
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
    plt.savefig(f"Bargraph all {algo}_r{rounding}_{dt_string}")
    plt.close()