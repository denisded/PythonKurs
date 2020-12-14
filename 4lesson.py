from functools import reduce
from itertools import count, cycle
from math import factorial
from sys import argv
from time import sleep


# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
#     В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
#     Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

def zp(virobotka, stavka, premia):
    return virobotka * stavka + premia

file, virobotka, stavka, premia = argv
print(zp(int(virobotka), int(stavka), int(premia)))

# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
#     значения которых больше предыдущего элемента.
#     Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
#     Для формирования списка использовать генератор.
#     Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
#     Результат: [12, 44, 4, 10, 78, 123].

list2 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 301]
newlist2 = [el for el in list2 if el > list2[list2.index(el)-1]]
print(newlist2)

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
#   Подсказка: использовать функцию range() и генератор.

print([el for el in range(20, 241) if (el % 20 == 0 or el % 21 == 0)])

# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
#   Сформировать итоговый массив чисел, соответствующих требованию.
#   Элементы вывести в порядке их следования в исходном списке.
#   Для выполнения задания обязательно использовать генератор.
#   Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
#   Результат: [23, 1, 3, 10, 4, 11]

list4 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([el for el in list4 if list4.count(el) == 1])

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
#   В список должны войти четные числа от 100 до 1000 (включая границы).
#   Необходимо получить результат вычисления произведения всех элементов списка.
#   Подсказка: использовать функцию reduce().


def multiplay(a, b):
    return a * b


list5 = [el for el in range(100, 1000) if el % 2 == 0]
print(reduce(multiplay, list5))

# 6. Реализовать два небольших скрипта:
#   а) итератор, генерирующий целые числа, начиная с указанного,
#   б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#   Подсказка: использовать функцию count() и cycle() модуля itertools.
#   Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#   Необходимо предусмотреть условие его завершения.
#   Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
#   Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

listn = []
n = int(input("Введите число для старта последовательности "))
print("Выведем последовательность")
for i in count(n):
    print(i)
    listn.append(i)
    sleep(0.2)
    if i == n + 3:
        break

print("Теперь цикличность")
j = 0
for i in cycle(listn):
    print(i)
    sleep(0.2)
    j += 1
    if j == n ** n:
        break

# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
#   При вызове функции должен создаваться объект-генератор.
#   Функция должна вызываться следующим образом: for el in fact(n).
#   Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
#   начиная с 1! и до n!.
#   Подсказка: факториал числа n — произведение чисел от 1 до n.
#   Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def fact7(n7):
    for el in range(1, n7+1):
        yield factorial(el)


n7 = int(input("Введите число "))
for el in fact7(n7):
    print(el)
