# '''Consider a Bernoulli process with probability of success in each trial being $p$.
# 	\begin{enumerate}[label=(\alph*)]
# 		\item Show that the probability that the first success occurs on the $n$th trial is given by the geometric distribution
# 		      \[
# 			      P_1(n;p) = p\,(1-p)^{n-1}.
# 		      \]
# 		      Verify that this gives a properly normalized set of probabilities, i.e.,
# 		      \[
# 			      \sum_{n=1}^{\infty} P_1(n;p) = 1.
# 		      \]
# 		\item Show that the mean and variance of this distribution are
# 		      \[
# 			      E(r)=\frac{1}{p}, \qquad V(r)=\frac{1-p}{p^2}.
# 		      \]
# 		\item Make a plot of this distribution for $p=0.4$.
# 	\end{enumerate} '''

import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'notebook'])

p = 0.4  # probability of success
n = np.arange(1, 19)  # number of trials
P1 = p * (1 - p) ** (n - 1)  # geometric distribution
P1 /= np.sum(P1)  # normalize probabilities

plt.bar(n, P1, label='Geometric Distribution (p=0.4)')
plt.xlabel('Number of Trials (n)')
plt.ylabel('Probability')
plt.legend()



path = 'C:/Users/tobia/Documents/ubc-grad/PHYS509-UBC-TheoryofMeasurements-notes/homework-problems/problem-set-1/'
plt.savefig(f'{path}set1-p13c.png')
plt.show()
