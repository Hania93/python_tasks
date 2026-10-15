# 1. Tworzenie i typowanie — jednym przypisaniem wielokrotnym utwórz imię, wiek, średnią ocen i status
# studenta. Wypisz każdą zmienną z typem ( f"{imie=}" i type() ), a potem przypisz do wiek napis
# "dwadzieścia" i pokaż nowy typ

name, age, avg, status = "Ola", 20, 4.2, "student"

print(f"name={name} {type(name)}")
print(f"age={age} {type(age)}")
print(f"avg={avg} {type(avg)}")
print(f"status={status} {type(status)}")

age = "dwadziescia"
print(f"age={age} {type(age)}")