#Making new vector with 5 consecutive zeros interleaved between each value
import numpy as np 
a=[]
b=[]

x1=int(input("Enter starting number : "))
x2=int(input("Enter ending number : "))
for i in range (x1,x2+1):
    a.append(i)

a1=np.array(a)
print("Before :")
print(a1)

z=5 #number of zeros
temp=np.zeros(len(a)+(len(a)-1)*(z))
temp[::z+1] = a
print("After :")
print(np.floor(temp))
