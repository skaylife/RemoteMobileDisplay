from flask import Flask, render_template, url_for, request, jsonify
import json

def edit_item(index):
    # Получаем данные из формы и изменяем соответствующий элемент списка
    name = request.form['name']
    url = request.form['url']
    items[index]['name'] = name
    items[index]['url'] = url

    # Сохраняем список в файле JSON
    with open(filename, 'w') as f:
        f.write(json.dumps(items))

    # Возвращаем JSON-ответ с измененным элементом
    return jsonify(items[index])