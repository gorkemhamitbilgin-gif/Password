import random

# Karakter setleri
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "+-/*!&$#?=@"

print("=== Parola Oluşturucu ===")

# Kullanıcı seçenekleri
length = int(input("Parola uzunluğu: "))
use_lower = input("Küçük harf olsun mu? (e/h): ").lower()
use_upper = input("Büyük harf olsun mu? (e/h): ").lower()
use_numbers = input("Rakam olsun mu? (e/h): ").lower()
use_symbols = input("Sembol olsun mu? (e/h): ").lower()

# Karakter havuzu
char_pool = ""

if use_lower == "e":
    char_pool += lower
if use_upper == "e":
    char_pool += upper
if use_numbers == "e":
    char_pool += numbers
if use_symbols == "e":
    char_pool += symbols

# Eğer havuz boşsa uyar
if char_pool == "":
    print("Hiçbir karakter türü seçmedin! Parola oluşturulamadı.")
    exit()

# Parola oluşturma
password = ""
for i in range(length):
    password += random.choice(char_pool)

# Sonuç
print("\nOluşturulan Parola:", password)
