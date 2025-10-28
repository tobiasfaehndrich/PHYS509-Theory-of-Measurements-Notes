'''The $\chi^{2}$ Distribution: Let $X_{i}$, $i=1, ..., n$ be n independent normal random variables with Gaussian p.d.f.s $N(\mu_{i},\sigma_{i}^{2})$.

	Define
	$$ \chi^{2}=\sum_{i=1}^{n}\left(\frac{x_{i}-\mu_{i}}{\sigma_{i}}\right)^{2} $$
	Then (you can take this as a given) the pdf for $\chi^{2}$ is
	$$ p(\chi^{2};n)=\frac{1}{2^{\frac{n}{2}}\Gamma(n/2)}(\chi^{2})^{\frac{n}{2}-1}e^{-\frac{1}{2}\chi^{2}} $$
	which is called the $\chi^{2}$ distribution with n degrees of freedom.
	\begin{enumerate}
		\item[(a)] Make plots of this for n=1, 2, 3 and 10.'''


import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
import scienceplots

plt.style.use(['science', 'notebook'])

n = [1, 2, 3, 10]
x_square = np.linspace(0, 15, 1000)

for i in range(len(n)):
    p_chi_square = (1/(2**(n[i]/2)*gamma(n[i]/2)))*(x_square**(n[i]/2-1))*np.exp(-x_square/2)
    plt.plot(x_square, p_chi_square, label=f'n={n[i]}')

plt.ylim(0, 1)
plt.xlabel(r'$\chi^{2}$')
plt.ylabel(r'$p(\chi^{2};n)$')
plt.legend()
plt.savefig('hw2-p9a.png', dpi=300)
plt.show()


