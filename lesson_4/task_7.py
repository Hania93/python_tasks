# 7. Wspólni znajomi — Ola zna {"Kasia", "Tomek", "Igor", "Zuza"} , a Marek — {"Tomek", "Zuza",
# "Bartek"} . Wyświetl posortowane: wspólnych znajomych, znajomych tylko Oli, wszystkich razem oraz
# liczbę osób znanych tylko jednemu z nich.

Ola = {"Kasia", "Tomek", "Igor", "Zuza"}
Marek = {"Tomek", "Zuza", "Bartek"}

print("Wspólni znajomi")
shared = sorted(Ola & Marek)
print(shared)

print("Znajomi tylko Oli")
only_ola = sorted(Ola - Marek)
print(only_ola)

print("Znajomi obu bez duplikatów")
sum = sorted(Ola | Marek)
print(sum)

print("Liczba osób znanych tylko jednemu z nich:")
print(len(Ola ^ Marek))