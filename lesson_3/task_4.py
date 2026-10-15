# 4. Odwracacz słów — zapytaj o słowo, wypisz je od tyłu i sprawdź, czy to palindrom (porównaj słowo
# małymi literami z jego odwróceniem).

word = input("Podaj słowo: ")
word_reverse = word[::-1]
print(word_reverse)

print("Palindrom:", word_reverse.lower() == word.lower()) 