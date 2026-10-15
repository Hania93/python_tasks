# 7. Maskowanie numeru karty — dla numer = "4532015112830366" sprawdź, czy ma 16 znaków, i wypisz go
# z zakrytymi pierwszymi 12 cyframi w grupach po 4

number = "4532015112830366"

print(f"Długość poprawna: {len(number) == 16}")
print(number[-4:])