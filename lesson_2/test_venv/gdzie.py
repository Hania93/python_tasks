# 10. Gdzie jest mój Python? — gdzie.py wypisuje sys.executable . Uruchom go: (a) z aktywnym venv, (b)
# po deactivate , (c) bez aktywacji, przez venv/bin/python gdzie.py (Windows:
# venv\Scripts\python.exe gdzie.py ). W komentarzu wyjaśnij rolę PATH 

import sys
print(sys.executable)

# PATH to lista katalogów, w których terminal szuka programów.
# Aktywacja venv dodaje jego katalog bin na początek PATH,
# dlatego polecenie python uruchamia interpreter z tego środowiska.
# deactivate przywraca poprzednią wartość PATH.
# Podanie venv/bin/python pozwala wybrać interpreter bez aktywacji
# i bez szukania go w PATH.