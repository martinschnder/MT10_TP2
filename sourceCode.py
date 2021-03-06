def lucas(s):
    n = pow(2, s) - 1
    if s % 2 == 0:
        print("Veuillez entrer un nombre impair")
        return False
    L = 4
    for i in range(s - 2):
        L = pow(L, 2) - 2
    if (L % n == 0):
        return True
    else: return False

def naif_iter(x, n):
    res = 1
    for i in range(n):
        res = res *x
    return res

def naif_rec(x, n):
    if n == 1: return x
    else: return(x * naif_rec(x, n-1))

def dicho_rec(x, n):
    if n == 1: return x
    else: 
        if (n % 2 == 0):
            return dicho_rec(x*x, n/2)
        else: return x*dicho_rec(x*x, (n-1)/2)

def dicho_rec_mod(x, n, N):
    if n == 1: return mod(x,N)
    else: 
        if (n % 2 == 0):
            return dicho_rec_mod(x*x, n/2, N)
        else: return x*dicho_rec_mod(x*x, (n-1)/2, N)

def chooseSize(l, N):
    for size in reversed(range(floor(ln(N)/ln(2) + 1))):
        if l * 8 % size == 0:
            return size

def numerise(message, N):
    result = []
    binaryMessage = BinaryStrings().encoding(message)
    size = chooseSize(len(message), N)
    for i in range(0, len(binaryMessage), size):
        sum = 0
        for j in range(size):
            sum += int(str(binaryMessage[i+j])) * pow(2, size - j - 1)
        result.append(sum)
    result.append(size)
    return result

def toBin(n, size):
    res = bin(n)[2:]
    if len(res) < size:
        res = (size-len(res))*'0' + res
    return res

def alphabetise(message, N) :
    result = []
    size = message.pop(-1)
    for digit in message:
        result.append(toBin(int(digit), size))
    binaryMessage = ''.join(result)
    alphabeticMessage = ''
    for i in range(0, len(binaryMessage), 8):
        alphabeticMessage = alphabeticMessage + chr(int(binaryMessage[i:8+i], 2))
    return(alphabeticMessage)

import random
def cleRSA (m):
    result = {}
    result["p"] = chooseP(m)
    result["q"] = chooseQ(m, result["p"])
    result["e"] = chooseE(result["p"], result["q"])
    result["N"] = result["p"]*result["q"]
    result["d"] = inv_modulo(result["e"], (result["p"]-1)*(result["q"]-1))
    result.pop("p")
    result.pop("q")
    return result

def inv_modulo(x, m):
    (p, u, v) = xgcd(x, m)
    if p == 1: return u % abs(m)
    else: raise Exception("%s et %s ne sont pas premiers entre eux" % (x, m))

def chooseP(m):
    return randPremier(int((1 / sqrt(2)) * pow(2,m/2)), int(pow(2,m/2)))

def chooseQ(m, p):
    while True:
        q = randPremier(int(1/sqrt(2)*pow(2,m/2)),int(pow(2,m/2)))
        if q != p:
            return q

def chooseE(p, q):
    phi = (p-1)*(q-1)
    while 1:
        e = randint(1, phi)
        if gcd(e, phi) == 1 :
            return e

def protocole1(message, signature, Na, Nb, Nc = 256, ea = 0, eb = 0, da = 0, db = 0):
    if 3 * Nc >= Na or 3 * Nc >= Nb:
        print("Veuillez rentrez une valeur plus petite pour Nc")
        return 1
    if da and eb:
        m1c = numerise(message, 3 * Nc)
        s1c = numerise(signature, 3 * Nc)
        m2c = encode_rsa(m1c, eb, Nb)
        s2c = encode_rsa(s1c, da, Na)
        print("Message et signature cryptes")
        return(m2c, s2c)
    if db and ea:
        m1c = decode_rsa(message, db, Nb)
        s1c = decode_rsa(signature, ea, Na)
        m1 = alphabetise(m1c, 3 * Nc)
        s1 = alphabetise(s1c, 3 * Nc)
        print("Message et signature decryptes")
        print(m1, s1)
        return(m1, s1)

