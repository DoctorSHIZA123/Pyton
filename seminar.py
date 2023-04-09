# Семинар 1
# Задача 1
...
# n = int(input("Введите 1-е расстояние "))
# m = int(input("Введите 2-е расстояние "))
# t = (m + n - 1) // n
# print(t)
...
# Задача 2
# frst = int(input('Первый класс >>> '))  # Ввод колличества 1-го класса
# sec = int(input('Второй класс >>> '))   # Ввод колличества 1-го класса
# thrd = int(input('Третий класс >>> '))  # Ввод колличества 1-го класса
# sum = ((frst+1) // 2) + ((sec+1) // 2) + ((thrd+1) // 2) 
# print(sum)

# Задача 3
# n = int(input())
# m = int(input())
# if n - m == 0:
#     c = 0
# else:
#     c = (n + m) - 1
# print(c)

# Задача 4
year = int(input('Ввод года '))
if year%4==0 and year%100!=0  or year%400==0:
    print('YES')
elif year//100==0:
    print('NO')
else:
    print('NO')    


# n = "World"
# print(n)


