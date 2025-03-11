def computeGCD(x, y):
    while y:
        x, y=y, x%y
    return x

result=computeGCD(3, 6)
print(result)