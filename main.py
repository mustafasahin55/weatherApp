from tkinter import *
from tkinter import ttk

from functions import *

API_KEY = 'e3c9fbab31d34ed89b484646242008'
CITY = "Kagithane"

icon_paths = {
    "Sunny": r"Icons\sun.png",
    "Cloudy": r"Icons\cloudy.png",
    "Storm": r"Icons\storm.png",
    "Clear": r"Icons\storm.png",
    "Default": r"Icons\default.png"
    #/*TODO*/
}

root = Tk()
root.title("Kağıthane 3 Saatlik Hava Durumu Ortalamaları")
root.geometry("600x400")
data = update_weather(API_KEY, CITY)
x = 1

for i in data.values():
    temp = i['temperature']
    hum = i['humidity']
    wind = i['wind']
    condition = i['con'].strip(" ")


    if condition == "Sunny":
        icon = PhotoImage(file=icon_paths["Sunny"])
    elif condition == "Cloudy":
        icon = PhotoImage(file=icon_paths["Cloudy"])
    elif condition == "Storm":
        icon = PhotoImage(file=icon_paths["Storm"])
    elif condition == "Clear":
        icon = PhotoImage(file=icon_paths["Storm"])
    else:
        icon = PhotoImage(file=icon_paths["Default"])

    tempLabel = Label(root, text=temp)
    humLabel = Label(root, text=hum)
    windLabel = Label(root, text=wind)
    image_label = Label(root,image=icon)

    l1 = Label(root,text="SICAKLIK: ")
    l1.grid(row=1,column=0)
    l2 = Label(root, text="NEM: ")
    l2.grid(row=2, column=0)
    l3 = Label(root, text="RÜZGAR: ")
    l3.grid(row=3, column=0)

    tempLabel.grid(row=1, column=x)
    humLabel.grid(row=2, column=x)
    windLabel.grid(row=3, column=x)
    image_label.grid(row=4, column=x)

    x = x + 1

root.mainloop()
