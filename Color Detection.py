
pocket_number = int(input("Enter a pocket number 0 thru 36: "))#input

if pocket_number >= 0 and pocket_number <= 36:#number condition

    if pocket_number == 0:#color conditions
        pocket_color = "green"

    elif pocket_number >= 1 and pocket_number <= 10:
        if pocket_number % 2 == 0:
           pocket_color = "black"
        else:
            pocket_color = "red"

    elif pocket_number >= 11 and pocket_number <= 18:
        if pocket_number % 2 == 0:
           pocket_color = "red"
        else:
            pocket_color = "black"

    elif pocket_number >= 19 and pocket_number <= 28:
        if pocket_number % 2 == 0:
            pocket_color = "black"
        else:
            pocket_color = "red"

    elif pocket_number >= 29 and pocket_number <= 36:
        if pocket_number % 2 == 0:
            pocket_color = "red"
        else:
            pocket_color = "black"

    print(pocket_number, "is", pocket_color)
else:
    print("The entered number is invalid")
