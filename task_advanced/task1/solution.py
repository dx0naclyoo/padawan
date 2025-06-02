

total_words: int = 0
uniq_words: set = set()
words_top: dict = dict()


def analyze_text(line: str):
    """Функция анализирует слова в файле и записывает статистику в глобальные переменные
    Используются глобавльные переменные, для хранения результатов.
    total_words: int = 0
    uniq_words: set = set()
    words_top: dict = dict()
    
    Args:
        line (str): # Example - 'Эпопея Разума и Машины: Великая История Компьютеров и Компьютерных Наук'
    """
    list_of_words = line.split()
    
    # Кол-во слов
    global total_words
    total_words += len(list_of_words)
    uniq_words.update(list_of_words)

    # top 10
    for item in list_of_words:
        if item in words_top:
            words_top[item] += 1  
        else: 
            words_top[item] = 1


def read_file_batch(file_name: str, last_position: int = 0) -> dict:
    """_summary_

    Args:
        file_name (str): Название файла
        last_position (int, optional): Место на котором остановились читать файл. Defaults to 0.

    Returns:
        dict: Результат чтения. 
        Example: {'line': 'Эпопея Разума и Машины: Великая История Компьютеров и Компьютерных Наук', 'new_postition': 122, 'eof': False}
    """
    end_of_file: bool = False
    
    with open(file_name, 'r') as file:
        file.seek(last_position)
        line = file.readline()
        new_position = file.tell()
        if not line:
            end_of_file = True
        return {'line': line, 'new_postition': new_position, 'eof': end_of_file}


def main(file_path: str) -> None:
    # Запуск всей программы
    current_pos = 0 # Текущая позиция чтения файла
    eof = False # Указатель, что файл ещё не закончился
    
    while not eof:
        # Читаем файл батчами. Сохраняем line и позицию на которой остановились
        read_dict: dict = read_file_batch(file_path, last_position=current_pos)
        current_pos  = read_dict['new_postition']
        eof = read_dict['eof']
        analyze_text(line=read_dict['line'])
    
    
    # Вывод результата
    print(f'Всего слов - {total_words}')
    print(f'Кол-во уникальных слов - {len(uniq_words)}')
    top_10 = sorted(words_top.items(), key=lambda x: x[1], reverse=True)[:10]
    for word, count in top_10:
        print(f'Слово - {word}, Кол-во - {count}')

file_path = "computer_science.txt"
main(file_path)