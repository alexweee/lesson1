dictionary = {"как дела?": "Хорошо!", "что делаешь?": "Программирую", "лох?": "лох"}

def podstava(x):
    otvet = dictionary[x]
    print(otvet)

def get_answer(answer):
    while True:
        try:
            user_input_raw = input(answer)
            user_input = str(user_input_raw.lower())
        except KeyboardInterrupt:
            print("пока")
            break

        if user_input == "пока":
            print("Пока")
            break
        elif user_input in dictionary:
            podstava(user_input)
        else:
            print("норм")


get_answer("Введите свой вопрос:")