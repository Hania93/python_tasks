# 6. Paragon z groszami — kupiono: zeszyt 4.99 zł × 1, segregator 7.49 zł × 1, długopis 3.29 zł × 2 (produkt w
# jednej linii: nazwa1, cena1, ilosc1 = ... ). Wypisz „surową” sumę, zaokrąglij ją i wydrukuj paragon; VAT
# zawarty w cenie to suma * 23 / 123 .

items = [
    {
        "name": "notebook",
        "price": 4.99,
        "amount": 1 
    },
    {
        "name": "ring_binder",
        "price": 7.49,
        "amount": 1 
    },
    {
        "name": "pen",
        "price": 3.29,
        "amount": 2 
    }
]

total_sum = 0

for item in items:
    item["sum"] = item.get("price", 0) * item.get("amount", 0)
    
    total_sum += item["sum"]
    
vat = total_sum * 23 / 123

print(total_sum)

print(f"{'Produkt':<15} {'Ilość':>6} {'Wartość':>10}")

for item in items:
    print(f"{item.get('name', ''):<15} {item.get('amount', 1):>6} {item.get('sum', 0):>10.2f}")
    
print('-' * 33)
print(f"RAZEM: {round(total_sum, 2):>26.2f}")
print(f"w tym VAT 23% {round(vat, 2):>19.2f}")