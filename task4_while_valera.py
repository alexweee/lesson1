spisok = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]


x = 0
while spisok[x] != "Валера":
    print(spisok.pop(x))
#    print(spisok[x])
    
    if spisok[x] == "Валера":
        print("Валера нашелся")
        break

    



