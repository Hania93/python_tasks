# 4. Książka telefoniczna — Utwórz słownik z trzema kontaktami. Dodaj czwarty, zmień numer jednej osoby,
# usuń inną przez del i wyświetl słownik. Potem zapytaj ( input() ) o imię i wyświetl numer przez get() z
# domyślnym "brak numeru" .

contacts = {'Mama': '601 111 222', 'Kasia': '700 800 900', 'Tata': '982 755 666'}

print(contacts)

contacts["Pan Józef"] = '512 000 333'
contacts["Mama"] = '888 888 888'

print(contacts)

del contacts["Kasia"]

print(contacts)

check_name = input("Kogo szukasz: ")

check_number = contacts.get(check_name, "brak numeru")

print(f"{check_name}: {check_number}")