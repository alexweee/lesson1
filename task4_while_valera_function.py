def find_person(name, spisok):
    x = 0
    while spisok[x] != name:
        print(spisok.pop(x))
        if spisok[x] == name:
            return "{} нашелся".format(name)
            break



list_of_names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]


print(find_person("Валера", list_of_names))
    



