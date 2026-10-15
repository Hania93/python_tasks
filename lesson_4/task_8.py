# 8. Pułapka aliasu w playliście — moja_playlista = ["Intro", "Lato", "Nocą"] . Brat pisze
# playlista_brata = moja_playlista i dodaje "Metal Mix" . Wyświetl obie playlisty i wynik is , wyjaśnij
# w komentarzu, co się stało, a potem popraw kod

moja_playlista = ["Intro", "Lato", "Nocą"]

# playlista_brata = moja_playlista

# playlista_brata.append("Metal Mix")

# print(moja_playlista)
# print(playlista_brata)
# print(moja_playlista is playlista_brata)

#brat nie skopiowal listy tylko utworzył do niej alias (inną nazwe), ale ciągle wskazywala ona na to samo miejsce w pamięci i dlatego dodając do swojej listy modyfikował pierwotną listę, wynik is jest True, bo to to samo miejsce w pamięci Żeby tego uniknąć trzeba skopiować listę - copy(), niżej poprawka

playlista_brata = moja_playlista.copy()
playlista_brata.append("Metal Mix")

print(moja_playlista)
print(playlista_brata)
print(moja_playlista is playlista_brata)
