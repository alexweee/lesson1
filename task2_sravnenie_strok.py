FIRST_STRING = input("Введите первую строку: ")
SECOND_STRING = input("Введите вторую строку: ")


def Sravnen(a, b):
    
    if type(a) != str or type(b) !=str:
        return 0
    elif a == b:
        return 1
    elif (len(a) > len(b)) and b != "learn":
        return 2
    elif (len(a) != len(b)) and b == "learn":
        return 3


result = Sravnen(FIRST_STRING, SECOND_STRING)

print(result)