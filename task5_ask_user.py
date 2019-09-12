
def ask_user(question):
    while True:
        user_input_raw = input(question)
        user_input = str(user_input_raw.lower())
        if user_input == "хорошо":
            print("OK")
            break
        else:
            print("Пробуем еще раз")

def get_answer(answer):
    while True:
        user_input_raw = input(answer)
        user_input = str(user_input_raw.lower())
        if user_input == "пока":
            print("Пока")
            break
        if user_input == ("как твои?" or "а как твои?" or "а как твои дела?" or "а твои как?"):
            print("Мои тоже хорошо")
        else:
            print("норм")


ask_user("Как дела?")

get_answer("Введите свой вопрос:")