# Prosty kalkulator BMI

print("Witaj! Obliczymy Twój wskaźnik BMI.")

# Pobierz dane od użytkownika
waga = float(input("Podaj swoją wagę w kilogramach: "))
wzrost = float(input("Podaj swój wzrost w metrach (np. 1.75): "))

# Oblicz BMI
bmi = waga / (wzrost ** 2)

# Określ kategorię
if bmi < 18.5:
    kategoria = "niedowaga"
elif bmi < 25:
    kategoria = "waga prawidłowa"
elif bmi < 30:
    kategoria = "nadwaga"
else:
    kategoria = "otyłość"

# Wyświetl wynik w czytelnej formie
print(f"\nTwoje BMI wynosi: {bmi:.2f}")
print(f"Kategoria wagowa: {kategoria.capitalize()}")
