import numpy,sys
#sys.setrecursionlimit(250)
#Flip Coin Number of Ways 
coinsInBag = [0.01,0.05,0.1,0.25,0.5]
def numberOfWays(target):
    if (target < 0):
        return 0
    elif(target == 0):
        return 1
    else:
        return numpy.mean([numberOfWays(target - coin) for coin in coinsInBag])

print ((numberOfWays(1)))

