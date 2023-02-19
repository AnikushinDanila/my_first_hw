'''
Задача №1
====> if else
Дано натуральное число N. Если число N двузначное,
то найти сумму цифр числа. Если число N трехзначное,
то найти произведение ненулевых цифр числа,
иначе написать, что число неподходящее.
In: 400
Out: 4
'''

# n = input('Введите натуральное число: ')
# попытка №1
if len(n) == 2:
    print('summa =', int(n[0]) + int(n[1]))
elif len(n) == 3:
    if not n[0]:
        n[0] = 1
    if not n[1]:
        n[1] = 1
    if not n[2]:
        n[2] = 1
    print(int(n[0]) * int(n[1]) * int(n[2]))
else:
    print('wrong number')
# еще вариант
# val = int(input('Введите натуральное число\n>'))
# numbers = len(str(val))

# if numbers == 2:
#     print(val % 100 // 10 + val % 10)
# elif numbers == 3:
#     hundreds = val // 100
#     tens = val % 100 // 10
#     ones = val % 10
#     if not tens:
#         tens = 1
#     if not ones:
#         ones = 1
#     print(hundreds * tens * ones)
# else:
#     print("Неподходящее число")

# попытка №2
# if len(n) == 2:
#     summ = n[0] + n[1]
# elif len(n) == 3:
#     if n[0] != 0:
#
# else:
#     print(f"Число {n} неподходящее")




"""
Дана строка из двух слов. Поменяйте эти слова местами.
Пример:
In: 'Hello Python'
Out: 'Python Hello'
"""
# №1
# s = input('Введите строку из двух слов: ')
# a = s.split()
# b = a[::-1]
# ' '.join(b)
# print(*b)#звездочка раскрывает список

# №2
# s = ' '.join(input('Введите строку из двух слов: ').split(' ')[::-1])
# print(s)

"""
Задача №3
========> while
Строка из нескольких слов, не более 10.
Определите, сколько букв содержит самое длинное слово в строке.
Пример:
In: Как дела в учебе
Out: 5
"""
# active = True
# while active:
#     msg = input('Введите слова из нескольких букв: ').split(' ')
#     print(msg)
#     for x in msg:
#         print (len(x))

    # for x in msg:
    #     a = len(x[0])
    #     if msg[x] > a:
    #         a = msg[x]
    #         print(a)
    # pass

# просмотри такое решение
my_string = input("Введите строку из несколькиих слов (не более  10): ")
my_string += ' ' # Чтобы обработать последнее слово, добавляем пробел к строке
max_len = index = word_len = 0

while index < len(my_string):
    if my_string[index] != " ":
        word_len += 1
    else:
        if word_len > max_len:
            max_len = word_len
        word_len = 0
    index += 1

print(f"Самое длинное слово содержит {max_len} букв.")


"""
Задача №4
=====> while
Дано слово из символов(латинские буквы + цифры), других символов нет.
Нужно вывести новой строкой только цифры, если они есть или
написать, что их нет.
Пример: 
In: 'antuh1ouou21au3'
Out: 1213

In: 'sauhsauhasnhuasnhu'
Out: 'no digits'
"""
# active = True
# while active:
#     s = input('Введите строку: ')
#     for x in s:
#         if x.isdigit():
#             print(x)


