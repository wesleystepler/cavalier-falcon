import random
import matplotlib.pyplot as plt
import math

# Initializes data needed for question 3
x_range = range(1, 301)
x_weights = []
for i in x_range:
    prob = (1/3249)*i*math.e**((-0.5)*(1/3249)*(i**2))
    x_weights.append(prob)

big_list = []
def sample_mean(n, x_range, x_weights):
    global big_list
    sample_means =[]
    for i in range(0, 10000):
        m10 = []
        for j in range(0, n):
            sim_x = random.choices(x_range, x_weights)
            m10.append(sim_x[0])
        s = sum(m10)
        sample_mean = s/n
        big_list.append(sample_mean)
        #print(sample_mean)
        sample_means.append(sample_mean)

    return sample_means


def three_a():
    """Run this code to get the histograms for question 3a.
    Change the first parameter in sample_mean to desired n value"""
    sample_mean(10, x_range, x_weights)
    # Create a histogram
    step = 2
    a = 0
    b = 301
    hist_bins = [x * step for x in range(a,b)]
    fig, ax = plt.subplots(figsize =(10, 7))
    ax.hist(big_list, bins = hist_bins)

    # Show plot
    plt.show()

def three_b():
    estimated_params = {}
    probs = {}
    """Run this function for question 3b"""
    n_vals = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
    #n_vals = [2]
    samples = []
    MAD = []
    for n in n_vals:
        probs[f"P[Z{n}]"] = []
        probs[f"True Normal Z{n}"] = []
        z_vals = []
        print(f"Running on n = {n}...")
        run = sample_mean(n, x_range, x_weights)
        samples.append(run)
        # Estimate expected value and variance
        exp_val = sum(run)/len(run)
        var = 0
        for m in run:
            var += (m - exp_val)**2
        var /= 10000
        estimated_params[f"Expected value for n= {n}"] = exp_val
        estimated_params[f"Variance for n = {n}"] = var
        for m in run:
            # Calculate normal CDF from data
            z_neg_14 = 0
            z_neg_1 = 0
            z_neg_5 = 0
            z_0 = 0
            z_5 = 0
            z_1 = 0
            z_14 = 0

            zn_neg_14 = 0
            zn_neg_1 = 0
            zn_neg_5 = 0
            zn_0 = 0
            zn_5 = 0
            zn_1 = 0
            zn_14 = 0
            z = (m - exp_val)/(math.sqrt(var)/math.sqrt(n))
            zn = (m - 71.4389)/(37.34277/math.sqrt(n))
            z_vals.append(z)
            if z <= -1.4:
                z_neg_14 += 1
            if z <= -1:
                z_neg_1 += 1
            if z <= -0.5:
                z_neg_5 += 1
            if z <= 0:
                z_0 += 1
            if z <= 0.5:
                z_5 += 1
            if z <= 1:
                z_1 += 1
            if z <= 1.4:
                z_14 += 1

            if zn <= -1.4:
                zn_neg_14 += 1
            if zn <= -1:
                zn_neg_1 += 1
            if zn <= -0.5:
                zn_neg_5 += 1
            if zn <= 0:
                zn_0 += 1
            if zn <= 0.5:
                zn_5 += 1
            if zn <= 1:
                zn_1 += 1
            if zn <= 1.4:
                zn_14 += 1

        probs[f"P[Z{n}]"].append(z_neg_14/n)
        probs[f"P[Z{n}]"].append(z_neg_1 / n)
        probs[f"P[Z{n}]"].append(z_neg_5 / n)
        probs[f"P[Z{n}]"].append(z_0 / n)
        probs[f"P[Z{n}]"].append(z_5 / n)
        probs[f"P[Z{n}]"].append(z_1 / n)
        probs[f"P[Z{n}]"].append(z_14 / n)

        probs[f"True Normal Z{n}"].append(zn_neg_14/n)
        probs[f"True Normal Z{n}"].append(zn_neg_1 / n)
        probs[f"True Normal Z{n}"].append(zn_neg_5 / n)
        probs[f"True Normal Z{n}"].append(zn_0 / n)
        probs[f"True Normal Z{n}"].append(zn_5 / n)
        probs[f"True Normal Z{n}"].append(zn_1 / n)
        probs[f"True Normal Z{n}"].append(zn_14 / n)

        for p in range(0, len(probs[f"P[Z{n}]"])):
            diffs = []
            diffs.append(abs(probs[f"P[Z{n}]"][p] - probs[f"True Normal Z{n}"][p]))
        MAD.append(max(diffs))


    #print(exp_val)
    #print(var)
    #print(estimated_params)
    #print(probs)

    # Graph the MAD values vs. the n values
    x_axis = n_vals
    y_axis = MAD

    print(x_axis)
    print(y_axis)

    plt.plot(x_axis, y_axis)
    plt.xlabel('n Values')
    plt.ylabel('MAD Values')
    plt.show()


# Uncomment the function of the question you want to run
# three_a()
three_b()
