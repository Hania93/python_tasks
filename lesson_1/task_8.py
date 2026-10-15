# 8. Sprawdzanie parzystości — dla podanej liczby całkowitej wyświetl wynik porównań: czy jest parzysta
# ( liczba % 2 == 0 ) i czy dzieli się przez 3.

try:
    number = int(input("Podaj liczbę całkowitą: "))    
    is_even = number % 2 == 0    
    is_divisible_by_3 = number % 3 == 0
        
    print(f"Parzysta: {is_even}")
    print(f"Podzielna przez 3: {is_divisible_by_3}")
    
except ValueError:
    print("Podana wartość musi być liczbą całkowitą!")