# \subsection*{Problem 14 The Negative Binomial Distribution}
# \begin{quote}
# 	Suppose, instead of the usual binomial situation in which we fix the number of trials $n$ and ask how many successes $r$ we get, we reverse the problem: we keep performing trials until we get $r$ successes and ask how many trials $n$ we had to make.
# 	\begin{enumerate}[label=(\alph*)]
# 		\item Generalize the argument for the geometric distribution to show that the probability that the $r$th success is on the $n$th trial is given by the negative binomial distribution
# 		      \[
# 			      P_r(n;p) = {n-1 \choose r-1}\, p^r (1-p)^{n-r}, \qquad n=r, r+1,\ldots
# 		      \]

# 		\item Show that the mean and variance of this distribution are
# 		      \[
# 			      E(n)=\frac{r}{p}, \qquad V(n)=\frac{r(1-p)}{p^2}.
# 		      \]
# 		\item Make a plot of this distribution for $p=0.4,\ r=10$ and for $p=0.6,\ r=5$.
# 	\end{enumerate}

import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from scipy.special import comb

plt.style.use(['science', 'notebook'])

cases = [(0.4, 10), (0.6, 5)]  # (p, r) pairs

plt.figure(figsize=(10, 5))

for i, (p, r) in enumerate(cases, start=1):
    n = np.arange(r, 60)  # number of trials
    P_r = comb(n-1, r-1) * (p**r) * ((1-p)**(n-r))  # negative binomial distribution
    P_r /= np.sum(P_r)  # normalize for plotting

    plt.subplot(1, 2, i)
    plt.bar(n, P_r, alpha=0.7, label=f'p={p}, r={r}')
    plt.xlabel('Number of Trials (n)')
    plt.ylabel('Probability')
    plt.legend()

path = 'C:/Users/tobia/Documents/ubc-grad/PHYS509-UBC-TheoryofMeasurements-notes/homework-problems/problem-set-1/'
plt.tight_layout()
plt.savefig(f'{path}set1-p14c.png')
plt.show()

