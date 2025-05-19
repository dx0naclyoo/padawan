from typing import Final, Set

# --- Константы для определения пола ---

# Имена унисекс (имеют приоритет над другими правилами)
UNISEX_NAMES_LOWER: Final[Set[str]] = set(
    name.lower()
    for name in [
        "Саша", "Женя", "Валя", "Паша", "Шура", "Сима", "Лера",
        "Камиль",  # Может быть и мужским, и женским
        "Никита",  # Исторически мужское, но используется и для сокращения женских
        "Миша"  # Сокращение от Михаил, но иногда от Мишель
    ]
)

# Мужские имена, которые по окончанию (-а, -я) похожи на женские
MALE_NAMES_WITH_FEMALE_LIKE_ENDINGS_LOWER: Final[Set[str]] = set(
    name.lower()
    for name in [
        "Илья", "Никита", "Лука", "Фома", "Кузьма", "Алёша", "Данила",
        "Гаврила", "Антипа", "Ермола", "Сила", "Добрыня", "Юноша",
        "Старшина", "Воевода"
    ]
)

# Женские имена, которые по окончанию (согласная, -ь) похожи на мужские
FEMALE_NAMES_WITH_MALE_LIKE_ENDINGS_LOWER: Final[Set[str]] = set(
    name.lower()
    for name in [
        "Любовь", "Эсфирь", "Рахиль", "Юдифь", "Агарь", "Нинель", "Руфь",
        "Суламифь", "Мишель", "Николь", "Кармен", "Беатрис", "Гюльчатай",
        "Айгуль", "Асель", "Сольвейг", "Этель", "Инес", "Долорес", "Консуэло",
        "Перистель", "Адель", "Эльвир"
    ]
)

# Константы для возвращаемых значений пола
GENDER_MALE: Final[str] = "мужской"
GENDER_FEMALE: Final[str] = "женский"
GENDER_UNISEX: Final[str] = "унисекс"
GENDER_UNKNOWN: Final[str] = "неизвестно"

# Вспомогательные данные: русские гласные в нижнем регистре
RUSSIAN_VOWELS_LOWER: Final[Set[str]] = set("аеёиоуыэюя")


def determine_gender_by_russian_name(name: str) -> str:
    """
    Определяет вероятный пол русского имени на основе общих окончаний
    и списков исключений.

    Эта функция использует подход, основанный на правилах, и не является безошибочной.
    Точность сильно зависит от полноты списков исключений.
    Предназначена в первую очередь для распространенных русских имен.

    Предупреждение: Определение пола по имени — сложная задача с множеством
    нюансов (культурных, лингвистических). Данный метод предоставляет
    лишь приблизительную оценку для русскоязычных имен.

    Args:
        name: Строка с именем для анализа.

    Returns:
        Строка, указывающая определенный пол: "мужской", "женский",
        "унисекс" или "неизвестно".
    """
    if not isinstance(name, str):
        return GENDER_UNKNOWN

    name_stripped: str = name.strip()
    if not name_stripped:
        return GENDER_UNKNOWN

    name_lower: str = name_stripped.lower()

    # Проверки исключений (по убыванию приоритета)
    if name_lower in UNISEX_NAMES_LOWER:
        return GENDER_UNISEX
    if name_lower in FEMALE_NAMES_WITH_MALE_LIKE_ENDINGS_LOWER:
        return GENDER_FEMALE
    if name_lower in MALE_NAMES_WITH_FEMALE_LIKE_ENDINGS_LOWER:
        return GENDER_MALE

    last_char: str = name_lower[-1]

    # Общие эвристические правила
    if last_char in ("а", "я"):
        return GENDER_FEMALE
    if last_char == "й":
        return GENDER_MALE
    if last_char not in RUSSIAN_VOWELS_LOWER and last_char != "ь":
        return GENDER_MALE
    if last_char == "ь":
        return GENDER_MALE

    return GENDER_UNKNOWN


# --- Примеры использования ---
if __name__ == "__main__":
    test_names: list[str] = [
        "Мария", "Александр", "Саша", "Илья", "Никита", "Любовь", "Игорь",
        "Андрей", "Женя", "Ольга", "Эсфирь", "Гюльчатай", "  Иван  ",
        "", "Кирилл", "Светлана", "Лев", "Емельян", "Адель", "Камиль", "Миша", "Валя"
    ]

    for t_name in test_names:
        gender: str = determine_gender_by_russian_name(t_name)
        print(f"Имя: '{t_name}' -> Пол: {gender}")

    # Примеры вне явных списков
    print(f"Имя: 'Руслан' -> Пол: {determine_gender_by_russian_name('Руслан')}")  # мужской
    print(f"Имя: 'Алина' -> Пол: {determine_gender_by_russian_name('Алина')}")    # женский
    print(f"Имя: 'Василий' -> Пол: {determine_gender_by_russian_name('Василий')}")  # мужской
    print(f"Имя: 'Беатрис' -> Пол: {determine_gender_by_russian_name('Беатрис')}")  # женский (из списка исключений)