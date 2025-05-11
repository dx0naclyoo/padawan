import httpx

# URL API Центрального банка РФ
url = "https://www.cbr-xml-daily.ru/daily_json.js"

try:
    # Делаем GET-запрос к API
    response = httpx.get(url)
    
    # Проверяем статус ответа
    if response.status_code != 200:
        print(f"Ошибка: Сервер вернул статус {response.status_code}")
        print(f"Содержимое ответа: {response.text}")
        exit(1)
    
    # Пробуем разобрать JSON
    data = response.json()
    
    # Извлекаем курсы доллара и евро
    usd_rate = data['Valute']['USD']['Value']
    eur_rate = data['Valute']['EUR']['Value']
    
    # Выводим результат в консоль
    print(f"USD: {usd_rate:.2f} rub, EUR: {eur_rate:.2f} rub")

except httpx.RequestError as e:
    print(f"Ошибка сети: {e}")
except ValueError as e:
    print(f"Ошибка парсинга JSON: {e}")
    print(f"Содержимое ответа: {response.text}")
except KeyError as e:
    print(f"Ошибка в структуре данных: {e}")