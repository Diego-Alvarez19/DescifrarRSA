import math

# Método de Fermat para factorizar n
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

# Inverso modular usando el algoritmo extendido de Euclides
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

# Exponenciación modular rápida
def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

# Descifrado del mensaje
def decrypt_message(ciphertext, d, n):
    cipherlist = ciphertext.split("␟")
    message_prepared = [int(cipher) for cipher in cipherlist]
    message_encoded = [mod_exp(c, d, n) for c in message_prepared]
    message_decrypted = "".join(chr(c) for c in message_encoded)
    return message_decrypted

# Captura de valores de Wireshark (ejemplo)
n = 35183 # Sustituye este valor por el capturado
e = 133    # Sustituye este valor por el capturado
ciphertext = "11799␟30892␟7217␟5867␟10274␟1070␟3211␟30232␟10376␟10274␟5867␟30892␟24534␟30232␟21724␟1070␟21301␟10274␟13857␟30232␟21724␟1070␟30232␟32289␟5074␟30892␟30232␟21093␟7217␟32289␟21724␟34249␟30892␟30232␟20088␟21724␟30232␟11799␟30892␟21093␟21301␟32289␟7217␟30892␟11799␟16535␟10274␟5074␟8813␟8813"  # Sustituye este valor por el mensaje capturado

# Factorización de Fermat
p, q = fermat_factor(n)
print(f"p = {p}, q = {q}")

# Calcular φ(n) y d
phi_n = (p - 1) * (q - 1)
d = mod_inverse(e, phi_n)
print(f"d = {d}")

# Descifrar el mensaje
message = decrypt_message(ciphertext, d, n)
print(f"Decrypted message: {message}")
