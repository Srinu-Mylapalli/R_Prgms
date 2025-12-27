def pour_water(jugA,jugB):
    max1, max2, fill=3, 4, 2
    print(f"{jugB}\t{jugB}")
    if (jugB==fill):
        return
    elif (jugB==max2):
        pour_water(0,jugA)
    elif (jugA != 0 and jugB ==0):
        pour_water(0,jugA)
    elif (jugA==fill):
        pour_water(jugA,0)
    elif (jugA<max1):
        pour_water(max1, jugB)
    elif (jugA<(max2-jugB)):
        pour_water(0, (jugA+jugB))
    else:
        pour_water(jugA-(max2-jugB),(max2-jugB)+jugB)
print("jugA \t jugB")
pour_water(0, 0)
