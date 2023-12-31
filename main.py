from flask import Flask, render_template, redirect, url_for, request, jsonify
from commands import *
import json
import psutil
import plotly.graph_objs as go

from config import configStart
from commandsFunc.workTimePc import workTimePc
from commandsFunc.sysEditSound import set_system_volume
from commandsFunc.monitor import OnPc, OffPc

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


    # Обработчик запроса на выполнение функции по ключу
@app.route('/execute/<path:url>')
def execute_func(url):
    # Извлекаем нужную функцию из словаря funcs
    

    if url:
        # Выполняем функцию и возвращаем результат
        func = link_tab(url)
        # func()
        return redirect('/')
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

@app.route('/diagrams')
def diagrams():
    cpu_percent = psutil.cpu_percent()
    cpu_count = psutil.cpu_count(logical=True)
    mem = psutil.virtual_memory()
    mem_percent = mem.percent
    disk_usage = psutil.disk_usage('/')
    disk_free = disk_usage.free / 1024 / 1024 / 1024
    disk_total = disk_usage.total / 1024 / 1024 / 1024

    return render_template("diagrams.html",
                           cpu_percent=cpu_percent,
                           cpu_count=cpu_count,
                           mem_percent=mem_percent,
                           mem_total=round(mem.total / 1024 / 1024, 2),
                           mem_used=round(mem.used / 1024 / 1024, 2),
                           disk_count=len(psutil.disk_partitions()),
                           disk_free=round(disk_free, 2),
                           disk_total=round(disk_total, 2))

@app.route("/system_info")
def system_info():
    cpu_percent = psutil.cpu_percent()
    cpu_count = psutil.cpu_count(logical=True)
    mem = psutil.virtual_memory()
    mem_percent = mem.percent
    disk_usage = psutil.disk_usage('/')
    disk_free = disk_usage.free / 1024 / 1024 / 1024
    disk_total = disk_usage.total / 1024 / 1024 / 1024

    return jsonify(cpu_percent=cpu_percent,
                   cpu_count=cpu_count,
                   mem_percent=mem_percent,
                   mem_total=mem.total / 1024 / 1024,
                   mem_used=round(mem.used / 1024 / 1024, 2),
                   disk_count=len(psutil.disk_partitions()),
                   disk_free=disk_free,
                   disk_total=disk_total)

@app.route('/settings', methods=['GET', 'POST'])
def settings_elem():
    return settings()

@app.route('/move/<string:position>/<int:index>', methods=['POST'])

def show_page(position, index):
    if position == 'up':
        # Перемещаем элемент вверх по списку
        if index > 0:
            items[index], items[index - 1] = items[index - 1], items[index]

            # Сохраняем список в файле JSON
            with open(filename, 'w') as f:
                f.write(json.dumps(items))

        return redirect('/settings')
        # Возвращаем JSON-ответ с обновленным списком
        return jsonify(items)
    elif position == 'down':
        # Перемещаем элемент вниз по списку
        if index < len(items) - 1:
            items[index], items[index + 1] = items[index + 1], items[index]

            # Сохраняем список в файле JSON
            with open(filename, 'w') as f:
                f.write(json.dumps(items))

        return redirect('/settings')
        # Возвращаем JSON-ответ с обновленным списком
        return jsonify(items)
    else:
        return 'Не работает смена позиции ссылок'

@app.route('/sys_sounds', methods=['POST'])
def sys_sounds():
    try:
        positionHtml = request.form['sounds_position']
        sys_sounds_position = int(positionHtml) / 100
        # print(sys_sounds_position)
        set_system_volume(new_volume=sys_sounds_position)
        # set_system_volume(new_volume=0.01)
        # set_system_volume(sys_sounds_position)
        # result = str(float(position) * 2)
        # result = positionHtml
        redirect("/")
        return positionHtml
    except Exception as e:
        return str(e), 400

@app.route('/monitor/<path:status>', methods=['POST'])
def monitor(status):
    try:
        if status == "off":
            OffPc()
            return redirect('/')
        else:
            OnPc()
            return redirect('/')
    except Exception as e:
        return str(e), 400
    
# @app.route('/update', methods=['POST'])
# def update():
#     try:
#         user_input = request.form['user_input']  # Получаем значение из ползунка

#         # Выполните здесь необходимую обработку с user_input
#         # Например, преобразуем значение в число и умножим на 2:
#         result = str(float(user_input) * 2)

#         return result
#     except Exception as e:
#         return str(e), 400  # Отправляем ошибку 400 Bad Request



if __name__ == '__main__':
    app.run(configStart["host"], configStart["port"])
        # Загружаем список элементов из файла JSON


# if __name__ == "__main__":
#     app.config['SERVER_NAME'] = "localhost:5000"
#     app.run()