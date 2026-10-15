# 5. Konwerter temperatury z datą — pobierz temperaturę w °C, przelicz F = C * 9 / 5 + 32 i wypisz z
# datą date.today()

from datetime import date

temp_c = float(input("Podaj temp w stopniach C: "))

temp_f = temp_c * 9 / 5 + 32

print(f"Pomiar z {date.today()}: {temp_c}°C = {temp_f:.2f}°F")