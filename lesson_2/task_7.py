# 7. Geometria koła — pobierz promień koła i bok kwadratu; wypisz pole i obwód koła ( math.pi ) oraz
# przekątną kwadratu ( math.sqrt )

import math

r = float(input("Podaj promien kola: "))
a = float(input("Podaj bok kwadratu: "))

print(f"Pole koła: {math.pi*r*r}")
print(f"Obwód koła: {2*math.pi*r}")
print(f"Przekątna kwadratu: {a*math.sqrt(2)}")