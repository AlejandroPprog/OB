def EsNumPrimo(n):
    for num in range(2, n):
        if n % num == 0:
            print("No es primo")
            return False
    print("Es primo")
    return True

print(EsNumPrimo(5))
print(EsNumPrimo(10))
print(EsNumPrimo(381))