# 12. Formater karty zadania — rozbuduj main.py z etapu 2: program pyta o tytuł, tagi, czas i priorytet, a
# potem:
# czyści tytuł strip() i zmienia na wielką tylko pierwszą literę: tytul[:1].upper() + tytul[1:]
# ( capitalize() zmieniłoby ZUS na zus );
# porządkuje tagi: usuwa spacje replace() , tnie split(",") i skleja ", ".join(...) ;
# drukuje kartę z etykietami :<12 i minutami :02d 

from datetime import date

task_title = input("Tytuł zadania: ").strip()
task_title = task_title[:1].upper() + task_title[1:]
tags = input("Tagi (po przecinku): ").replace(" ", "").split(',')
estimated_time = int(input("Czas [min]: "))
priority = int(input("Priorytet: (1-3): "))

for tag in tags:
    tag = tag.replace(' ', '')
    
print(30*"=")
print(f"{'Zadanie:':<12}{task_title}")
print(f"{'Tagi:':<12}{", ".join(tags)}")
print(f"{'Czas:':<12}{estimated_time // 60} godz. {estimated_time % 60:02d} min")
print(f"{'Priorytet:':<12}{priority} (pilne: {priority >= 2})")
print(30*"=")
