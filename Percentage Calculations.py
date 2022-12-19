
#input
amount=input("Enter meal amount, dollars and cents:")

#percentage calculations
Tax_p=0.05
Tip_p=0.20
Tax= float(amount) * float(Tax_p)
Tip= float(amount) * float(Tip_p)
Total= float(amount)+float(Tax)+float(Tip)

#outputs
print('Tip is $' + format(round(Tip,2), ",.2f") )
print('Tax is $' + format(round(Tax,2), ",.2f") )
print('Total is $' + format(round(Total,2), ",.2f") )
