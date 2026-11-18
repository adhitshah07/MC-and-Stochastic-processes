import numpy as np
import matplotlib.pyplot as plt

##Analysis of a simple profit/loss strategy
print("""A strategy returns a profit of £120 with probability 0.45, 
and a loss of £80 with probability 0.55""")

##Sampling N applications of the strategy
random = np.random.default_rng(42)

def strategy(a,b,n,p):
    unifarray = random.uniform(0,1,n)
    PandL = np.where(unifarray<p, a, b)
    Expectation = a*p + b*(1-p)
    return PandL, Expectation
st80120 = strategy(120,-80,1000,0.45)
##Testing the strategy over N trades
Nvals = [10,100,1000,10000,100000]
print("(No. trades, mean, standard deviation)")
for i in Nvals:
    pnl = strategy(120,-80,i,0.45)[0]
    mean = np.mean(pnl)
    variance = np.var(pnl)
    print("(",i, mean, np.sqrt(variance),")")

##Finding and plotting a cumulative sum of 1000 trade outcomes
x = np.arange(1,1001)
y = np.cumsum(st80120[0])
pnlExp = st80120[1]


plt.plot(x,y, color = "blue",label = "Simulated P&L")
plt.plot(x,pnlExp*x,color = "red",label = "Theoretical P&L")
plt.xlabel("Trade number")
plt.xlim(1,1100)
plt.ylabel("Cumulative Profit/Loss")
plt.title("Cumulative Profit/Loss across 1000 sampled trades of the strategy")
plt.legend()
plt.show()

##Simulating multiple possible trading paths
PSize = 1000
PNo = 10000
MultiUnif = np.random.uniform(0,1,(PNo,PSize))
MultiPnL = np.where(MultiUnif<0.45, 120, -80)
EndPnL = np.sum(MultiPnL, axis = 1)

##Analysis of the distrubition of final outcomes of the trading paths
print("Consider a path of 1000 trades simulated 10 000 times")
print("""
--------------------------------------------------
Theoretical calculations:

Expected value for n trades = 10n = 10*1000 = 10000

Variance for n trades = 9900n = 9900 * 1000 = 990000

Standard Deviation = (9900n)^0.5 = (9900000)^0.5 = approx. 3146.43

--------------------------------------------------
""")
MeanEnd = np.mean(EndPnL)
VarEnd = np.var(EndPnL)
StdEnd = np.std(EndPnL)
LossEnd = np.mean(EndPnL<0)
print("Sample mean outcome:", MeanEnd)
print("Sample standard deviation of outcomes:", StdEnd)
print("Number of paths that ended in a loss:", LossEnd)
print("Estimated Probability of ending in a loss:", LossEnd)
Perc5 = np.percentile(EndPnL, 5)
Perc95 = np.percentile(EndPnL, 95)
Perc50 = np.percentile(EndPnL, 50)
##Histogram Plot and percentile analysis
plt.hist(EndPnL, bins = 50)
plt.title("Distribution of path outcomes")
plt.axvline(Perc5, color = "red", label = "5th percentile")
plt.axvline(Perc50, color = "blue", label = "Median")
plt.axvline(Perc95, color = "green", label = "95th percentile")
plt.legend()
plt.show()
print("5th, 50th and 95th percentiles:", Perc5, Perc50, Perc95)

##Getting sample S&P 500 data and rebuilding its path

levels = np.genfromtxt("SP500.csv",delimiter=",",skip_header=1,usecols=1,)
levels = levels[~np.isnan(levels)]

returns = (levels[1:]/levels[:-1] -1)
spmean  = np.mean(returns)
spsd = np.std(returns, ddof = 1)
levels_rebuilt = levels[0]*np.cumprod(1+returns)


#print(np.allclose(levels_rebuilt, levels[1:]))     #(sanity check)

##Sampling S%P 500 data to predict multiple paths
SPno = 10000
SPSize = 252
samplereturns = random.choice(returns, size = (SPno, SPSize), replace = True) 
simulatedlevels = levels[-1]*np.cumprod(1 + samplereturns, axis = 1)

p_losslevels = np.mean(simulatedlevels[:,-1] <levels[-1])
totalreturn = simulatedlevels[:,-1]/levels[-1] - 1
sp5 = np.percentile(totalreturn, 5)
sp50 = np.percentile(totalreturn, 50)
sp95 = np.percentile(totalreturn, 95)
print(sp5, sp50, sp95)

#Plotting a random selection of five S&P paths

