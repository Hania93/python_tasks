# Kalkulator pola i obwodu — poproś o długość i szerokość prostokąta w metrach (mogą być ułamkowe) i
# wyświetl jego pole oraz obwód

try:
    a = float(input("Podaj długość prostokąta (m) "))
    b = float(input("Podaj szerokosc prostokąta (m) "))

    if a <= 0 or b <= 0:
        print("Wymiary muszą być większe od 0")        
    else:
        print(f"Długość (m): {a}")
        print(f"Szerokość (m): {b}")
        print(f"Pole: {a * b} m2")
        print(f"Obwód: {2 * (a + b)} m")
    
except ValueError:
    print("Podałeś nieprawidłową wartość")
