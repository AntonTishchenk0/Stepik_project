import random
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
from string import punctuation


chars = ''

try:
    count_pass = int(input('Введите количество генерируемых паролей от 1 до 100: '))
    if count_pass > 100:
        print('Превышено количество пароля!')
        count_pass = int(input('Введите цифру от 1 до 100: '))
except ValueError:
    print('Ошибка ввода, количество должно быть цифрой!')
    try:
        count_pass = int(input('Введите цифру от 1 до 100: '))
        if count_pass > 100:
            print('Превышено количество пароля!')
            count_pass = int(input('Введите цифру от 1 до 100: '))
    except ValueError:
        print('Ошибка ввода, количество должно быть цифрой!')
        count_pass = int(input('Введите цифру от 1 до 100: '))
        if count_pass > 100:
            print('Превышено количество пароля!')
            count_pass = int(input('Введите цифру от 1 до 100: '))

try:
    length_pass = int(input('Введите длину генерируемых паролей от 1 до 50: '))
    if length_pass > 50:
        print('Превышена длина пароля!')
        length_pass = int(input('Введите цифру от 1 до 50: '))
except ValueError:
    print('Ошибка ввода, количество должно быть цифрой!')
    try:
        length_pass = int(input('Введите цифру от 1 до 50: '))
        if length_pass > 50:
            print('Превышена длина пароля!')
            length_pass = int(input('Введите цифру от 1 до 50: '))
    except ValueError:
        print('Ошибка ввода, количество должно быть цифрой!')
        length_pass = int(input('Введите цифру от 1 до 50: '))
        if length_pass > 50:
            print('Превышена длина пароля!')
            length_pass = int(input('Введите цифру от 1 до 50: '))

use_digit = input('Использовать цифры в пароле от 1 до 9?\n'
                  'Введите да, yes, y или нет, no, n: ').lower()
if use_digit == 'да' or use_digit == 'y' or use_digit == 'yes':
    chars += digits
elif use_digit == 'нет' or use_digit == 'n' or use_digit == 'no':
    print('Продолжим подбор!')
else:
    print('Что-то на непонятном! Мне это не нужно знать!')
    print('Продолжим подбор пароля!')

use_uppercase = input('Использовать заглавные буквы в пароле?\n'
                      'Введите да, yes, y или нет, no, n:  ').lower()
if use_uppercase == 'да' or use_uppercase == 'y' or use_uppercase == 'yes':
    chars += ascii_uppercase
elif use_uppercase == 'нет' or use_uppercase == 'n' or use_uppercase == 'no':
    print('Продолжим подбор пароля!')
else:
    print('Что это? Мне оно для чего?')
    print('Продолжим подбор пароля!')

use_lowercase = input('Использовать строчные буквы в пароле?\n'
                      'Введите да, yes, y или нет, no, n:  ').lower()
if use_lowercase == 'да' or use_lowercase == 'y' or use_lowercase == 'yes':
    chars += ascii_lowercase
elif use_lowercase == 'нет' or use_lowercase == 'n' or use_lowercase == 'no':
    print('Продолжим подбор пароля!')
else:
    print('Ну что снова?')
    print('Продолжим подбор пароля!')

use_symbol = input('Использовать символы "!#$%&*+-=?@^_" в пароле?\n'
                   'Введите да, yes, y или нет, no, n:  ').lower()
if use_symbol == 'да' or use_symbol == 'y' or use_symbol == 'yes':
    chars += punctuation
elif use_symbol == 'нет' or use_symbol == 'n' or use_symbol == 'no':
    print('Продолжим подбор пароля!')
else:
    print('Ну что снова?')
    print('Продолжим подбор пароля!')

not_use_ambiguous_symbol = input('Использовать неоднозначные символы?\n'
                                 'Введите да, yes, y или нет, no, n: ').lower()
if not_use_ambiguous_symbol == 'нет' or not_use_ambiguous_symbol == 'no' or not_use_ambiguous_symbol == 'n':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


def generate_password(length, char):
    lst_pass = []
    password = ''
    for _ in range(count_pass):
        for _ in range(length_pass):
            if len(password) != length:
                password += random.choice(char)
    lst_pass.append(password)
    return lst_pass


for c in range(count_pass):
    print('Ваш новый пароль: ', *generate_password(length_pass, chars))
