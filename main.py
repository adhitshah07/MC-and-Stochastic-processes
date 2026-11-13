import numpy as np
import matplotlib.pyplot as plt

#Analysis of a simple profit/loss strategy
print("""A strategy returns a profit of £120 with probability 0.45, 
and a loss of £80 with probability 0.55""")

#Sampling N applications of the strategy
random = np.random.default_rng()

def strategy(a,b,n,p):
    unifarray = random.uniform(0,1,n)
    PandL = np.where(unifarray<p, a, b)
    Expectation = a*p + b*(1-p)
    return PandL, Expectation

#Testing the strategy over N trades
Nvals = [10,100,1000,10000,100000]
print("(No. trades, mean, standard deviation)")
for i in Nvals:
    pnl = strategy(120,-80,i,0.45)[0]
    mean = np.mean(pnl)
    variance = np.var(pnl)
    print("(",i, mean, np.sqrt(variance),")")

x = np.arange(1,1001)
y = np.cumsum(strategy(120,-80,1000,0.45)[0])
pnlExp = strategy(120,-80,1000,0.45)[1]


plt.plot(x,y, color = "blue",label = "Simulated P&L")
plt.plot(x,pnlExp*x,color = "red",label = "Theoretical P&L")
plt.xlabel("Trade number")
plt.xlim(1,1100)
plt.ylabel("Cumulative Profit/Loss")
plt.title("Cumulative Profit/Loss across 1000 sampled trades of the strategy")
plt.legend()
plt.show()









