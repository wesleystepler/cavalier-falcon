import random
import math
import matplotlib.pyplot as plt
import numpy as np

def CDF(x):
    result = 1 - (2.718281828459045)**((-0.5)*(1/3249)*(x**2))
    return result


# Generate 250 values of the sample mean for different values of n
# This code completes questions 2a and 2b
x_range = range(1, 301)
x_weights = []
for i in x_range:
    prob = (1/3249)*i*math.e**((-0.5)*(1/3249)*(i**2))
    x_weights.append(prob)

big_list = []
def sample_mean(n, x_range, x_weights):
    global big_list
    sample_means =[]
    for j in range(0, 250):
        m10 = []
        for k in range(0, n):
            sim_x = random.choices(x_range, x_weights)
            m10.append(sim_x[0])
        s = sum(m10)
        sm = s/n
        big_list.append(sample_mean)
        #print(sm)
        sample_means.append(sm)

    return sample_means


def two_c():
    """Run this function for question 2c"""
    sample_mean(10, x_range, x_weights)
    sample_mean(30, x_range, x_weights)
    sample_mean(50, x_range, x_weights)
    sample_mean(100, x_range, x_weights)
    sample_mean(250, x_range, x_weights)
    sample_mean(500, x_range, x_weights)
    sample_mean(1000, x_range, x_weights)

    print(big_list)

    n_vals = [10]*250 + [30]*250 + [50]*250 + [100]*250 +[250]*250 +[500]*250 +[1000]*250

    # Source: https://stackoverflow.com/questions/33382619/plot-a-horizontal-line-on-a-given-plot
    x = np.linspace(1, 21, 200)
    y = np.exp(-x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.hlines(y=71.4389, xmin=0, xmax=1100, linewidth=2, color='r')

    plt.scatter(n_vals, big_list)
    plt.show()

def two_e():
    """Use this function for question 2e"""
    test = sample_mean(300, x_range, x_weights)
    e = 0
    for num in test:
        if num > 77.4389 or num < 65.4389:
            e += 1
    error = e / len(test)
    if error > 0.01:
        print("Reject")
    else:
        print("Accept")


# Uncomment the function of the question you want to run
# two_c()
# two_e()