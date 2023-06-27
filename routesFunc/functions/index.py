import json
from flask import jsonify, render_template, request
from config import configStart
from commands import *

def get_items():
    try:
        with open('data.json', 'r') as f:
            items = json.load(f)
    except FileNotFoundError:
        items = []
    return items

def save_items(items):
    with open('data.json', 'w') as f:
        json.dump(items, f)

def start():
    items = get_items()
    data = {}
    data["ip_all"] = ip_all()
    data["port"] = configStart["port"]
    if request.method == 'POST':
        # Получаем данные из формы и добавляем новый элемент в список
        name = request.form['name']
        url = request.form['url']
        items.append({'name': name, 'url': url})
        
        # Сохраняем список в файле JSON
        save_items(items)

        # Возвращаем JSON-ответ с добавленным элементом
        return jsonify(items[-1])
    
    else:
        # Отображаем страницу с формой добавления элемента и списком всех элементов
        return render_template('default.html', items=items, data=data)