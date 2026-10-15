# 3. Analiza stringa — dla tekst = " Python jest super! " wypisz: długość, napis po strip() , ten napis
# małymi literami, wersję z "świetny" zamiast "super" i znak o indeksie 4 oczyszczonego napisu

text = " Python jest super! "
print(len(text))
print(text.strip())
print(text.lower())
print(text.replace("super", "świetny"))
print(text.strip()[4])