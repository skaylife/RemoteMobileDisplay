import json

# Название файла
filename = "data.json"

# Функция для чтения файла
def get_items():
    try:
        with open(filename, 'r') as f:
            items = json.load(f)
    except FileNotFoundError:
        items = []
    return items

# Функция для записи файлов
def write_items(items):
    try:
        # Сохраняем список в файле JSON
        with open(filename, 'w') as f:
            f.write(json.dumps(items))
    except FileNotFoundError:
        items = []
    return items

# Тоже сохраняет файл
def save_items(items):
    with open('data.json', 'w') as f:
        json.dump(items, f)