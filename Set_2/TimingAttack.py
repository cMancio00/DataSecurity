from TimingAttackModule import *
import numpy as np

def main():
    ta = TimingAttack()
    exponent = [1]
    for _ in range(1,64):
        variance = generateObservations(exponent,ta)
        if variance[0] < variance[1]:
            exponent.append(0)
        else:
            exponent.append(1)
    print(exponent)
    ta.test(exponent)

def generateObservations(exponent:list[int],ta:TimingAttack)->list[int]:
    observations0 = []
    observations1 = []
    for _ in range(2000):
        chipertext = np.random.randint(0,(2**62-1))
        realTime = ta.victimdevice(chipertext)
        observations0.append(trybit(0,ta,exponent,realTime,chipertext))
        observations1.append(trybit(1,ta,exponent,realTime,chipertext))
    var0 = np.array(observations0)
    var1 = np.array(observations1)
    return [np.var(var0),np.var(var1)]

def trybit(bit:int,ta:TimingAttack,exponent:int,realTime:int,chipertext:int)->int:
    exponent.append(bit)
    observation = realTime - ta.attackerdevice(chipertext,exponent)
    del exponent[-1]
    return observation

    
if __name__ == "__main__":
    main()