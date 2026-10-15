# 5. Kantor wymiany walut — zapytaj o kwotę w złotych i kurs dolara (ile złotych kosztuje 1 USD), a potem
# wyświetl kwotę w dolarach.

from decimal import Decimal, InvalidOperation

try:
    count_pln = Decimal(input("Podaj kwotę w złotówkach (pln) "))
    rate = Decimal(input("Ile złotych kosztuje 1 usd? (pln) "))

    if count_pln <= 0 or rate <= 0:
        print("Kurs i kwota muszą być większe od zera.")
    else:
        print(f"Kwota (USD): {count_pln / rate:.2f}")
    
except InvalidOperation:
    print("Podałeś nieprawidłowe wartości")