def int32_to_ip(int32):
    return '.'.join(str((int32 >> (8 * i)) & 0xFF) for i in reversed(range(4)))

# int32 >> (8 * i) move os bits para a direita em blocos de 8 (um byte).

# & 0xFF isola apenas os 8 bits do byte atual.

# reversed(range(4)) garante a ordem correta (do byte mais significativo ao menos).

variavel = int32_to_ip(0)
print(variavel)
