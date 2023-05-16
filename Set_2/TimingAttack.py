from TimingAttackModule import *
import numpy as np

def main():
    ta = TimingAttack()
    d = [1]
    for i in range(1,63):
        c = np.random.randint(0,(2**61 - 1))    
        d.append(1)
        observations = generateObservations(d,ta,c)
        var1 = np.var(observations)
        del d[-1]
        d.append(0)
        observations = generateObservations(d,ta,c)
        var0 = np.var(observations)
        del d[-1]
        if var1 < var0:
            d.append(1)
        else:
            d.append(0)
    print(d)
    ta.test(d)

def generateObservations(d:list[int],ta:TimingAttack,c:int)->np.array:
    observations = []
    realTime = ta.victimdevice(c)
    for _ in range(100):
        observations.append(realTime - ta.attackerdevice(c,d))
    return np.array(observations)

    
if __name__ == "__main__":
    main()