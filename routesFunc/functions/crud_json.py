import json

# Название файла
filename = "data.json"

# Функция для записи файлов
def get_items():
    try:
        with open(filename, 'r') as f:
            items = json.load(f)
    except FileNotFoundError:
        items = []
    return items

# Функция для чтения файла
def write_items(items):
    try:
        # Сохраняем список в файле JSON
        with open(filename, 'w') as f:
            f.write(json.dumps(items))
    except FileNotFoundError:
        items = []
    return items