
import random

def cut_cake(people):
    try:
        parts_1 = 1 / people
        print(f'Каждый человек получит {parts_1} пирога')
    except:
        print("Не надо")

while True:
    p = random.randint(1, 10)
    cut_cake(p)