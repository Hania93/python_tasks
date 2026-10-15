# 1. “Flat is better than nested.”
# Płaskie jest lepsze niż zagnieżdżone.
# Unikaj zbędnych poziomów zagnieżdżenia.

# # Zagnieżdżone warunki
# if zalogowany:
#     if ma_bilet:
#         print("Możesz wejść")

# # Płasko — ten sam efekt
# if zalogowany and ma_bilet:
#     print("Możesz wejść")
    
# 2. “Errors should never pass silently.”
# Błędy nigdy nie powinny przechodzić niezauważone.
# Obsługuj błędy.

# # Błąd zostaje ukryty
# try:
#     wiek = int("abc")
# except ValueError:
#     pass

# # Informujemy o błędzie
# try:
#     wiek = int("abc")
# except ValueError:
#     print("Wiek musi być liczbą całkowitą.")
    
# 3. “Sparse is better than dense.”
# Przejrzysty układ jest lepszy niż upakowany.
# Oddzielaj fragmenty kodu, które wykonują różne zadania.

# imie = input("Podaj imię: ")
# wiek = int(input("Podaj wiek: "))

# wiek_za_rok = wiek + 1

# print(f"{imie}, za rok będziesz mieć {wiek_za_rok} lat.")