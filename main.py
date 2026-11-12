import numpy as np
import matplotlib.pyplot as plt

# #Analysis of a simple profit/loss strategy
random = np.random.default_rng()
# unifarray = [] 
# for i in range(100):
#     unifarray.append(random.random())
# print(unifarray)
unifarray = random.uniform(0,1,100)
print(np.mean(unifarray < 0.45))