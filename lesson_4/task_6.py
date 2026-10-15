# 6. Identyfikator po zmianie — Zapamiętaj id przed każdą zmianą i porównaj z id po niej: x = 10 → x =
# x + 1 ; lista = [1, 2] → lista.append(3) → lista = lista + [4] . W komentarzach wyjaśnij, które
# operacje zmieniają obiekt w miejscu, a które tworzą nowy.

x = 10
print(id(x)) ## 

x += 1
print(id(x)) ## inne id niż przed zmianą, ponieważ obiekt niemutowalny, czyli zmiana powoduje, że powstaje nowy obiekt w innym miejscu w pamięci

lista = [1, 2]
print(id(lista))

lista.append(3)
print(id(lista)) ## lista jest obiektem mutowalnym, dlatego jej zmiana czyli dodanie nowego elemntu do niej nie powoduje powstania nowego obiektu tylko zmienia juz istniejąca list

lista = lista + [4]
print(id(lista)) ## tu do istniejącej listy dodajemy inną listę i powstaje nowy obiekt w pamięci
