import math

# Método de Fermat para factorizar n
def fermatFactor(n):
    x = math.isqrt(n) + 1  # Primer x tal que x^2 >= n
    y2 = x * x - n  # y^2 = x^2 - n
    y = math.isqrt(y2)
    
    # Repetimos hasta que y^2 sea un cuadrado perfecto
    while y * y != y2:
        x += 1
        y2 = x * x - n
        y = math.isqrt(y2)
    
    # Cuando encontramos, devolvemos p y q
    p = x - y
    q = x + y
    return p, q

# Probamos el método de Fermat en la implementación RSA existente
#####################################################################Implementacion RSA Tarea####################################################################

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def inverseMod(a, b):
    g, x, y = egcd(a, b)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % b

def PowMod(base, exp, mod):
    return pow(base, exp, mod)

def encode(message, modulo, exponent):  
    return PowMod(message, exponent, modulo)

def decode(ciphertext, p, q, exponent):
    return PowMod(ciphertext, inverseMod(exponent, (p-1)*(q-1)), p*q)

# Parámetros RSA
p = 1000000007
q = 1822222109
e = 23917
modulo = p * q

m = int(input("Mensaje a cifrar (como número entero): "))
ciphertext = encode(m, modulo, e)

########################################################################################################################################

# Intento de factorizar el módulo con Fermat
print("Intentando factorizar el módulo con Fermat...")
p_fact, q_fact = fermatFactor(2047)
print(f"Factores encontrados: p = {p_fact}, q = {q_fact}")

# Intento de descifrar usando los factores encontrados
cleartext = decode(ciphertext, p_fact, q_fact, e)
print(f"Cifrado: {ciphertext}, Mensaje descifrado Fermat: {cleartext}")