import numpy as np
data = np.loadtxt(fname = "C:\\Users\\1\\Documents\\text.txt")
truedata = data.astype(np.int)
print(truedata)
fuel = 0
for i in range(len(truedata)):
    while truedata[i] > 0:
        truedata[i] = (truedata[i] // 3) - 2
        if truedata[i] > 0:
            fuel += truedata[i]
            
print(fuel)