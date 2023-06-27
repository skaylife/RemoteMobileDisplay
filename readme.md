## Импорт модулей и запуск из `main.py`

##### Структура папок:
```
project/
    main.py
    testModule/
        allModules.py
        testModules/
            oneModule.py
            twoModule.py
```

##### file - `oneModule.py`

```
def oneModuleFunc():
    print("oneModuleFunc")
```

##### file - `twoModule.py`
```
def twoModuleFunc():
    print("twoModuleFunc")
```

##### file - `allModules.py`
```
from .testModules.oneModule import oneModuleFunc
from .testModules.twoModule import twoModuleFunc 

def testFunc():
    oneModuleFunc()
    twoModuleFunc()
    print("testFunc")

# экспортируем функции func_one и func_two
__all__ = [
    'oneModuleFunc', 
    'twoModuleFunc',
    'testFunc'
]
```

##### file - `main.py`
```
from testModule.allModules import *

oneModuleFunc()
twoModuleFunc()
print("*******************")
testFunc()
```

##### Вывод в `console`

```
oneModuleFunc
twoModuleFunc
*******************
oneModuleFunc
twoModuleFunc
testFunc
```