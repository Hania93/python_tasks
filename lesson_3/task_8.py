# Rzutowanie typów — zamień liczba_str = "5.8" na float , a potem na int ; wypisz wyniki z typami
# i porównaj z round() . Potem uruchom int(liczba_str) , przepisz ostatnią linię tracebacku do
# komentarza z wyjaśnieniem i zakomentuj tę instrukcję

liczba_str = "5.8"
liczba_float = float(liczba_str)
liczba_int = int(liczba_float)
liczba_round = round(liczba_float)

print(f"Liczba string: {liczba_str}, typ: {type(liczba_str)}")
print(f"Liczba float: {liczba_float}, typ: {type(liczba_float)}")
print(f"Int: {liczba_int}, typ: {type(liczba_int)}")
print(f"Round: {liczba_round}, typ: {type(liczba_round)}")

#liczba_int = int(liczba_str)
# ValueError: invalid literal for int() with base 10: '5.8'
# int() nie przyjmuje napisu z częścią ułamkową.
# Najpierw trzeba zamienić taki napis na float.