from flask import Flask, render_template, url_for, redirect, request, jsonify
import json

filename = 'data.json'


def delete_item(index):
    
    try:
        with open(filename, 'r') as f:
            items = json.load(f)
    except FileNotFoundError:
        pass
    # Удаляем соответствующий элемент из списка
    del items[index]

    # Сохраняем список в файле JSON
    with open(filename, 'w') as f:
        f.write(json.dumps(items))
    
    # Обновляет страницу с перебросом на основную 
    return redirect('/')
    # Возвращаем JSON-ответ с удаленным элементом
    return jsonify({'success': True})
