def factorial (n : int):
    res = 1

    for i in range (2, n+1)
        res *= i

    return res

def comb(n: int, k: int):
    return factorial(n) // (factorial(n-k) * factorial(k))

def main():
    n,k = list(map(int, input(.split())))
 print (comb(n,k))