
while True:
    Num = float(input("Enter number of between 1.00 and 999.9 inclusive: "))
    if Num == 555.55:
        break #exits the loop
    elif Num < 1.00 or Num > 999.99:
        print("No, not valid") # beyond limit
    else:
        print("Yes,", Num, "is valid") #within limit
print("Exit the loop")
