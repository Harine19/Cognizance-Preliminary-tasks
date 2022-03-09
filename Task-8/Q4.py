#Convert the first character of each element in a series to uppercase
import pandas as pd
l=input("Enter a statement : ")
elements=l.split() 
statement=pd.Series(elements)
for i in statement.str.capitalize() :
    print(i,end = " ")
print()
