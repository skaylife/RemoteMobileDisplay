from flask import Flask, render_template, url_for, request, jsonify
from commands import *
import json
from commandsFunc.workTimePc import workTimePc

from routesFunc.allFunctions import *

app = Flask(__name__)
# app.run(debug=True, host='192.168.1.61')

# Указываем имя файла для хранения данных
filename = 'data.json'

# Создаем пустой список для хранения элементов
items = []

try:
    with open(filename, 'r') as f:
        items = json.load(f)
except FileNotFoundError:
    pass

@app.route('/', methods=['GET', 'POST'])
def index():
    return start()


@app.route('/edit/<int:index>', methods=['POST'])
def edit_elem(index):
    return edit_item(index)


@app.route('/delete/<int:index>', methods=['POST'])
def delete_elem(index):
    return delete_item(index)


@app.route('/move_up/<int:index>', methods=['POST'])
def move_up(index):
    # Перемещаем элемент вверх по списку
    if index > 0:
        items[index], items[index - 1] = items[index - 1], items[index]

        # Сохраняем список в файле JSON
        with open(filename, 'w') as f:
            f.write(json.dumps(items))

    # Возвращаем JSON-ответ с обновленным списком
    return jsonify(items)


@app.route('/move_down/<int:index>', methods=['POST'])
def move_down(index):
    # Перемещаем элемент вниз по списку
    if index < len(items) - 1:
        items[index], items[index + 1] = items[index + 1], items[index]

        # Сохраняем список в файле JSON
        with open(filename, 'w') as f:
            f.write(json.dumps(items))

    # Возвращаем JSON-ответ с обновленным списком
    return jsonify(items)




    # Обработчик запроса на выполнение функции по ключу
@app.route('/execute/<url>')
def execute_func(url):
    # Извлекаем нужную функцию из словаря funcs
    
    func = link_tab(url)
    if func:
        # Выполняем функцию и возвращаем результат
        return func()
    else:
        # Если ключ не найден, возвращаем 404 ошибку
        return render_template("default.html"), 404

@app.route('/main')
def main():
    return render_template("main.html")

@app.route('/process_data/<index>/', methods=['POST'])
def yt(index):
    if index == '1':
        return link_tab("youtube.com")
    elif index == '2':
        data = {}
        data["ip_all"] = ip_all()
        data["workTimePc"] = workTimePc()
        return render_template("main.html", items=data)
        # return render_template("main.html")
    else:
        return 'Не работает условие кнопки'
    return 'Ничего не отработало'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
        # Загружаем список элементов из файла JSON


# if __name__ == "__main__":
#     app.config['SERVER_NAME'] = "localhost:5000"
#     app.run()