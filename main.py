import string
import math
from collections import Counter

alf = string.ascii_lowercase


def decrypt(text, rot):
    output = ""
    for k in text:
        if not k.isalpha():
            output+= k
            continue
        ind = alf.index(k.lower())
        new_c = alf[ind - rot % 25]
        output += new_c.upper() if k.isupper() else new_c
    return output

FREQ = {"e": 12.7, "t": 9.06, "a": 8.17, "o": 7.51, "i": 6.97,
        "n": 6.75, "s": 6.33, "h": 6.09, "r": 5.99, "d": 4.25,
        "l": 4.03, "c": 2.78, "u": 2.76, "m": 2.41, "w": 2.36,
        "f": 2.23, "g": 2.02, "y": 1.97, "p": 1.93, "b": 1.29,
        "v": 0.98, "k": 0.77, "j": 0.15, "x": 0.15, "q": 0.1,
        "z": 0.07
       }


def difference(t):
    counter = Counter(t)
    return sum([abs(counter.get(letter,0) * 100 / len(t) - FREQ[letter]) for letter in alf ])

def break_cipher(msg):
    lowest_dif = 99999
    enc_key = 0
    a = [difference(decrypt(msg,x)) for x in range(1,len(alf))]
    return a.index(min(a))+1

    
            
crypted_txts = ["Hyhubwklqj wkdw kdv d ehjlqqlqj kdv dq hqg","Jkxkzu ateopo kj lqnlkoa. Jkxkzu xahkjco wjusdana. Aranuxkzu’o ckjjw zea. Ykia swpyd PR?","Dqiwj xaejco wna w zeoawoa, ywjyan kb pdeo lhwjap."]
for metin in crypted_txts:
    rot = break_cipher(metin)
    print(f"{decrypt(metin,rot)} rot = {rot}")
    print(50 * "*")
