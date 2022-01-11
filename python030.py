# Ejercicio 30: Calcular el máximo común divisor(MCD) de dos números

def mcd(x, y):
    mcd = 1

    if x % y == 0:
        return y

    for k in range(int(y/2), 0, -1):
        if x % k == 0 and y % k == 0:
            mcd = k
            break

    return mcd


print(mcd(10, 9))
print(mcd(9, 20))
print(mcd(1, 9))
print(mcd(50, 20))