def protocole2(message, Na, Nb, Nc = 256, ea = 0, eb = 0, da = 0, db = 0):
    if 3 * Nc >= Na or 3 * Nc >= Nb:
        print("Veuillez rentrez une valeur plus petite pour Nc")
        return 1
    if Na > Nb:
        if da and eb:
            m1c = numerise(message, 3 * Nc)
            m2c = encode_rsa(m1c, eb, Nb)
            m3c = encode_rsa(m2c, da, Na)
            return m3c
        if db and ea:
            m2c = decode_rsa(message, ea, Na)
            m1c = decode_rsa(m2c, db, Nb)
            m1 = alphabetise(m1c, 3* Nc)
            return m1
    if Na < Nb:
        if da and eb:
            m1c = numerise(message, 3 * Nc)
            m2c = encode_rsa(m1c, da, Na)
            m3c = encode_rsa(m2c, eb, Nb)
            return m3c
        if db and ea:
            m2c = decode_rsa(message, db, Nb)
            m1c = decode_rsa(m2c, ea, Na)
            m1 = alphabetise(m1c, 3* Nc)
            return m1
      
def factorisationRSA (N):
    L0 = 1
    u = 0
    n = L0+u
    L = 1
    R0 = ceil(sqrt(L*N))
    R = R0 + u
    S = sqrt(R^2-L*N)
    while floor(S) != S :
        for L in range(L0, n+1) :
            u = n-L
            R0 = ceil(sqrt(L*N))
            R = R0+u
            S = sqrt(R^2-L*N)
        n = n+1
        L0 = L
    print("PCGD(N,R-S) = ", gcd(N,int(R-S)), "\nPGCD(N,R+S) = ", gcd(N,int(R+S)))
    
def testPrimaliteFermat(n,l) :
    for _ in range(l):
        a = randint(1,n-1)
        if pow(a,n-1,n) != 1:
            return False
    return True

def testPrimaliteMillerRabin(n, l):
    if n == 2 or n == 3 :
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(l):
        a = randint(2, n - 1)     
        d = pow(a, s, n)            
        if d == 1 or d == n - 1:
            continue                
        for _ in range(r - 1):      
            d = pow(d, 2, n)        
            if d == n - 1:
                break               
        else:
            return False            
    return True

for n in range(10):
    if (not is_prime(pow(2, 2^n) + 1)):
        print(n, pow(2, 2^n ) + 1)


mersenne=[]
for p in prime_range(258):
    mersenne.append(pow(2,p)-1)
    
for index, value in enumerate(mersenne):
    if (is_prime(value)):
        print(prime_range(258)[index], end=",")
        
        
def is_parfait(n, p):
    if (pow(2,p-1)*(pow(2,p)-1))==n:
        return True
    else: 
        return False
    
p=0
for index, value in enumerate(mersenne):
    if (is_prime(value)):
        p = prime_range(258)[index]
        print("Mp premier pour p =", p)
        print("parfait ?", is_parfait(pow(2,p-1)*value,p))
        
def dicho_iteratif(x, n):
    y = 1
    while (n > 0):
        if (n%2 == 0):
            x = x*x
            n = n/2
        else: 
            y = y*x
            x = x*x
            n = (n-1)/2
    return y

def encode_rsa(message, e, N):
    return map(lambda x: power_mod(int(x), int(e), int(N)), message)

def decode_rsa(cipher, d, N):
    return list(map(lambda x: power_mod(x, int(d), int(N)), cipher))

def randPremier(start, end):
    while 1:
        nombre = randint(start, end)
        if is_prime(nombre) : 
            return nombre
        
def toBin(n, size):
    res = bin(n)[2:]
    if len(res) < size:
        res = (size-len(res))*'0' + res
    return res