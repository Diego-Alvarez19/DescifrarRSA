import math
import random

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

# Factorización metodo de Pollard
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def funtion_factor(N, x):
    return (pow(x, 2) + 1) % N

def method_pollard(N): #max_iterations=50000
    x = (random.randint(0, 2) % (N - 2))
    y = x
    d = 1
    #iteration = 0

    while d == 1:
        #Función iterativa aplicada a x y y
        x = funtion_factor(N, x)
        y = funtion_factor(N, funtion_factor(N, y))

        # Calcula el MCD de la diferencia entre x e y
        d = gcd(abs(x - y), N)
        #iteration += 1 

        '''if iteration >= max_iterations:
            print(f"No se pudo encontrar un factor después de {max_iterations} iteraciones.")
            return 'failure' '''
        # retry if the algorithm fails to find prime factor
        # with chosen x and c 
        if (d == N):
            return method_pollard(N)

    return d, N // d

#################Metodo de Primos pequenos########################
# Método de Criba de Eratóstenes para generar primos pequeños
def sieve_of_eratosthenes(limit):
    """Genera una lista de números primos hasta un límite dado usando la Criba de Eratóstenes."""
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if (is_prime[p]):
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if is_prime[p]]

# Método de factorización por primos pequeños
def small_prime_factorization(n):
    """Factoriza n utilizando la división por primos."""
    factors = []
    primes = sieve_of_eratosthenes(int(n**0.5) + 1)  # Solo necesitamos primos hasta sqrt(n)

    for prime in primes:
        while n % prime == 0:  # Mientras n sea divisible por prime
            factors.append(prime)  # Agregar el factor
            n //= prime  # Dividir n por el primo
        if n == 1:  # Si n se convierte en 1, hemos terminado
            break

    if n > 1:  # Si queda un número mayor que 1, es un primo
        factors.append(n)

    return factors

    
# Calculo de d
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def calc_d(e, phi_n):
    gcd, x, y = extended_gcd(e, phi_n)
    if gcd != 1:
        raise ValueError("No existe el inverso multiplicativo")
    else:
        return x % phi_n

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