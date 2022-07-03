from time import time
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("C:/Users/JeanK/OneDrive/Bureaublad/rocket/Test 3/Data_3_fix.csv")
print(data)

time_data = data["time(s)"].tolist()
thrust_data = data["thrust(N)"].tolist()
print(time_data)
print(thrust_data)

def area(x, y):
    sum_area = 0
    n = len(x)
    dx = (x[-1] - x[0])/n
    for i in range(n-1):
        area = ((y[i] + y[i+1])/2) * dx
        sum_area += area
    return sum_area
def graph(t,f,a):
    plt.plot(t, f)
    plt.xlabel("time(s)")
    plt.ylabel("thrust(N)")
    plt.title("Thrust chart")
    plt.grid()
    plt.plot([], [], ' ', label="Area under curve: " + str(a))
    plt.legend()
    plt.fill_between(
        x= t, 
        y1= f, 
        color= "b",
        alpha= 0.2)

    plt.show()
a = area(time_data, thrust_data)
graph(time_data, thrust_data, a)