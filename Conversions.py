

#input 
while True:
    dst_meter = float(input("Enter the distance in meters: "))
    
    if dst_meter == 0:
        break #exits loop
    
    #formulae for conversion
    else: 
        Miles = dst_meter*0.000621371192236

        Feet = Miles*5280

        Inches = Feet*12


        print("conversion in metres:", int(Miles), 'MILES', int(Feet), 'FEET',
                  int(Inches), 'INCHES')
