a = [
    "Сегодня мы работали с файлами Python.",
    "Научились сохранять текст.",
    "Узнали, как читать данные обратно."]
with open("diary.txt", "w", encoding="utf-8") as f:    # Создаём файл и записываем первые 3 строки
    for x in a:
        f.write(x + "\n")
with open("diary.txt", "a", encoding="utf-8") as f:   # Добавляем ещё одну запись в конец файла
    f.write("Следующее занятие – CSV и JSON\n")
with open("diary.txt", "r", encoding="utf-8") as f:   # Читаем все строки из файла в список
    s = f.readlines()
for x in s:                                              # Выводим каждую запись на экран
    print(x.strip())
print(f"\nКоличество записей в файле: {len(s)}")       # Считаем и выводим общее число строк