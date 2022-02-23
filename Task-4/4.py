#program to check if given number is palindrome number
num=int(input("Enter a number: "))
if str(num)==str(num)[::-1]:
    print("True")
else:
    print("False")
