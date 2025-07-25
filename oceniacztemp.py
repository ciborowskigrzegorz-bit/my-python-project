# Poproś o temperaturę
temp = float(input("Podaj temperaturę w °C: "))

# Sprawdź przedziały i wyświetl odpowiedni komunikat
if temp < 0:
    print("Mróz")
elif 0 <= temp <= 10:
    print("Zimno")
elif 11 <= temp <= 20:
    print("Chłodno")
elif 21 <= temp <= 30:
    print("Ciepło")
elif 31 <= temp <= 40:
    print("Bardzo ciepło")
else:
    print("Gorąco")
