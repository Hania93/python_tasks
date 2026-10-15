# 11. Tabela prawdy: automatyczne podlewanie — ogród jest podlewany według reguły podlewaj =
# (sucha_ziemia and not pada_deszcz) or tryb_reczny . W komentarzach zapisz przewidywany wynik dla
# wszystkich 8 kombinacji trzech zmiennych i sprawdź co najmniej 3 z nich za pomocą print() . Potem
# znajdź kombinacje, dla których reguła sucha_ziemia and (not pada_deszcz or tryb_reczny) daje inny
# wynik, i wyjaśnij w komentarzu, dlaczego.
# Oczekiwany wynik: wydruki zgodne z tabelą, np. True False False -> True i True True False ->
# False ; reguły różnią się dokładnie w 2 kombinacjach.

#podlewaj = (sucha_ziemia and not pada_deszcz) or tryb_reczny
# sucha_ziemia pada_deszcz tryb_reczny -> podlewaj
# True True True -> True
# True False True -> True
# False True True -> True
# False False True -> True
# True True False ->False
# True False False -> True
# False True False -> False
# False False False -> False

sucha_ziemia = True
pada_deszcz = False
tryb_reczny = False
print((sucha_ziemia and not pada_deszcz) or tryb_reczny) #true

sucha_ziemia = True
pada_deszcz = True
tryb_reczny = False
print((sucha_ziemia and not pada_deszcz) or tryb_reczny) #false

sucha_ziemia = False
pada_deszcz = False
tryb_reczny = True
print((sucha_ziemia and not pada_deszcz) or tryb_reczny) #true

#sucha_ziemia and (not pada_deszcz or tryb_reczny)
# True True True -> True
# True False True -> True
# False True True -> True <-----
# False False True -> True <-----
# True True False ->False 
# True False False -> True
# False True False -> False
# False False False -> False

# Reguły różnią się w dwóch miejscach, gdy sucha_ziemia = False i tryb_reczny = True,
# niezależy od tego, czy pada deszcz.
# W pierwszej regule tryb ręczny wystarcza, aby włączyć podlewanie, bo wystarczy, że w OR jedno jest prawdziwe
# W drugiej regule sucha ziemia jest konieczna
# False w AND zawsze daje False.