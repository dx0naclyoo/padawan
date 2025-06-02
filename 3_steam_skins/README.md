# Steam Skins

Привет! Пришёл заказ создать крутой сайт по поиску скинов в Steam.
Но злые ребята из Валв мешают фронту работать и блокируют его запросы напрямую, нужно создать "proxy", который поможет фронтендеру закончить

Фронтендер уже сделал свою работу, создал рабочее приложение и ожидает, что бэкенд будет отдавать ему конкретные данные.
**Фронтенд:** https://flourishing-alpaca-c7e241.netlify.app/

Что нужно знать:
- Как приложения общаются между собой, http/https
- Как вообще создаются backend приложения | Python FastAPI
- Выставление правильных CORS на Backend'e
  
---

## Контракт между бекендом фронтендом

На бекенде есть ручка `/search/`, на которую фронтенд отправляет свой запрос поиска.
* **Метод:** `GET`
* **URL:** `your_domain/search/`
* **Пример запроса:** `your_domain/search/?query=case`

**Ожидает получить JSON в следующем формате:**

```json
{
  "content": { // Всё, что внутри content, возвращает Steam
    "success": true,
    "start": 0,
    "pagesize": 20,
    "total_count": 4429,
    "searchdata": {
      "query": "knife",
      "search_descriptions": false,
      "total_count": 4429,
      "pagesize": 20,
      "prefix": "searchResults",
      "class_prefix": "market"
    },
    "results": [
      {
        "name": "Knife | Jack Knife",
        "hash_name": "Knife | Jack Knife",
        "sell_listings": 11,
        "sell_price": 1696,
        "sell_price_text": "$16.96",
        "app_icon": "[https://cdn.fastly.steamstatic.com/steamcommunity/public/images/apps/489940/56876299e611314a6e0857e3996ba1c204b24249.jpg](https://cdn.fastly.steamstatic.com/steamcommunity/public/images/apps/489940/56876299e611314a6e0857e3996ba1c204b24249.jpg) ",
        "app_name": "BATTALION: Legacy",
        "asset_description": {
          "appid": 489940,
          "classid": "3607522451",
          "instanceid": "0",
          "background_color": "",
          "icon_url": "jg7Hw3nq8oHhNZxCx6gr5bZ-qp-hM9Y58aHmwRd1PCHsTUeZzEMILKGqGeXa42JL5-hggtXmFRNgkDj8IQ7zOy3i3SHUyavM-poZlZ2c72vzAKWsfQG_rgB1K6WyYM6Fpu6HK__-tPsu0TdRatE3tJAp4QVMMlXRr4LJijw3ET50pwr8B-BW7PAGIzP8IrlJ7A",
          "tradable": 1,
          "name": "Knife | Jack Knife",
          "name_color": "ff7200",
          "type": "",
          "market_name": "Knife | Jack Knife",
          "market_hash_name": "Knife | Jack Knife",
          "commodity": 1
        },
        "sale_price_text": "$16.23"
      }
    ]
  }
}
```

---

## Рабочие ссылки

Как это выглядит в браузере:
* **Фронтенд:** https://flourishing-alpaca-c7e241.netlify.app/
* **Бэкенд для примера:** https://padawan-skins.onrender.com/search/?query=case

---

## Парсинг предметов

Получать эту информацию можно с помощью **API Steam**, а именно `/search/`.
**Ссылка на API Steam для парсинга:** https://steamcommunity.com/market/search/render/?query=case&norender=1

**Пример ответа API Steam:**

```json
{
    "success": true,
    "start": 0,
    "pagesize": 10,
    "total_count": 4,
    "searchdata": {
        "query": "Gamma Case",
        "search_descriptions": false,
        "total_count": 4,
        "pagesize": 10,
        "prefix": "searchResults",
        "class_prefix": "market"
    },
    "results": [
        {
            "name": "Gamma Case",
            "hash_name": "Gamma Case",
            "sell_listings": 7898,
            "sell_price": 47150,
            "sell_price_text": "471,50 руб.",
            "app_icon": "[https://cdn.fastly.steamstatic.com/steamcommunity/public/images/apps/730/8dbc71957312bbd3baea65848b545be9eae2a355.jpg](https://cdn.fastly.steamstatic.com/steamcommunity/public/images/apps/730/8dbc71957312bbd3baea65848b545be9eae2a355.jpg)",
            "app_name": "Counter-Strike 2",
            "asset_description": {
                "appid": 730,
                "classid": "1797256701",
                "instanceid": "0",
                "background_color": "",
                "icon_url": "-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXU5A1PIYQNqhpOSV-fRPasw8rsUFJ5KBFZv668FFYznarJJjkQ6ovjw4SPlfP3auqEl2oBuJB1j--WoY322QziqkdpZGr3IteLMlhpw4RJCv8",
                "tradable": 1,
                "name": "Gamma Case",
                "name_color": "D2D2D2",
                "type": "Base Grade Container",
                "market_name": "Gamma Case",
                "market_hash_name": "Gamma Case",
                "commodity": 1
            },
            "sale_price_text": "451 руб."
        },
        ...
    ]
}
```
---

## 🚀 Деплой

Ожидается, что бэкенд будет публичным (доступным во всей сети). Для этого можно воспользоваться сервисом **render.com**, который позволяет бесплатно деплоить наши проекты.

После деплоя нужно будет подставить свою ссылку в форму **API Backend URL** на фронтенде и проверить результат.
