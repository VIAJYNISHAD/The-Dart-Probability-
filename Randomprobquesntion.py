import random 
from array import*
import numpy as np
import math
import matplotlib.pyplot as plt

def probablity(N):
    def distance(P):
        x=math.sqrt(P[0]**2+P[1]**2)
        return x

    S=[]
    for i in range(2*N):
        S.append(random.randint(0, 10))

    S=np.array(S)
    S=S.reshape(N,2)
    d=[]
    for i in range(N):
        d.append(distance(S[i]))

    sum1=0
    sum2=0
    sum3=0
    for i in range(N):
        if d[i]<=5:
            sum1=sum1+1
        else:
            sum3=sum3+1

    return (sum1/N)*100
Num=[]
N=[]
A=[]
B=[]
I=50
#50 points!
P=(3.14*5*5)/(20*20);
for i in range(1,I):
    Num.append(probablity(i))

for i in range(1,I):
    N.append(i)

for i in range(1,I):
    A.append(P*100)

total=0             
for x in Num:
    total=total+x

T=total/I
for i in range(1,I):
    B.append(T)

plt.plot(N,Num)
plt.plot(N,B)
plt.plot(N,A)
plt.legend(['Probablity of Random points vs Number of times point pick','Mean Probablity line','Area ratio of circle to square'])
plt.show()