def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def inverseMod(a, b):
    #return  pow(a, -1, b) #funciona en python > 3.8
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
  return PowMod(ciphertext, inverseMod(exponent, (p-1)*(q-1) ) , p*q)
  
p = 1000000007
q = 1000000009
e = 23917
modulo = p * q

  
m = int(input())
ciphertext = encode(m, modulo, e)
cleartext = decode(ciphertext, p, q, e)
print(f"cifrado: {ciphertext}, mensaje: {cleartext}")
