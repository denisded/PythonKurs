# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
#   вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

while True:
    a1 = input("Введи даные для записи в файл ") + "\n"
    if a1 == "\n":
        break
    with open("file1.txt", "a") as file1:
        file1.write(a1)

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
#   выполнить подсчет количества строк, количества слов в каждой строке.

with open("file2.txt", "r") as file2:
    kolvoslov = 1
    for i in file2:
        print("Кол-во символов в", kolvoslov, "строке:", len(i)-1)
        kolvoslov += 1
print("Количество строк:", kolvoslov - 1)

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#   Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
#   Выполнить подсчет средней величины дохода сотрудников.

with open("file3.txt", "r", encoding='utf-8') as file3:
    rab = file3.read().split('\n')
    rabdict = {}
    for i in rab:
        a3 = i.split(',')
        if int(a3[1]) < 20000:
            dicta3 = {a3[0]: a3[1]}
            rabdict.update(dicta3)
print(list(rabdict.keys()))

# 4. Создать (не программно) текстовый файл со следующим содержимым:
#   One — 1
#   Two — 2
#   Three — 3
#   Four — 4
#   Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
#   При этом английские числительные должны заменяться на русские.
#   Новый блок строк должен записываться в новый текстовый файл.

def rename(a):
    a4 = a.readline()
    listfile4 = []
    listfile4.append(a4.split(' '))
    strfile41 = ' '.join(list([rus.get(listfile4[0][0]), listfile4[0][1], listfile4[0][2]]))
    with open("file41.txt", "a") as file41:
        file41.write(strfile41)


rus = {"One": "один", "Two": "два", "Three": "три", "Four": "четыре"}
with open("file4.txt", "r", encoding='utf-8') as file4:
    rename(file4)
    rename(file4)
    rename(file4)
    rename(file4)

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#   Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

print("Стоп символ +")
listh = []
stopwhile = False
while stopwhile is False:
    for i in input("Введите строку чисел, разделенных пробелом ").split():
        if i == "+":
            stopwhile = True
            break
        else:
            with open("file5.txt", "a") as file5:
                file5.write(i+' ')
b5=[]
with open("file5.txt", "r") as file5:
    for i in file5:
        a5 = i.split()
        for j in a5:
            b5.append(int(j))
print(sum(b5))

# 6. Необходимо создать (не программно) текстовый файл,
#   где каждая строка описывает учебный предмет и наличие лекционных,
#   практических и лабораторных занятий по этому предмету и их количество.
#   Важно, чтобы для каждого предмета не обязательно были все типы занятий.
#   Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
#   Вывести словарь на экран.
#       Примеры строк файла:
#       Информатика: 100(л) 50(пр) 20(лаб).
#       Физика: 30(л) — 10(лаб)
#       Физкультура: — 30(пр) —
#
#       Пример словаря:
#       {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

dict6 = {}
with open("file6.txt", "r", encoding="utf-8") as file6:
    listfile6 = file6.read().split('\n')
    for i in listfile6:
        sumhours = 0
        predmet = i[:i.find(':'):]
        for j in i.split():
            if j.find('(') > 0:
                sumhours += int(j[:j.find('('):])
        dict6.update({predmet: sumhours})

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
#   название, форма собственности, выручка, издержки.
#       Пример строки файла: firm_1 ООО 10000 5000.
#   Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
#   Если фирма получила убытки, в расчет средней прибыли ее не включать.
#   Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
#   Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#       Пример списка:
#       [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#   Итоговый список сохранить в виде json-объекта в соответствующий файл.
#       Пример json-объекта:
#       [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
#   Подсказка: использовать менеджеры контекста.
import json

dict7 = {}
with open("file7.txt", "r", encoding="utf-8") as file7:
    for i in file7.read().split('\n'):
        firm = i.split()[0]
        try:
            pribil = int(i.split()[2]) - int(i.split()[3])
        except Exception as err:
            pribil = 0
            print(f"Ошибка: {err}, при подсчете прибыли для фирмы {i.split()[0]}")
        dict7.update({firm: pribil})
count = 0
sumribil = 0
for i in dict7.values():
    if i > 0:
        count += 1
        sumribil += i
    avergepribil = sumribil / count
listjson = [dict7, {"average_profit": avergepribil}]
with open("json_file7.json", "w") as json_file7:
    json.dump(listjson, json_file7)
