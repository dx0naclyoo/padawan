beer = {'Пиво': 0}
whores = {'Шлюхи': 0}
drugs = {'Таблетки': 0}
while True:
    command = input("Выберите действие:\n 1:Завершить работу\n 2:Выбрать список для трат\n 3:Посмотреть куда проебал больше всего")
    if command == '1':
        break
    if command == '2':
        b = input('Выберите какие траты вы хотите посмотреть:\n 1:Пиво\n 2:Шлюхи\n 3:Таблетосы')
        if b == '1':
            print(beer['Пиво'])
            c = input('1:Вернуться назад\n 2:Добавить траты')
            if c == '1':
                continue
            if c == '2':
                beer['Пиво'] += int(input('Введите сумму'))
        if b == '2':
            print(whores['Шлюхи'])
            c = input('1:Вернуться назад\n 2:Добавить траты')
            if c == '1':
                continue
            if c == '2':
                whores['Шлюхи'] += int(input('Введите сумму'))
        if b == '3':
            print(drugs['Таблетки'])
            c = input('1:Вернуться назад\n 2:Добавить траты')
            if c == '1':
                continue
            if c == '2':
                drugs['Таблетки'] += int(input('Введите сумму'))
    if command == '3':
        if beer['Пиво'] > whores['Шлюхи'] and beer['Пиво'] > drugs['Таблетки']:
            print(beer)
        if whores['Шлюхи'] > beer['Пиво'] and whores['Шлюхи'] > drugs['Таблетки']:
            print(whores)
        if drugs['Таблетки'] > beer['Пиво'] and drugs['Таблетки'] > whores['Шлюхи']:
            print(drugs)
        else:
            if beer['Пиво'] == whores['Шлюхи'] and beer['Пиво'] > drugs['Таблетки']:
                print(beer, whores)
            if beer['Пиво'] > whores['Шлюхи'] and beer['Пиво'] == drugs['Таблетки']:
                print(beer, drugs)
            if whores['Шлюхи'] > beer['Пиво'] and whores['Шлюхи'] == drugs['Таблетки']:
                print(whores, drugs)
            if whores['Шлюхи'] == beer['Пиво'] and whores['Шлюхи'] == drugs['Таблетки']:
                print(whores, drugs, beer)