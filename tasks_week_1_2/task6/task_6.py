import time

def sum_a_and_b(a: int, b: int):
    time.sleep(5)
    return a + b

# Функция - sum_a_and_b
# Что требуется знать:
# Что такое декоратор и замыкание.

# Написать декоратор - который будет хэшировать аргументы функции sum_a_and_b и вывод
# sum_a_and_b(5, 5) -> 10 | time - 5 sec
# sum_a_and_b(5, 5) -> 10 | time - взять значения из хэша
# ОБЯЗАТЕЛЬНО ! a, b могут меняться местами, a + b, b + a
# Уловие: Использовать dict, для хранения хэша

a = {'key': 'value', 'key2': 'value2'}
print(a['key'])

if __name__ == '__main__':
    sum_a_and_b(5, 5) # 5 sec
    sum_a_and_b(5, 6) # 5 sec
    sum_a_and_b(6, 5) # moment
    sum_a_and_b(5, 5) # moment