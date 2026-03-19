carparts = ('Engine', 'Transmission', 'Wheel', 'Gear', 'Brake', 'Battery')
print('Our tuple is: ', carparts)
print('Item in the first position is: ', carparts[0])
print('Item in the 5th position is: ', carparts[4])
indexOfWheel = carparts.index('Wheel')
print('Index of Wheel is: ', indexOfWheel)
lengthcarpartsTuple = len(carparts)
print('Length of the carparts tuple is: ', lengthcarpartsTuple)
for item in carparts:
    print(item)
print(carparts * 2)
print(carparts[1:4])
if "Brake" in carparts:
    print("Brake is available in the carparts tuple")
else:
    print("Brake is not available in the carparts tuple")