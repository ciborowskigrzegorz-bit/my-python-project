year = int(input("Podaj rok: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Rok przestępny")
        else:
            print("Nieprzestępny")
    else:
        print("Rok przestępny")
else:
    print("Nieprzestępny")
