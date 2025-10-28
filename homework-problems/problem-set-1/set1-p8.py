# 	Write a program to simulate an experiment which has 100 
# independent Bernoulli trials, each with probability $p=0.2$
#  of success. That is, this pseudo-experiment has some random 
# number of successes, with expected mean 20. Now write 
# another loop that runs this pseudo-experiment $N$ times. 
# Make a histogram of the pseudo-experiment results when 
# $N=100$. Overlay a histogram of the Binomial distribution, 
# suitably normalized to the number of entries $N$. Repeat for 
# $N=1000$ and $N=100000$.

import numpy as np
import matplotlib.pyplot as plt

n = 100  # number of Bernoulli trials
p = 0.2  # probability of success
mu_expected = n * p  # expected mean

N_vals = [100, 1000, 100000]  # number of pseudo-experiments

# plot 3 histograms in a row on the same figure
plt.figure(figsize=(15, 5))

for N in N_vals:
    results = []
    for i in range(N):
        results.append(np.random.binomial(n, p))
    plt.subplot(1, 3, N_vals.index(N) + 1)
    plt.hist(results,bins=np.arange(-0.5, n+1.5, 1), density=True, alpha=0.5, label=f'Simulation (N={N})')
    # overlay histogram of binomial distribution, normalized to N:
    plt.hist(np.random.binomial(n, p, size=100000), bins=np.arange(-0.5, n+1.5, 1),density=True, alpha=0.5, label='Binomial Distribution')
    plt.xlabel('Number of Successes')
    plt.ylabel('Probability')
    plt.legend()


path = 'C:/Users/tobia/Documents/ubc-grad/PHYS509-UBC-TheoryofMeasurements-notes/homework-problems/problem-set-1/'
plt.savefig(f'{path}set1-p8.png')
plt.show()
