import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import json
import os
from os import walk
import seaborn as sns
import pandas as pd
from datetime import datetime

def generate_boxplot(algo, rounding):
    if rounding == None:
        rounding = 1
    dirpath, _, filenames = next(walk("scores"))
    if not os.path.exists("boxplots"):
        os.mkdir("boxplots")
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
        # plot the boxplot for the iteration
        sns.boxplot(x=scores)
        # save figure
        plt.title(f"Boxplot for {algo} r{rounding}_iter{iter}")
        plt.savefig(f"boxplots/box_{iter}")
        plt.close()
    # plot the boxplot for the whole run and for the latest iteration
    sns.boxplot(x=scores_all)
    # save figure
    plt.title(f"Boxplot for {algo} r{rounding}_all iterations")
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
    plt.savefig(f"Box all {algo}_r{rounding}_{dt_string}")
    plt.close()