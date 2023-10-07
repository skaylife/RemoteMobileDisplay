from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def set_system_volume(new_volume):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Убедимся, что новая громкость находится в диапазоне [0.0, 1.0]
    new_volume = max(0.0, min(1.0, new_volume))

    volume.SetMasterVolumeLevelScalar(new_volume, None)

        # Запись времни в словарь
    data = {}
    data["system_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["time_work_pc"] = str(up_time).split(".")[0]

if __name__ == "__main__":
    # Устанавливаем громкость на 100% (1.0)
    set_system_volume(new_volume=0.05)
    print("Change system volume")