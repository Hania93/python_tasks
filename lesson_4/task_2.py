# Niemutowalność krotki — Utwórz punkt = (10, 20, 30) , rozpakuj go do x, y, z i wyświetl y .
# Spróbuj zmienić pierwszy element na 15 , przepisz komunikat błędu do komentarza i wyjaśnij go.
# Zakomentuj błędną linię i zbuduj nowy_punkt z (15,) i wycinka punkt[1:] .
# Oczekiwany wynik: 20 , TypeError: 'tuple' object does not support item assignment , (15, 20,
# 30)

point = (10, 20, 30)
x, y, z = point
print(f"y = {y}")

#point[0] = 15
# TypeError: 'tuple' object does not support item assignment - krotka jest niemutowalna, dlatego nie można zmienić wartości jej elementów

new_point = (15, ) + point[1:]
print(new_point)

