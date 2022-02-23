#this 2 dimentional list contains a dealer's cars and their details
size=int(input("How many cars do you have?: "))
x = [[(i) for j in range(3)] for i in range(size+1)]

x[0]=["S.no","Brand","Color"]

for i in range(1,size+1):
    print("For car ",i,": ")
    company=input("Enter company name of car: ")
    color=input("Enter colour of car: ")
    x[i]=[i,company,color]

print()
#print in tabular form    
for i in x:
    for j in i:
        print(j,end='\t')
    print()

print("\nSecond record: ")
for i in x[2]:
    print(i,end='\t')

