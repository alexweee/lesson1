AGE = int(input("Введите свой возраст для определения занятости: "))

def age_function(a):
    if 6 >= a >= 0:
        return "Детский сад"
    elif 17 >= a >= 7:
        return "Школа"
    elif 24 >= a >= 18:
        return "ВУЗ"
    elif 100 >= a >= 25:
        return "ВУЗ"
    else:
        return "Введите корректный возраст"

RESULT= age_function(AGE)

print(RESULT)
