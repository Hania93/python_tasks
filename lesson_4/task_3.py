# 3. is kontra == — Utwórz lista1 = [1, 1] , lista2 = [1, 1] , lista3 = lista1 . Wyświetl == i
# is dla wszystkich trzech par i wyjaśnij wyniki w komentarzach. Dopisz 3 do lista3 i wyświetl lista1

lista1 = [1, 1]
lista2 = [1, 1]
lista3 = lista1

print(lista1 == lista2) #true
print(lista1 is lista2) #false
# te same wartosci, ale inne obiekty w pamieci w innym miejscu

print(lista2 == lista3) #true
print(lista2 is lista3) #true
# te same wartosci, ale inne obiekty w pamieci w innym miejscu

print(lista1 == lista3) #true
print(lista1 is lista3) #true
# to samo miejsce w pamieci, ten sam obiekt

lista3.append(3)
print(lista1)




