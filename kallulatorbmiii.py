def calculate_bmi(weight, height, weight_unit, height_unit):
    # Konwersja jednostek
    if weight_unit == 'lbs':
        weight = weight * 0.45359237  # funty na kg
    if height_unit == 'cm':
        height = height / 100  # cm na metry

    # Walidacja
    if weight <= 0 or height <= 0:
        return None, "Waga i wzrost muszą być większe od zera"

    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "niedowaga"
    elif bmi < 25:
        category = "waga prawidłowa"
    elif bmi < 30:
        category = "nadwaga"
    else:
        category = "otyłość"
    return bmi, category

if __name__ == "__main__":
    while True:
        try:
            weight = float(input("Podaj wagę: "))
            weight_unit = input("Jednostka wagi (kg/lbs): ").strip().lower()
            height = float(input("Podaj wzrost: "))
            height_unit = input("Jednostka wzrostu (m/cm): ").strip().lower()
            bmi, result = calculate_bmi(weight, height, weight_unit, height_unit)
            if bmi is None:
                print(result)
            else:
                print(f"Twoje BMI: {bmi:.2f}")
                print(f"Kategoria: {result}")
        except ValueError:
            print("Podaj poprawne wartości liczbowe!")
        again = input("Czy chcesz powtórzyć kalkulację? (t/n): ").strip().lower()
        if again !='t':
            break