#Checking if 2 random arrays are equal
import numpy as np

a=[]
b=[]
size=int(input("Enter array's size : "))

print("For array 1")
for i in range (size):
    x=int(input("Enter array element : "))
    a.append(x)
    
print("For array 2")
for i in range (size):
    x=int(input("Enter array element : "))
    b.append(x)  
        
a1=np.array(a)
b1=np.array(b)
array_equal = np.allclose(a1,b1)
print("Result : ",array_equal)
