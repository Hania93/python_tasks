# 10. Identyfikator obiektu — a) W pliku .py przypisz a = 256 , b = 256 , c = 257 , d = 257 i wyświetl
# a is b , c is d . b) Wpisz te przypisania linia po linii w REPL ( python w terminalu) i sprawdź c is d . c)
# W pliku dopisz e = int("257") , f = int("256") i wyświetl c is e , a is f . W komentarzach wyjaśnij
# wszystkie różnice i to, dlaczego liczby porównujemy przez == 

a = 256
b = 256
c = 257
d = 257

print(a is b)
print(c is d)

e = int("257")
f = int("256")

print(c is e)
print(a is f)

# Python trzyma gotowe obiekty małych liczb całkowitych do 256, dlatego a, b, f to ten sam obiekt, w jednym komilowanym kodzie może też dzielić większe liczby dlatego c is d też jest True

# przy konwersji python tworzy inny obiekt niż ten zwykly int i dlatego mimo, że c i e mają ta samo wartośc są innym obiektem bo jest wieksze niz 256, zapisanych stalych używa do liczb <= 256

# w REPL każde osobno wpisane przypisanie jest kompilowane oddzielnie, liczba 256 korzysta z pamięci podręcznej małych liczb, ale osobno utworzone obiekty 257 będą różne
