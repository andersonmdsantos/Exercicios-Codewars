## My way
# def scramble(s1, s2):
#     s1_lista = list(s1)
#     for letra in s2:
#         if letra in s1_lista:
#             s1_lista.remove(letra)
#         else:
#             return False
#     return True

## IA
from collections import Counter

def scramble(s1, s2):
    return Counter(s2) <= Counter(s1)

teste = scramble("scripting", "scripts")
print(teste)