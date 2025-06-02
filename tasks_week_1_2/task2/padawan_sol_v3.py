per = {}

def cat_add(key: str, value: int):
    """Добавляет ключ и значение введенные пользователем в словарь per"""

    if key not in per:
        per[key] = value
    else:
        per[key] += value


def find_max(per):
    """Ищет на что было больше всего потрачено в словаре per"""

    max_per = max(per.values())
    for key, value in per.items():
        if value == max_per:
            print(f'{key} - {value}')


while True:
    command = input("Выберите действие:\n 1:Завершить работу\n 2:Выбрать список для трат\n 3:Посмотреть куда проебал больше всего\n 4:Добавить категорию трат или добавить траты в имеющуюся категорию\n")

    if command == '1':  # Завершаем работу программы
        break
    
    if command == '2':  # Выводим все названия категорий и сумму трат
        for key, value in per.items():
            print(key, value)

    if command == '3':  # Вывод категорий с максимальной тратой
        if per:
            find_max(per)
        else:
            print('Ваш список трат пока пустой')
            continue

    if command == '4':  # Добавление новой категории или же увеличение трат уже имеющейся категории
        key = str(input('Введите название категории'))
        value = int(input('Введите сумму трат'))
        cat_add(key, value)