# 9. Zegar z sekund — zamień podaną liczbę sekund na godziny, minuty i sekundy. Wyświetl wynik opisowo
# oraz w formacie H:M:S za pomocą parametru sep .
# Wskazówka: najpierw // 3600 , potem reszta %
# 3600 

try:
    input_seconds = int(input("Podaj liczbę sekund: "))
    
    if(input_seconds < 0):
        print("Podana liczba sekund nie może być ujemna")
    else:
        hours = input_seconds // 3600
        minutes = (input_seconds % 3600) // 60
        seconds = input_seconds % 60
        
        print(f"Liczba sekund: {input_seconds}")
        print(f"{hours} godz. {minutes} min {seconds} s")
        print(hours, minutes, seconds, sep=":")
    
except ValueError:
    print("Podana wartość musi być liczbą całkowitą!")