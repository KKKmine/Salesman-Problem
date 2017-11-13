import numpy as np
import math
import time
import threading
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from Individual import Individual
from Population import Population
from Map import Map

POINT_POS_RANGE = 10

POINT_SIZE = 20
POPULATION_SIZE = 50
SELECTION_SIZE = 3
MUTATION_RATE = 0.03

isRun = False

myMap = Map(POINT_SIZE, POINT_POS_RANGE)
        
fig = plt.figure()
record_plt = fig.add_subplot(2,1,1)
record_plt.set_title("Salesman Problem\nPoint: "+str(POINT_SIZE))

myPopulation = []
map_plt = []
map_path = []
record_line = []

def ShowPath(index, indi):
    map_plt[index].set_title("Generation: "+str(myPopulation[index].generation)+"\nDistance: "+str(indi.GetDistance()))
    map_path[index].set_data(indi.GetPathPos())
    record_line[index].set_xdata(np.append(record_line[index].get_xdata(), myPopulation[index].generation))
    record_line[index].set_ydata(np.append(record_line[index].get_ydata(), indi.GetDistance()))
    if(record_plt.get_xlim()[1] < myPopulation[index].generation):
        record_plt.set_xlim([0, myPopulation[index].generation+100])

for i in range(3):
    myPopulation += [Population(POPULATION_SIZE, SELECTION_SIZE, MUTATION_RATE)]
    map_plt += [fig.add_subplot(2,3,4+i)]
    map_plt[i].set_xlim([0, POINT_POS_RANGE])
    map_plt[i].set_ylim([0, POINT_POS_RANGE])
    map_plt[i].plot(myMap.pointX, myMap.pointY, 'o')
    path, = map_plt[i].plot([], [])
    map_path += [path]
    line, = record_plt.plot([], [])
    record_line += [line]
    ShowPath(i, myPopulation[i].GetFittest())
record_plt.set_xlim([0, 1])
record_plt.set_ylim([0, record_line[0].get_ydata()[0]])

bRun = Button(plt.axes([0.8, 0.02, 0.1, 0.05]), "Run")
def runLoop():
    while(isRun):
        for i in range(3): 
            myPopulation[i].Evolve()
            ShowPath(i, myPopulation[i].GetFittest())
        fig.canvas.draw_idle()
def runButtonClick(event):
    global isRun
    if(isRun):
        isRun = False
    else:
        isRun = True
        threading.Thread(target = runLoop, name = "Population").start()
bRun.on_clicked(runButtonClick)

plt.show()
