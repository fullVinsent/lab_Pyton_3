def sumOfStructure(number, times):
    if times > 0:
        result = pow(number, times) + sumOfStructure(number, times - 1)
        return result
    elif times == 0:
        return 1
    else:
        return "error"

number = int(input("Введіть число: "))
times = int(input("Введіть n: "))

print("1+"+str(number)+"+"+str(number)+"^2+...+"+str(number)+"^"+str(times)+" = "+str(sumOfStructure(number,times)))