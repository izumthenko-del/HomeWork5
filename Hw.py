import colorama
import inspect
colorama.init()
print(f"Атрибути модуля: {dir(colorama)}")
print("-"*50)
from colorama import Fore
print(f"Атрибути класу Fore: {dir(Fore)}")
print("-"*50)
