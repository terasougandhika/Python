
print("Check for a magic date")
#inputs
month = int(input("Enter mm for month"))
day = int(input("Enter dd for day"))
year = int(input("Enter yy for year"))
#condition for date
if month <=12 and day <= 31:
    if month * day == year: #consition for magic date
        print(month +day +year +"is a magic date")
    else:
        print("The entered date is not magic date")
else:
    print("The entered date is invalid")
