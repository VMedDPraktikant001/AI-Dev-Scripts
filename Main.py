#Importing necessary modules
import matplotlib.pyplot as plt 
import csv
from datetime import datetime
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

#setting important global variables
workingdir = os.getcwd()
#heartrate Vmedd
x = [] 
y = []
#heartrate EKG
x1 = []
y1 = []
#breathingrate Vmedd
x2 = []
y2 = []
#breathingrate EKG
x3 = []
y3 = []

#Version Number output
print("Software Version 1.4")

#directory finder GUI
Tk().withdraw()
globaldir = askdirectory(title="Bitte wählen sie den Ordner aus in dem sich die CSV dateien befinden")
globaldir = globaldir.replace("/", "\\")

#finds the two csv files and saves their directories 
filelist = os.listdir(globaldir)
for file in filelist:
    if "Pat_" in file:
        konvertedfilename = file
    elif file == "VMedDHealthMonitorResults.csv":
        vmeddfilename = file

konvertedfiledir = globaldir + "\\" + konvertedfilename
vmeddfiledir = globaldir + "\\" + vmeddfilename

#creates a figure 
fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle("CSV Vergleich")
ax1.set_title("Herzfrequenz")
ax2.set_title("Atemfrequenz")

#plots the heartrate and breathingrate graphs
with open(vmeddfiledir, "r", encoding="utf-8") as csvfile1:
    plots = csv.reader(csvfile1, delimiter=";")
    for row in plots:
        if row[1] != (" Heartrate"):
            if len(row[0]) == 23:
                x.append(datetime.strptime(row[0], r"%Y-%m-%d_%H:%M:%S:%f"))
                y.append(int(float(row[1].replace(",", "."))))
                x2.append(datetime.strptime(row[0], r"%Y-%m-%d_%H:%M:%S:%f"))
                y2.append(int(float(row[2].replace(",", "."))))
            else: 
                x.append(datetime.strptime(row[0], r"%Y-%m-%d_%H:%M:%S"))
                y.append(int(float(row[1].replace(",", "."))))
                x2.append(datetime.strptime(row[0], r"%Y-%m-%d_%H:%M:%S"))
                y2.append(int(float(row[2].replace(",", "."))))
ax1.plot(x,y, label="Radar", color="black")
ax1.legend()
ax2.plot(x2,y2, label="Radar", color="black")
ax2.legend()

with open(konvertedfiledir, "r", encoding="utf-8") as csvfile2:
    plots = csv.reader(csvfile2, delimiter=";")
    for row in plots: 
        if row[1] != (" Heartrate"):
            x1.append(datetime.strptime(row[0], r"%Y-%m-%d_%H:%M:%S"))
            y1.append((int(row[1].replace("?","0"))))
            x3.append(datetime.strptime(row[0], r"%Y-%m-%d_%H:%M:%S"))
            y3.append((int(row[2].replace("?","0"))))
ax1.plot(x1,y1, label = "EKG", color="red")
ax1.legend()
ax2.plot(x3,y3, label = "EKG", color = "red")
ax2.legend()

#settings scales
ax1 

#makes the plot appear
ax1.grid()
ax2.grid()
ax1.set_ylim(40,120)
ax2.set_ylim(0,40)
plt.show()

#make it recognize whether milliseconds present 