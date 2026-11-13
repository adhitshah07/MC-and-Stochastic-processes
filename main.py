import numpy as np
import matplotlib.pyplot as plt

#Analysis of a simple profit/loss strategy
print("""A strategy returns a profit of £120 with probability 0.45, 
and a loss of £80 with probability 0.55""")

#Sampling N applications of the strategy
random = np.random.default_rng()
def strategy(n):
    unifarray = random.uniform(0,1,n)
    PandL = np.where(unifarray<0.45, 120, -80)
    return PandL

#Testing the strategy over N trades
Nvals = [10,100,1000,10000,100000]
print("(No. trades, mean, standard deviation)")
for i in Nvals:
    pnl = strategy(i)
    mean = np.mean(pnl)
    variance = np.var(pnl)
    print("(",i, mean, np.sqrt(variance),")")

x = np.arange(0,1000)
y = np.cumsum(strategy(1000))

plt.plot(x,y)
plt.xlabel("Trade number")
plt.ylabel("Cumulative Profit/Loss")
plt.title("Cumulative Profit/Loss across 1000 sampled trades of the strategy")
plt.ylim(-5000,10000)
plt.axhline(0)
plt.show()









