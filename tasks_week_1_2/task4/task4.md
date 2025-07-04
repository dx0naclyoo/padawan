# Система обращения к пользователям  
## (для рассылки бота паблика "Ножки-Альтушки")

Цель системы — формировать уважительное и дружелюбное обращение к подписчикам, используя их имя.  
Система умеет обрабатывать имена по определённым правилам.

---

## 🧾 Входные данные:
- Имя пользователя (например: *Маша*, *Никита*, *Семён* и т.д.)

## 📌 Правила преобразования:

### 1. **"Папич"-стиль**
- К имени добавляется суффикс `ыч` на конце.
- Примеры:
  - Никита → **Никитыч**
  - Саня → **Саныч**
  - Денис → **Денисыч**

> ✅ Это стандартный способ обращения ко всем в системе бота

---

### 2. **Если имя женское, то не преобразовывать его**
- Выводить: "ааа женщина"
- Их имена остаются без изменений

| Исходное имя | Результат        |
|--------------|------------------|
| Семён        | Семёныч          |
| Маша         | ааа женщина      |

---

## 🧪 Примеры работы системы:

| Имя       | Преобразованное имя |
|-----------|---------------------|
| Миша      | Мишыч               |
| Никита    | Никитыч             |
| Саня      | Саныч               |

---
