from TimingAttackModule import *
import numpy as np

def main():
    ta = TimingAttack()
    d = [1]
    for i in range(1,64):
          
        variance = generateObservations(d,ta)
        if variance[0] < variance[1]:
            d.append(0)
        else:
            d.append(1)
    print(d)
    ta.test(d)

def generateObservations(d:list[int],ta:TimingAttack)->np.array:
    observations0 = []
    observations1 = []
    
    for _ in range(2000):
        c = np.random.randint(0,(2**62-1))
        realTime = ta.victimdevice(c)
        d.append(0)
        observations0.append(realTime - ta.attackerdevice(c,d))
        del d[-1]
        d.append(1)
        observations1.append(realTime - ta.attackerdevice(c,d))
        del d[-1]
    var0 = np.array(observations0)
    var1 = np.array(observations1)
    return [np.var(var0),np.var(var1)]

    
if __name__ == "__main__":
    main()