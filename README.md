Project 1: Monte Carlo & Stochastic Processes for trading

Using a simple trading strategy, a $£120$ profit is returned with probability $0.45$, and $£80$ loss with probability $0.55$. Let $X$ be the random variable associated with this strategy.
$$
X = 
\begin{cases}
120 &\qquad p = 0.45\\
-80 &\qquad p = 0.55
\end{cases}
$$

$$
E[X] = 120(0.45) - 80(0.55) = 10 
\\
Var[X] = E[(X-E[X])^2] = 0.45(110)^2 + 0.55(-90)^2 = 9900 \\
SD[X] = \sqrt{9900} \approx 99.50
$$

It is clear from the code results that, as we increase  the sampled number of trades, the values of sample mean and standard devation converge to these values. This is expected by the Law of Large Numbers.