import numpy as np
import matplotlib.pyplot as plt

#Analysis of a simple profit/loss strategy
print("""A strategy returns a profit of £120 with probability 0.45, 
and a loss of £80 with probability 0.55""")

#Sampling N applications of the strategy
random = np.random.default_rng()
Nvals = [10,100,1000,10000,100000]
for i in Nvals:
    unifarray = random.uniform(0,1,i)
    print("Number of trades = " , i)
    PandL = np.where(unifarray < 0.45, 120, -80)
    print("Mean profit/loss = ", np.mean(PandL))
    print("Standard deviation = ",np.sqrt(np.var(PandL)))






