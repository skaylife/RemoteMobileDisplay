from flask import Flask, render_template, url_for, redirect, request, jsonify
import json
from .crud_json import *


def edit_item(index):
    items = get_items()
    # Получаем данные из формы и изменяем соответствующий элемент списка
    name = request.form['name']
    url = request.form['url']
    items[index]['name'] = name
    items[index]['url'] = url

    # Сохраняем список в файле JSON
    write_items(items)

   # Обновляет страницу с перебросом на основную 
    return redirect('/')
    # Возвращаем JSON-ответ с измененным элементом
    return jsonify(items[index])
