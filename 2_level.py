def exponentintation(number, degree):
    if degree > 0:
        result = number * exponentintation(number, degree - 1)
        return result
    else:
        return 1

def allVariantExponentiation(number, degree):
    if degree == 0:
        return 1
    elif degree > 0:
        return exponentintation(number, degree)
    else:
        res = float(1 / exponentintation(number, abs(degree)))
        return res

number = int(input("Введіть число: "))
degree = int(input("Введіть степінь: "))

print(allVariantExponentiation(number, degree))
