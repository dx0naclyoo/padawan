import random
print('Выберите чем будете ходить введите в консоль один из вариантов Камень, Ножницы, Бумага')
player_pick = str(input())
if player_pick not in('Камень','Ножницы','Бумага'):
    print('Ты блять Слово правильно написать не можешь?')
ai_pick = random.randint(1,3)

if ai_pick == 1:
    print('Компьютер выбрал Камень')
if ai_pick == 2:
    print('Компьютер выбрал Ножницы')
if ai_pick == 3:
    print('Компьютер выбрал Бумагу')

if player_pick == 'Камень' and ai_pick == 1:
    print('Ничья!')

if player_pick == 'Камень' and ai_pick == 2:
    print('Победа!')

if player_pick == 'Камень' and ai_pick == 3:
    print('ГГ мы проебали!')

if player_pick == 'Бумага' and ai_pick == 1:
    print('Победа!')

if player_pick == 'Бумага' and ai_pick == 2:
    print('ГГ мы проебали!')
if player_pick == 'Бумага' and ai_pick == 3:
    print('Ничья!')

if player_pick == 'Ножницы' and ai_pick == 1:
    print('ГГ мы проебали!')
if player_pick == 'Ножницы' and ai_pick == 2:
    print('Ничья!')

if player_pick == 'Ножницы' and ai_pick == 3:
    print('Победа!')