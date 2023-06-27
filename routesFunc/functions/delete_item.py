from flask import Flask, render_template, url_for, request, jsonify
import json

filename = 'data.json'

try:
    with open(filename, 'r') as f:
        items = json.load(f)
except FileNotFoundError:
    pass

def delete_item(index):
    # Удаляем соответствующий элемент из списка
    del items[index]

    # Сохраняем список в файле JSON
    with open(filename, 'w') as f:
        f.write(json.dumps(items))

    # Возвращаем JSON-ответ с удаленным элементом
    return jsonify({'success': True})