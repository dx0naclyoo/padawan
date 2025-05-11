import json

tasks = []
try:
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
except FileNotFoundError:
    pass

while True:
    print('--------------')
    print("\n1. Добавить задачу\n2. Отметить выполненной\n3. Показать задачи\n4. Выход")
    print('--------------')
    choice = input("Выберите действие: ")
    
    if choice == '1':
        text = input("Введите задачу: ").strip()
        tasks.append({"text": text, "completed": False})

    elif choice == '2':
        index = int(input("Номер задачи: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
        
    elif choice == '3':
        print('Задачи для просмотра: ')
        if not tasks:
            print('Нет запланированных задач')
            continue
        
        for i, task in enumerate(tasks, 1):
            status = "выполнена" if task["completed"] else "не выполнена"
            print(f"{i}. {task['text']} ({status})")
        print('--------------')
        
    elif choice == '4':
        break

with open('tasks.json', 'w') as file:
    json.dump(tasks, file, indent=4)