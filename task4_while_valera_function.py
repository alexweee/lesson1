def find_person(name):
    x = 0
    while spisok[x] != name:
        print(spisok.pop(x))
        if spisok[x] == name:
            print("{} нашелся".format(name))
            break



spisok = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]


print(find_person("Валера"))
    



