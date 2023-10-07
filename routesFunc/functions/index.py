import json
from flask import jsonify, render_template, redirect, request
import re
from config import configStart
from commands import *

from .crud_json import *


def start():
    items = get_items()
    data = {}
    data["ip_all"] = ip_all()
    data["port"] = configStart["port"]
    if request.method == 'POST':
        # Получаем данные из формы и добавляем новый элемент в список
        name = request.form['name']
        url = request.form['url']
        # Проверка на наличие https:// и http://
        # if not url.startswith("https://") and not url.startswith("http://"):
        #     url = "https://" + url

        url = re.sub(r'https://', '', url)
        # Удаляем "http://"
        url = re.sub(r'http://', '', url)

        items.append({'name': name, 'url': url})
        
        # Сохраняем список в файле JSON
        save_items(items)

        # Перезагружаем страницу
        return redirect("/")
        # Возвращаем JSON-ответ с добавленным элементом
        return jsonify(items[-1])
    else:
        # return "Ошибка отправки формы"
        # Отображаем страницу с формой добавления элемента и списком всех элементов
        return render_template('default.html', items=items, data=data)