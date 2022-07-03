from time import time
import matplotlib.pyplot as plt
import pandas as pd
import PySimpleGUI as sg
import numpy as np

def file_info():
    sg.theme("DarkTeal2")
    layout = [[sg.T("")], [sg.Text("Choose the Data file: "), sg.Input(key="-IN2-" ,change_submits=True), sg.FileBrowse(key="-IN-")],[sg.Button("Submit")]]
    window = sg.Window('My File Browser', layout, size=(600,150))
    while True:
        event, values = window.read()
        print(values["-IN2-"])
        if event == sg.WIN_CLOSED or event=="Exit":
            break
        elif event == "Submit":
            print(values["-IN-"])
            return str(values["-IN-"])
def area(x, y):
    sum_area = 0
    n = len(x)
    dx = (x[-1] - x[0])/n
    print(n)
    print(dx)
    for i in range(n-1):
        area = ((y[i] + y[i+1])/2) * dx
        sum_area += area
        
    return sum_area
def graph(t,f,a):
    plt.plot(t, f)
    plt.xlabel("time(s)")
    plt.ylabel("thrust(N)")
    plt.title("thrust chart")
    plt.grid()
    plt.plot([], [], ' ', label="Area under curve: " + str(a))
    plt.xticks(np.arange(0, max(t), 0.1))
    plt.yticks(np.arange(0, max(f)+1, 1))
    plt.ylim(ymin=0)
    plt.xlim(xmin=0)
    plt.legend(loc=9, prop={'size': 20})
    plt.fill_between(
        x= t, 
        y1= f, 
        color= "b",
        alpha= 0.2)
    plt.show()
data = pd.read_csv(str(file_info()))
#print(data)
time_data = data["time(s)"].tolist()
thrust_data = data["thrust(N)"].tolist()
#print(time_data)
#print(thrust_data)
a = area(time_data, thrust_data)
graph(time_data, thrust_data, a)