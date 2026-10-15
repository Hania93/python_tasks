# 10. Wstęp do parku rozrywki — zapytaj o wzrost w centymetrach i o to, czy jest opiekun ( tak / nie ).
# Zasada: wpuszczane są dzieci o wzroście od 120 cm I z opiekunem LUB osoby o wzroście od 160 cm. Za
# pomocą porównań oraz and i or wyświetl True lub False 

try:
    height = int(input("Wzrost: "))
    is_guardian = input("Czy jest opiekun? (tak/nie): ").strip().lower()
    
    can_enter = height >= 160 or (height >= 120 and is_guardian == "tak")
        
    print(f"Można wejść: {can_enter}")
    
except ValueError:
    print("Podana wartość musi być liczbą całkowitą!")