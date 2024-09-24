import math

# Factorización de Fermat
def fermat_factor(n):
    x = math.isqrt(n) + 1
    y2 = x * x - n

    while y2 < 0:
        x += 1
        y2 = x * x - n

    y = math.isqrt(y2)

    while y * y != y2:
        x += 1
        y2 = x * x - n
        y = math.isqrt(y2)

    p = x + y
    q = x - y
    return p, q






# EJEMPLO DE UN NUEVO METODO A IMPLEMENTAR (ACA SE DEBE PONER)
# Método de factorización por división por prueba
def trial_division_factor(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return i, n // i
    raise ValueError("Factorization failed")

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def decrypt_message(ciphertext, d, n):
    cipherlist = ciphertext.split("␟")
    message_prepared = [int(cipher) for cipher in cipherlist]
    message_encoded = [mod_exp(c, d, n) for c in message_prepared]
    message_decrypted = "".join(chr(c) for c in message_encoded)
    return message_decrypted