# 12. Lista zadań w pamięci — Rozbuduj main.py z etapów 2–3: zamiast jednej karty program przechowuje
# wiele zadań.
# Utwórz listę do_zrobienia i dodaj trzy zadania jako słowniki z kluczami "tytul" , "minuty" ,
# "priorytet" , "tagi" (tagi jako zbiór, np. set("dom, urzędy".split(", ")) ).
# Wyświetl tytuł drugiego zadania i sumę minut wszystkich trzech.
# Przenieś pierwsze zadanie do listy zrobione ( pop(0) → append ) i wyświetl liczniki obu list.
# Wyświetl posortowane unikalne tagi wszystkich zadań ( | ).
# Pokaż pułapkę aliasu: archiwum = zrobione , dopisz do archiwum zadanie testowe i wyświetl
# len(zrobione) ; usuń zadanie testowe ( zrobione.pop() ), popraw przez .copy() i powtórz
# dopisanie.

to_do = [
    {
        "title": "Zrobic obiad", 
        "estimated_time": 75, 
        "priority": 2,
        "tags": {"jedzenie", "obiad", "głodny"}
    },
    {
        "title": "Zrobic zakupy", 
        "estimated_time": 35, 
        "priority": 3,
        "tags": {"zakupy", "jedzenie", "sklep"}
    },
    {
        "title": "Zrobic pranie", 
        "estimated_time": 15, 
        "priority": 1,
        "tags": {"pranie", "ciuchy", "pralka"}
    }    
]

done_list = []

print(f"Drugie zadanie: {to_do[1]["title"]}")

total_time = 0

for task in to_do:
    total_time += task["estimated_time"]
    
print(f"Łącznie minut: {total_time}")

done_task = to_do.pop(0)
done_list.append(done_task)

print(f"Do zrobienia: {len(to_do)}, zrobione: {len(done_list)}")

all_tags = set()

for task in to_do:
    all_tags = all_tags | task["tags"]

sorted_tags = sorted(all_tags)

print(f"Tagi: {sorted_tags}")

archive_list_copy = done_list.copy()

done_list.append({
        "title": "Zadanie testowe", 
        "estimated_time": 25, 
        "priority": 2,
        "tags": {"dom", "porządek", "sprzątanie"}
})

done_list.pop()

done_list.append({
        "title": "Zadanie testowe", 
        "estimated_time": 25, 
        "priority": 2,
        "tags": {"dom", "porządek", "sprzątanie"}
})

print(f"Alias: zrobione  ma {len(done_list)} zadania; kopia: zrobione ma {len(archive_list_copy)} zadanie")


# task_title = input("Tytuł zadania: ").strip()
# task_title = task_title[:1].upper() + task_title[1:]
# tags = input("Tagi (po przecinku): ").replace(" ", "").split(',')
# estimated_time = int(input("Czas [min]: "))
# priority = int(input("Priorytet: (1-3): "))

# for tag in tags:
#     tag = tag.replace(' ', '')
    
# print(30*"=")
# print(f"{'Zadanie:':<12}{task_title}")
# print(f"{'Tagi:':<12}{", ".join(tags)}")
# print(f"{'Czas:':<12}{estimated_time // 60} godz. {estimated_time % 60:02d} min")
# print(f"{'Priorytet:':<12}{priority} (pilne: {priority >= 2})")
# print(30*"=")
