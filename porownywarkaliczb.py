# Poproś użytkownika o podanie dwóch liczb
x = float(input("Podaj pierwszą liczbę: "))
y = float(input("Podaj drugą liczbę: "))

# Porównaj liczby i wyświetl wynik
if x > y:
    print(f"{x} jest większe od {y}")
elif x < y:
    print(f"{y} jest większe od {x}")
else:
    print(f"Obie liczby {x} i {y} są równe")
