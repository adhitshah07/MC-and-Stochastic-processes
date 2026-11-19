import numpy as np
import matplotlib.pyplot as plt

##Analysis of a simple profit/loss strategy
print("""A strategy returns a profit of £120 with probability 0.45, 
and a loss of £80 with probability 0.55""")
a1 = 120
b1 = -80
p1 = 0.45

Exp = a1*p1 + b1*(1-p1)
Var = ((a1)**2)*p1 + ((b1)**2)*(1-p1) - Exp**2
Std = np.sqrt(Var)
##Sampling N applications of the strategy
random = np.random.default_rng(22718)

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
    pnl = strategy(a1,b1,i,p1)[0]
    mean = np.mean(pnl)
    variance = np.var(pnl)
    print("(",i, mean, np.sqrt(variance),")")

##Finding and plotting a cumulative sum of 1000 trade outcomes
x = np.arange(1,1001)
y = np.cumsum(st80120[0])
pnlExp = st80120[1]


plt.plot(x,y, color = "blue",label = "Simulated P&L")
plt.plot(x,pnlExp*x,color = "red",label = "Expected cumulative P&L")
plt.xlabel("Trade number")
plt.xlim(1,1100)
plt.ylabel("Cumulative Profit/Loss")
plt.title("Cumulative Profit/Loss across 1000 sampled trades of the strategy")
plt.legend()
plt.tight_layout()
plt.show()

##Simulating multiple possible trading paths
PSize = 1000
PNo = 10000
MExp = Exp*PSize
MVar = Var*PSize
MultiUnif = random.uniform(0,1,(PNo,PSize))
MultiPnL = np.where(MultiUnif<p1, a1, b1)
EndPnL = np.sum(MultiPnL, axis = 1)

##Analysis of the distrubition of final outcomes of the trading paths
print("Consider a path of 1000 trades simulated 10 000 times")
print(f"""
--------------------------------------------------
Theoretical calculations:

Expected value for n trades = {Exp}n = {Exp}*{PSize} = {MExp}

Variance for n trades = {Var}n = {Var} * {PSize} = {MVar}

Standard Deviation = ({Var}n)^0.5 = ({MVar})^0.5 = approx. {np.sqrt(MVar):,.2f}
""")
MeanEnd = np.mean(EndPnL)
VarEnd = np.var(EndPnL)
StdEnd = np.std(EndPnL)
LossEnd = np.mean(EndPnL<0)
print(f"""
--------------------------------------------------
Analysis of n = {PNo} paths:

Sample mean outcome: £{MeanEnd:,.2f}
Sample standard deviation of outcomes: £{StdEnd:,.2f}
Estimated probability of ending in a loss: {LossEnd:.2%}

Ratio of sample mean and expectation: {MeanEnd/MExp:,.4f}
Simulated SD/TheoreticalSD: {StdEnd/np.sqrt(MVar):,.4f}
""")
Perc5 = np.percentile(EndPnL, 5)
Perc95 = np.percentile(EndPnL, 95)
Perc50 = np.percentile(EndPnL, 50)


##Histogram Plot and percentile analysis
plt.hist(EndPnL, bins = 50)
plt.title("Distribution of path outcomes")
plt.xlabel("Final P&L(£)")
plt.ylabel("No. simulated paths")
plt.axvline(Perc5, color = "red", label = "5th percentile")
plt.axvline(Perc50, color = "blue", label = "Median")
plt.axvline(Perc95, color = "green", label = "95th percentile")
plt.legend()
plt.tight_layout()
plt.show()
print(f"""
Histogram analysis:

5th percentile: £{Perc5:,.2f}
50th percentile: £{Perc50:,.2f}
95th percentile: £{Perc95:,.2f}
--------------------------------------------------
""")

##Getting sample S&P 500 data and rebuilding its path

levels = np.genfromtxt("SP500.csv",delimiter=",",skip_header=1,usecols=1,)
levels = levels[~np.isnan(levels)]

returns = (levels[1:]/levels[:-1] -1)
spmean  = np.mean(returns)
spsd = np.std(returns, ddof = 1)
levels_rebuilt = levels[0]*np.cumprod(1+returns)


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
print(f"""
S&P 500 Sampling summary:

No. paths sampled: {SPno}
Horizon: {SPSize}

Probability of making a loss: {p_losslevels:,.2%}
5th percentile of return: {sp5:,.2%}
50th percentile: {sp50:,.2%}
95th percentile: {sp95:,.2%}

-------------------------------------
""")

#Plotting a random selection of 20 S&P paths


samplepaths = random.choice(simulatedlevels.shape[0], size=20, replace=False)

x_sp = np.arange(1,SPSize + 1)
for i in range(20):
    y_sp = simulatedlevels[samplepaths[i],:]
    plt.plot(x_sp,y_sp)
plt.axhline(levels[-1], color="black", linestyle="--", label = "Starting level")
plt.xlabel("Trading day")
plt.ylabel("Index Level")
plt.title("20 simulated S&P 500 paths over 252 trading days")
plt.legend()
plt.tight_layout()
plt.show()