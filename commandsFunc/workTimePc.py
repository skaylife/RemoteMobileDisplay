import psutil
import datetime

def workTimePc():
    # Получение времени 
    boot_time = psutil.boot_time()
    up_time = datetime.datetime.now() - datetime.datetime.fromtimestamp(boot_time)

    # Запись времни в словарь
    data = {}
    data["system_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["time_work_pc"] = str(up_time).split(".")[0]

    # print("Системное время:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # print("Время работы компьютера:", str(up_time).split(".")[0])

    return data
