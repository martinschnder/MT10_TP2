def lucas(s):
    n = pow(2, s) - 1
    if s % 2 == 0:
        print("Veuillez entrer un nombre impair")
        return false
    L = 4
    for i in range(s - 2):
        L = pow(L, 2) - 2
    if (L % n == 0):
        return true
    else: return false

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
    if n == 1: return (mod(x, N))
    else: 
        if (n % 2 == 0):
            return dicho_rec(x*x, n/2)
        else: return x*dicho_rec(x*x, (n-1)/2)