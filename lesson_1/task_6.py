# 6. Konwerter systemów liczbowych — wyświetl podaną liczbę całkowitą w systemie dwójkowym i
# szesnastkowym. Potem poproś o trzy składowe koloru zapisane szesnastkowo i wyświetl kolor w zapisie
# #RRGGBB oraz jako liczby dziesiętne.
# Podaj liczbę całkowitą: 42
# Dwójkowo: 0b101010
# Szesnastkowo: 0x2a
# R (hex): 1E
# G (hex): 90
# B (hex): FF

try:
    number = int(input("Podaj liczbę całkowitą: "))
    print(f"Dwójkowo: {bin(number)}")
    print(f"Szestnastkowo: {hex(number)}")
    
    r = int(input("R (hex): "), 16)
    g = int(input("G (hex): "), 16)
    b = int(input("B (hex): "), 16)

    if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
        print("Każda składowa musi być w zakresie od 00 do FF.")
    else:
        print(f"Kolor: #{r:02X}{g:02X}{b:02X}")
        print(f"Dziesiętnie: R={r}, G={g}, B={b}")

except ValueError:
    print("Podałeś nieprawidłową wartość.")