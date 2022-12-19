

#inputs
miles_driven=input("Enter total miles driven, up to two decimals ")
gallons_used=input("Enter total gallons used, up to two decimals ")

MPG = float(miles_driven) / float(gallons_used) #formula

#print statements
print("Miles driven is",miles_driven)
print("Gallons used is",gallons_used)
print('The MPG is ${:,.2f}'.format(MPG))
