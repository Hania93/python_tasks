# 11. Inicjały i nazwa pliku — z osoba = " jan maria kowalski " utwórz inicjały, podpis „Nazwisko, Imiona”
# i nazwę pliku. Rozpakuj split() do trzech zmiennych; nazwę pliku sklej "_".join(...) 

osoba = " jan maria kowalski "

firstname, middlename, lastname = osoba.split()

firstname = firstname.capitalize()
middlename = middlename.capitalize()
lastname = lastname.capitalize()

print(f"Inicjały: {firstname[0]}.{middlename[0]}.{lastname[0]}.")
print(f"Podpis: {lastname}, {firstname} {middlename}")
print(f"Plik: {firstname.lower()}_{middlename.lower()}_{lastname.lower()}.txt")