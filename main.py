import numpy as np
import matplotlib.pyplot as plt

#Analysis of a simple profit/loss strategy
print("""A strategy returns a profit of £120 with probability 0.45, 
and a loss of £80 with probability 0.55""")

#Sampling N applications of the strategy
def strategy(n):
    unifarray = random.uniform(0,1,n)
    PandL = np.where(unifarray<0.45, 120, -80)
    return PandL
random = np.random.default_rng()
Nvals = [10,100,1000,10000,100000]
print("(No. trades, mean, standard deviation)")
for i in Nvals:
    pnl = strategy(i)
    mean = np.mean(pnl)
    variance = np.var(pnl)
    print("(",i, mean, np.sqrt(variance),")")







