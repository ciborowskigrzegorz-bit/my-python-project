# ...existing code...
if request.method == 'POST':
    # Get and store form data
    form_data = {
        "imie": request.form.get('imie', '').strip(),
        "wiek": request.form.get('wiek', '').strip(),
        "x": request.form.get('x', '').strip(),
        "y": request.form.get('y', '').strip()
    }
    
    # Validate required fields
    if not form_data["imie"] or not form_data["wiek"]:
        error = "Proszę podać imię i wiek"
    else:
        try:
            wiek = int(form_data["wiek"])
            if wiek < 0 or wiek > 150:
                error = "Wiek musi być liczbą od 0 do 150"
            else:
                greeting = f"Cześć, {form_data['imie']}! Masz {wiek} lat."
                
                # Calculate if both numbers provided
                if form_data["x"] and form_data["y"]:
                    try:
                        x = float(form_data["x"])
                        y = float(form_data["y"])
                        results = {
                            'x': x,
                            'y': y,
                            'dodawanie': x + y,
                            'odejmowanie': x - y,
                            'mnożenie': x * y,
                            'dzielenie': x / y if y != 0 else "Nie można dzielić przez zero",
                            'porównanie': f"{x} jest większe od {y}" if x > y else 
                                         f"{y} jest większe od {x}" if y > x else 
                                         f"Obie liczby {x} i {y} są równe"
                        }
                    except ValueError:
                        error = "Proszę podać prawidłowe liczby dla x i y"
        except ValueError:
            error = "Proszę podać prawidłowy wiek"
# ...existing code...