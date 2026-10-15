# 9. Normalizacja e-maila — adres " Jan.Kowalski@Gmail.COM " oczyść i zapisz małymi literami, sprawdź
# in , czy zawiera @ , i rozdziel split("@") na login i domenę.

email_raw = " Jan.Kowalski@Gmail.COM "
email = email_raw.strip().lower()
    
print(f"E-mail: {email}")
print(f"Zawiera @: {'@' in email}")

if '@' in email:
    splitted_email = email.split('@')
    
print(f"Login: {splitted_email[0]}")
print(f"Domena: {splitted_email[1]}")