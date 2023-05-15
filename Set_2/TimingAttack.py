from TimingAttackModule import *
import numpy as np

def main():
    ta = TimingAttack()
    c = np.random.randint(0,2**16)
    d = [1]
    
    for i in range(1,63):
        d.append(1)
        observations = simulateVictim(d,ta,c)
        varianza1 = calculateVariance(observations)
        del d[-1]
        d.append(0)
        observations = simulateVictim(d,ta,c)
        varianza0 = calculateVariance(observations)
        del d[-1]
        if varianza1 < varianza0:
            d.append(1)
        else:
            d.append(0)
    print(d)
    print(len(d))
    ta.test(d)

def simulateVictim(d:list[int],ta:TimingAttack,c:int)->np.array:
    observations = []
    for i in range(100):
        observations.append(ta.attackerdevice(c,d))
    return np.array(observations)

def calculateVariance(observations:np.array)->float:
    return np.var(observations)
    
    



if __name__ == "__main__":
    main()