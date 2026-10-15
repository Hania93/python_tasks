# 11. Generator hasła — zbuduj 8-znakowe hasło z ośmiu wywołań random.choice(znaki) połączonych + ,
# gdzie znaki = string.ascii_letters + string.digits . Potem użyj secrets.choice i w komentarzu
# wyjaśnij na podstawie dokumentacji modułu random , dlaczego hasła losuje się modułem secrets . (Pętlą
# skrócisz to w lekcji 5.

import string
import random
import secrets

znaki = string.ascii_letters + string.digits
haslo_random = ""
haslo_secrets = ""

for _ in range(8):
    haslo_random += random.choice(znaki)
    haslo_secrets += secrets.choice(znaki)
    
print(f"Haslo random: {haslo_random}")
print(f"Haslo secrets: {haslo_secrets}")

#hasło z random można przewidzieć, jest generowane wg przewidywalnego algorytmu a secrets nie