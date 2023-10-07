import json
from flask import jsonify, render_template, redirect, request
from config import configStart
from commands import *

from .crud_json import *


def settings():
    items = get_items()

    if request.method == 'POST':
        # Получаем данные из формы и добавляем новый элемент в список
        name = request.form['name']
        url = request.form['url']
        
        # Проверка наличие совпадения по url
        if not url.startswith("https://") and not url.startswith("http://"):
            url = "https://" + url
        
        # Перебор циклом сопадений с url который ввел пользователь
        for item in items:
            if item['url'] == url:
                return f"Найдено совпадение название: '{url}' для элемента '{item['name']}'"
            if item['name'] == name:
                    return f"Найдено совпадение название: '{name}' url: '{item['url']}'"

        # # Перебор циклом сопадений с name который ввел пользователь
        # for item in items:
        #     if item['name'] == name:
        #         return f"Найдено совпадение название: '{name}' url: '{item['url']}'"
        lambda id_elem: id_elem +1
        items.append({'id': id_elem(),'name': name, 'url': url})
        
        # Сохраняем список в файле JSON
        save_items(items)

        # Перезагружаем страницу
        return redirect("/settings")
        # Возвращаем JSON-ответ с добавленным элементом
        return jsonify(items[-1])
    else:
        # return "Ошибка отправки формы"
        # Отображаем страницу с формой добавления элемента и списком всех элементов
        return render_template('settings.html', items=items)