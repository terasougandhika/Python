

#count_vowels method
def count_vowels(s):
    cnt=0
    for i in s:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or  i=='A' or  i=='E' or  i=='I' or i=='O' or i=='U' ):
            cnt+=1
    return cnt

#count_special_character method
def count_special_character(s):
    cnt=0
    for i in s:
        if(i=='@' or i=='#' or i=='$' or i=='%' or i=='&'):
            cnt+=1
    return cnt

#count_uppercase method
def count_uppercase(s):
    cnt=0
    for i in s:
        if i.isupper():
            cnt+=1
    return cnt

#count_lowercase method
def count_lowercase(s):
    cnt=0
    for i in s:
        if i.islower():
            cnt+=1
    return cnt

#digit_property method
def digit_property(s):
    cnt=0
    digit_sum=0
    for i in s:
        if i.isdigit():
            cnt+=1
            digit_sum+=int(i)
    return [cnt,digit_sum]

#is_valid_secure_code method
def is_valid_secure_code(s):
    check1=count_vowels(s)
    check2=count_special_character(s)
    check3=count_uppercase(s)
    check4=count_lowercase(s)
    check5=digit_property(s)
    #conditions
    if(check5[0]>0):
        print("{} contains {} digits ".format(s,check5[0]))
    elif(check5[0]<2):
        print("{} is not a valid secure code".format(s))
        return
    
    if(check5[1]%2!=0):
        print("The sum of digits in {} is : {}, an odd integer".format(s,check5[1]))
    else:
        print("The sum of digits in {} is : {}, not a odd integer".format(s,check5[1]))
        print("{} is not a valid secure code".format(s))
        return
    
    if(check4>0):
        print("{} contains {} lowercases ".format(s,check4))
    else:
        print("{} is not a valid secure code".format(s))
        return
    
    if(check3>0):
        print("{} contains {} upercases ".format(s,check3))
    else:
        print("{} is not a valid secure code".format(s))
        return
   
    if(check1>0):
        print("{} contains {} vowel(s) ".format(s,check1))
    else:
        print("{} is not a valid secure code".format(s))
        return
   
    if(check2>0):
        print("{} contains {}special character(s)".format(s,check2))
    else:
        print("{} is not a valid secure code".format(s))
        retrun
    
    print("{} is a valid secure code".format(s))

#inputs        
input1=input("Provide a string for the secure code: ")
is_valid_secure_code(input1)


