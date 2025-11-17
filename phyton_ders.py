import random

# 1) Parolada kullanılacak tüm karakterler
chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# 2) Kullanıcıdan parolanın uzunluğunu al
password_length = int(input("Parola uzunluğunu gir: "))

# 3) Oluşturulan parolayı saklayacağımız değişken
password = ""

# 4) Döngü ile rastgele karakter seç ve parolaya ekle
for i in range(password_length):
    password += random.choice(chars)

# 5) Parolayı ekrana yazdır
print("Oluşturulan Parola:", password)