# 2. Kalkulator BMI — zapytaj o wagę (kg) i wzrost (m), oblicz waga / wzrost ** 2 i wypisz z jednym
# miejscem po przecinku

weight = float(input("Waga [kg]: "))
height = float(input("Wzrost [m]: "))

bmi = weight / height ** 2

print(f"Twoje BMI: {bmi:.1f}")