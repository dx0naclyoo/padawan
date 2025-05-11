expenses = {}  # Словарь для хранения трат {категория: сумма}

while True:
    # Запрашиваем категорию
    category = input("Введи категорию (или 'стоп'/'Enter' для завершения): ").strip().lower()
    
    # Проверяем, хочет ли пользователь выйти
    if category == 'стоп' or category == '':
        break
    
    # Запрашиваем сумму
    try:
        input_amount: str = input("Введи сумму: ").strip()
        int_amount: int = int(input_amount)  # Преобразуем в число
        
        # Добавляем или обновляем трату в словаре
        if category in expenses:
            expenses[category] += int_amount
        else:
            expenses[category] = int_amount
            
    except ValueError:
        print("Ошибка! Сумма должна быть числом, например, '500'. Попробуй ещё раз.")
        continue

# Проверяем, есть ли траты
if not expenses:
    print("Траты не введены, братан!")
else:
    # Находим категорию с максимальной тратой
    max_category = None
    max_amount = 0
    for category, int_amount in expenses.items():
        if int_amount > max_amount:
            max_amount = int_amount
            max_category = category
    
    print(f"Больше всего потрачено на {max_category}: {max_amount} руб")

