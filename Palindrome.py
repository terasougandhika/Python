

###function to check it is a palindrome or not
def Palindrome(a):
    return  a== a[::-1]

i=10
while  i:
    a=input("Enter a string to see if it is a palindrome or not ")
    if(Palindrome(a)):
        print(a+" is a Palindrome")
    else:
        print(a+" is not a Palindrome")
    i=i-1
