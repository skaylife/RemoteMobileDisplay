import ctypes
# Этот код выключает монитор
def OffPc ():
    print("OFFpc")
    ctypes.windll.user32.SendMessageW(0xFFFF, 0x112, 0xF170, 2)

def OnPc ():
    print("ONpc")
    ctypes.windll.user32.SendMessageW(0xFFFF, 0x112, 0xF170, -1)
# # Подождать некоторое время (например, 2 секунды)
# time.sleep(5)

