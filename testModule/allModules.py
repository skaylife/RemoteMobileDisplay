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



# def testFunc():
#     data = "testFunction"
#     return data