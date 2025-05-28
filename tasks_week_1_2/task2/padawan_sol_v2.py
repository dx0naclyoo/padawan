per = []
start = 0
while True:
    command = input("Выберите действие:\n 1:Завершить работу\n 2:Выбрать список для трат\n 3:Посмотреть куда проебал больше всего\n 4:Добавить категорию трат")
    print(per)
    if command == '1':
        break
    if command == '2':
        c = input('Если хотите посмотреть траты введите 1 если хотите внести траты введите 2:')
        if c == '1':
            for i in range(0, len(per), 2):
                print(per[i], per[i+1])
        if c == '2':
            for i in range(0, len(per), 2):
                print(per[i])
            d = str(input('Введите в какую категорию вы хотите добавить траты'))
            if d in per:
                indx = per.index(d)
                d = int(input('Введите сумму траты'))
                per[indx+1] += d
            else:
                continue
    if command == '4':
        x = str(input('Введите название категории трат:'))
        per.append(x)
        per.append(0)
    if command == '3':
        m = 0
        for i in per:
            if type(i) in (int, float) and i > m:
                # type(i) in (int, float) - можно использовать встроенный метод isinstance(i, (int, float))
                m = i
        for i in per:
            if i == m:
                indx = per.index(i, start)
                print(per[indx], per[indx-1])
                start = indx+1
            else:
                continue