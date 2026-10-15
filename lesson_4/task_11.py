# 11. Magazyn sklepu — Dla magazyn = {"mleko": {"cena": 3.49, "ilosc": 40}, "chleb": {"cena":
# 5.99, "ilosc": 25}, "kawa": {"cena": 24.99, "ilosc": 8}} : sprzedaj 3 mleka, przyjmij 12 chlebów,
# dodaj "herbata" (11.49 zł, 15 szt.), wycofaj kawę przez pop() z podaniem jej wartości. Wyświetl
# posortowane nazwy produktów i wartość zapasu mleka oraz chleba. Odwołaj się do magazyn["cukier"] ,
# zapisz błąd w komentarzu i zastąp tę linię wersją z get() 

magazyn = {
    "mleko": {"cena": 3.49, "ilosc": 40}, 
    "chleb": {"cena": 5.99, "ilosc": 25}, 
    "kawa": {"cena": 24.99, "ilosc": 8}
}

magazyn["mleko"]["ilosc"] -= 3

magazyn["chleb"]["ilosc"] += 12

magazyn["herbata"] = {
    "cena": 11.49,
    "ilosc": 15
}

removed = magazyn.pop("kawa")

print(f"Wycofano kawę o wartości: {removed["cena"]*removed["ilosc"]} zł")

print(f"Produkty: {sorted(magazyn.keys())}")

mleko_wartosc = magazyn["mleko"]["ilosc"] * magazyn["mleko"]["cena"]
chleb_wartosc = magazyn["chleb"]["ilosc"] * magazyn["chleb"]["cena"]

print(f"Mleko: {magazyn["mleko"]["ilosc"]} szt., {mleko_wartosc} zł; Chleb: {magazyn["chleb"]["ilosc"]} szt., {chleb_wartosc} zł", )

#print(magazyn["cukier"])
# KeyError, ponieważ taki klucz nie istnieje w słowniku

print(f"cukier: {magazyn.get("cukier", "brak produktu")}")
#bez błędu, zwraca brak produktu, bo nie ma takiego klucza w slowniku