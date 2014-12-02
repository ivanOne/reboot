__author__ = 'ivan'
import os
try:
    hour = int(input("Через сколько часов выключить?"))
    minutes = int(input("Минуты?"))
    hour = hour*60*60
    minutes = minutes*60
    time = hour+minutes
    os.system("shutdown -s -t "+str(time))
except ValueError:
    print("Не верно введены данные")






