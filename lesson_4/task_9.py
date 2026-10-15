# 9. Tydzień temperatur — Dla dni = ["pon", "wt", "śr", "czw", "pt", "sob", "niedz"] i temperatury
# = [14.5, 17.0, 12.5, 19.5, 21.0, 16.5, 13.0] wyświetl minimum, maksimum, średnią (jedno miejsce
# po przecinku), listę rosnąco, trzy najwyższe temperatury (sortowanie malejące + wycinek) i najcieplejszy
# dzień ( index() ), nie zmieniając oryginału.

dni = ["pon", "wt", "śr", "czw", "pt", "sob", "niedz"]
temperatury = [14.5, 17.0, 12.5, 19.5, 21.0, 16.5, 13.0]

print(f"Min: {min(temperatury)}, max: {max(temperatury)}, średnia: {round(sum(temperatury)/len(temperatury), 1):.1f}")

print(f"Rosnąco: {sorted(temperatury)}")

print(f"Trzy najcieplejsze: {sorted(temperatury, reverse=True)[:3]}")

index_max = temperatury.index(max(temperatury))
print(f"Najcieplej: {dni[index_max]}")