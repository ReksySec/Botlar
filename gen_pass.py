import random

def sifre(parola_uzunlugu):
    karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    parola = ""

    for i in range(parola_uzunlugu):
        parola += random.choice(karakterler)

    
    return parola
