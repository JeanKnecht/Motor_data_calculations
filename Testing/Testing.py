import csv
f = open(r'C:\Users\JeanK\OneDrive\Bureaublad\rocket\Rocket Data\Motor_data_calculations\Testing\test_data.csv', 'w')
f.write("time(s),thrust(N)\n")


def function(x):
    return x*0.5

x_list = []
for i in range(10001):  #same dx(interval) as the thrust data -> sample rate is ~100sps -> 0.01
    dx = 100/10000

    x_list.append(dx*i) 

y_list = [function(i) for i in x_list]

for i in range(len(x_list)):
    f.write(str(x_list[i])+ "," +str(y_list[i]) + "\n")

f.close()
##area under curve -> s0-1000 1/2x