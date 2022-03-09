#Getting the positions (indexes) where elements of 2 numpy arrays match
import numpy as np
l1=[]
l2=[]
size=int(input("Enter the length of array : "))
print("For array 1")
for i in range(size):
    x=int(input("Enter element : "))
    l1.append(x)
print("For array 2")
for i in range(size):
    x=int(input("Enter element : "))
    l2.append(x)
    
a=np.array(l1)
b=np.array(l2)
x=np.where(a==b)

print("Matching indexes :")
for i in x:
    print(i)
print()
