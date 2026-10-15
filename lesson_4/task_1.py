# 1. Operacje na liście — Utwórz owoce = ["jabłko", "banan", "wiśnia"] . Dodaj na koniec
# "pomarańcza" , zamień drugi element na "jagoda" , usuń ostatni element przez pop() i wyświetl usunięty
# element oraz listę.
# Oczekiwany wynik: Usunięto: pomarańcza i ['jabłko', 'jagoda', 'wiśnia']

owoce = ["jabłko", "banan", "wiśnia"]
owoce.append("pomarańcza")
owoce[1] = "jagoda"
removed = owoce.pop()

print(f"Usunięto: {removed}")
print(f"Lista po modyfikacjach to {owoce}")