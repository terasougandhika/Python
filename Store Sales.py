

#Enter store sales
Sunday = float(input("Enter the store sales for Sunday: "))
Monday = float(input("Enter the store sales for Monday: "))
Tuesday = float(input("Enter the store sales for Tuesday: "))
Wednesday = float(input("Enter the store sales for Wednesday: "))
Thursday = float(input("Enter the store sales for Thursday: "))
Friday = float(input("Enter the store sales for Friday: "))
Saturday = float(input("Enter the store sales for Saturday: "))

store_sales = [Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday]

#calculate store_sales:
sums = 0
for number in store_sales:
    sums += number
total = sums

average = sum(store_sales)/len(store_sales)
greater_value = max(store_sales)
least_value = min(store_sales)
#print store_sales
print("Total sales were $",format(total,".2f"))
print("Average sales were $",format(average,".2f"))
print("Greatest sales were $",greater_value)
print("Leasr sales were $",least_value)
