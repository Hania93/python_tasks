# 2. Zapoznanie — zapytaj użytkownika o imię i wiek, a potem wyświetl f-stringiem powitanie z wiekiem za 10
# lat

firstname = input("Podaj swoje imię: ")

try:
    wiek = int(input("Wpisz swój wiek w latach: "))

    if wiek < 0:
        print("Wiek nie może być ujemny.")
    else:
        print(f"Witaj {firstname}! Za 10 lat będziesz mieć {wiek + 10} lat.")

except ValueError:
    print("Wiek musi być liczbą całkowitą.")