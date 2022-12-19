

#inputs
a = input("Enter a number - counter at 1: ")
b = input("Enter a number - counter at 2: ")
c = input("Enter a number - counter at 3: ")
d = input("Enter a number - counter at 4: ")
e = input("Enter a number - counter at 5: ")

#list
l= [a,b,c,d,e]
print(l)
print ("You created list: ", l)

print("Now convert the list to tuple.")
print("Print the tuple in reversed order: ")

#tuple
t = tuple(l)
print(type(t))
print(t)

#reverse 
i = len(t)-1
while i >= 0:
  print ("Reverse print - counter: ",t[i])
  i -= 1
