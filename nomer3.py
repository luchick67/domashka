import json
p = {               # Создаём словарь с исходным профилем
    "Имя": "Алексей",
    "Группа": "КБ-101",
    "Навыки": ["Python", "Excel"],
    "Уведомления": True}
with open("participant.json", "w", encoding="utf-8") as f:     # Сохраняем профиль в JSON-файл
    json.dump(p, f, ensure_ascii=False, indent=4)
with open("participant.json", "r", encoding="utf-8") as f:     # Читаем профиль из файла
    d = json.load(f)
d["Навыки"].append("CSV")      # Добавляем новый навык в список
d["Уведомления"] = False         # Отключаем уведомления
with open("participant.json", "w", encoding="utf-8") as f:   # Перезаписываем файл обновлёнными данными
    json.dump(d, f, ensure_ascii=False, indent=4)
with open("participant.json", "r", encoding="utf-8") as f:     # Повторно читаем файл и выводим в консоль
    r = json.load(f)
for k, v in r.items():         # Красиво печатаем каждое поле профиля
    print(f"{k}: {v}")