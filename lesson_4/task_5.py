# 5. Lista mailingowa bez duplikatów — Dla zapisy = ["ola@wp.pl", "jan@onet.pl", "ola@wp.pl",
# "ewa@gmail.com", "jan@onet.pl", "ola@wp.pl"] wyświetl liczbę zapisów, liczbę unikalnych adresów,
# posortowane unikalne adresy i liczbę zapisów ola@wp.pl 

zapisy = ["ola@wp.pl", "jan@onet.pl", "ola@wp.pl",
"ewa@gmail.com", "jan@onet.pl", "ola@wp.pl"]

unique = set(zapisy)

print(f"Zapisów: {len(zapisy)}, unikalnych: {len(unique)}")
print(unique)

count_adress = 0

for adress in zapisy:
    if adress == "ola@wp.pl":
        count_adress += 1
        
print(f"ola@wp.pl: {count_adress} razy")