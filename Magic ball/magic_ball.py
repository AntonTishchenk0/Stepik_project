import random

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Введите ваше имя!\n')
print(f'Привет, {name}!')

question = input('Введите ваш вопрос: ')
while question != 'стоп':
    res = random.choice(answers)
    print(res)
    says = input('Хотите продолжить? Введите да: ').lower()
    if says == 'да':
        question = input('Введите ваш вопрос: ')
    else:
        print('Возвращайся если возникнут вопросы!')
        break
