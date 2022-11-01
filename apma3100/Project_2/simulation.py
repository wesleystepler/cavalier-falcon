"""
Wesley Stepler - pws3ms
APMA 3100 - Probability Project 2
"""

import random
import math
import statistics
from matplotlib import pyplot as plt

# Run the simulation 
runs = 10000
results = []
for i in range(0, runs):
    done = False
    w = 0
    attempt = 0
    while not done:
        if attempt >= 4:
            results.append(w)
            break

        possibilities = ["busy", "unavailable", "available"]
        weights = (0.2, 0.3, 0.5)

        simulation = random.choices(possibilities, weights)
        #print(simulation)
        if simulation[0] == "busy":
            w += 12
            attempt += 1
            continue
            

        elif simulation[0] == "unavailable":
            w += 27
            attempt += 1
            continue
            

        elif simulation[0] == "available":
            w += 6
            x_range = range(0, 21)
            # This commented out chunk better simulates a continuous RV, but has minimal effect on the outcome and seriously slows down runtime.
            #x_range = []
            #j = 0
            #while j <= 20:
            #    x_range.append(j)
            #    j += 0.01
            x_weights = []
            for i in x_range:
                prob = (1/8)*math.e**(-(1/8)*i)
                x_weights.append(prob)
            y_range = range(30, 61)
            # This commented out chunk better simulates a continuous RV, but has minimal effect on the outcome and seriously slows down runtime.
            #y_range = []
            #j = 30
            #while j <= 60:
            #    y_range.append(j)
            #    j += 0.01
            y_weights = []
            for i in y_range:
                y_weights.append(i*0.00222)

            sim_x = random.choices(x_range, x_weights)
            sim_y = random.choices(y_range, y_weights)


            w += sim_x[0] + sim_y[0] + 1
            done = True
        if done:
            results.append(w)

print("Simulation results:")
print(results)
print(f" Shortest call: {min(results)}, Longest call: {max(results)}")
print(f"Expected Value for W: {sum(results)/len(results)}")
print(f"Median Value for W: {statistics.median(results)}")
print()

# Now get the estimated CDF for W
probabilities = []
step = 2
a = 25
b = 75
w_vals = [x * step for x in range(a, b)]
for i in range(0, len(w_vals)):
    count = 0
    for j in range(0, len(results)):
        if results[j] <= w_vals[i]:
            count += 1
    p = count/len(results)
    probabilities.append((w_vals[i], p))

print("Data to Estimate W's CDF:")
print(probabilities)

# Create a histogram for W
step = 2
a = 18
b = 84
hist_bins = [x * step for x in range(a, b)]
fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(results, bins = hist_bins)
 
# Show plot
#plt.show()
