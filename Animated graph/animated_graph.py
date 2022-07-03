from time import time
import matplotlib.pyplot as plt
import pandas as pd
import PySimpleGUI as sg
import numpy as np
import imageio
import os
files = os.listdir("C:/Users/JeanK/OneDrive/Bureaublad/rocket/Rocket Data/Motor_data_calculations/Animated graph/Images")

def file_info():
    sg.theme("DarkTeal2")
    layout = [[sg.T("")], [sg.Text("Choose the Data file: "), sg.Input(key="-IN2-" ,change_submits=True), sg.FileBrowse(key="-IN-")],[sg.Button("Submit")]]
    window = sg.Window('Animated graph', layout, size=(600,150))
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
    t_animated = []
    f_animated = []
    plt.xlabel("time(s)")
    plt.ylabel("thrust(N)")
    plt.title("thrust chart")
    plt.grid()
    plt.ylim(ymin=0)
    plt.xlim(xmin=0)
    figure = plt.gcf() # get current figure
    figure.set_size_inches(25, 12)
    for i in range(len(t)):
        if(i==len(t)-1):
            plt.plot([], [], ' ', label="Area under curve: " + str(a))
            plt.legend(loc=9, prop={'size': 20})
        t_animated.append(t[i])
        f_animated.append(f[i])
        plt.xticks(np.arange(0, max(t_animated), 0.1))
        plt.yticks(np.arange(0, max(f_animated)+1, 1))
        plt.fill_between(
        x= t_animated, 
        y1= f_animated, 
        color= "b",
        alpha= 0.2)
        plt.plot(t_animated, f_animated)
        plt.savefig(f'C:/Users/JeanK/OneDrive/Bureaublad/rocket/Rocket Data/Motor_data_calculations/Animated graph/Images/{i:005}', dpi=100, facecolor = 'white')
        if(i == len(t)-1):
            
            for x in range(50):
                x += len(t)
                plt.savefig(f'C:/Users/JeanK/OneDrive/Bureaublad/rocket/Rocket Data/Motor_data_calculations/Animated graph/Images/{x:005}', dpi=100, facecolor = 'white')
    plt.close()

def gif():
    images = []
    img_path = [os.path.join('C:/Users/JeanK/OneDrive/Bureaublad/rocket/Rocket Data/Motor_data_calculations/Animated graph/Images', file) for file in files]
    for img in img_path:
        images.append(imageio.imread(img))

    imageio.mimwrite('C:/Users/JeanK/OneDrive/Bureaublad/rocket/Rocket Data/Motor_data_calculations/Animated graph/Gif/animated_graph.gif', images, fps = 20)
def empty_folder():
    for f in files:
        os.remove("C:/Users/JeanK/OneDrive/Bureaublad/rocket/Rocket Data/Motor_data_calculations/Animated graph/Images/"+f)
data = pd.read_csv(str(file_info()))
#print(data)
time_data = data["time(s)"].tolist()
thrust_data = data["thrust(N)"].tolist()
#print(time_data)
#print(thrust_data)
a = area(time_data, thrust_data)
empty_folder()
graph(time_data, thrust_data, a)
gif()