import os 
import subprocess
from flask import render_template
import socket
import requests

def ip_localhost():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()

    return ip_address

# ===================================================

# Отправляем GET-запрос к сайту, который покажет нам наш IP-адрес
def ip_global():

    response = requests.get('https://ifconfig.co/ip')
    return response.text.strip()


# ===================================================

def ip_all():
    data = {}
    data["ip_local"] = ip_localhost()
    data["ip_global"] = ip_global()
    return data

# ===================================================

def open_youtube():
    os.system("start http://youtube.com")
    return render_template("main.html")

# ===================================================

def link_tab(href = "google.com", page= "main.html"):
    url = f'https://{href}'
    os.system(f'start {url}')
    # return render_template(page)

def ipconfig(parameters=80):
    try:
        data = subprocess.check_output(['ipconfig','/all']).decode('utf-8').split('\n')
    except:
        data = subprocess.check_output(['ipconfig','/all']).decode('cp866').split('\n')
    # parameter = data[parameters].split(': ')
    # return parameter[1]
    return data

# def resultCommand

