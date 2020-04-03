fileWithNumbers = open("file_for_3_level.txt", "r")

symbolForEnd = input("Ведіть символ: ")

for x in fileWithNumbers:
    if x.endswith(symbolForEnd,0,-1):
        print(x[0:-1].swapcase())
        continue
    elif x.endswith(symbolForEnd):
        print(x.swapcase())