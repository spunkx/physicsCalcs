import math
import csv
import os.path

def writeCSV(row1, row2, filename):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([row1, row2])
    

def checkCSV(filename, param1, param2):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([param1, param2])

        
def writeDisplacement(arr):
    filename = "displacementovertime.csv"
    checkCSV(filename, "s", "t")
    for elem in arr:
        writeCSV(elem[0], elem[1], filename)
    

def writeVelocity(arr):
    filename = "velocityovertime.csv"
    checkCSV(filename, "v", "t")
    for elem in arr:
        writeCSV(elem[0], elem[1], filename)

    

s = input("Enter displacement")
a = 9.8
tEnd = 553 #times by 1000 from 0.553
v = 0

#veolcity over time
velocityoverTime = []
#displacement over time
currDispl = 0
displacementoverTime = []
for i in range(0, tEnd+1):
    #u = v
    v = 0 + a * (i/1000)
    currDispl = 0 * (i/1000) + (1/2 * a) * ((i/1000)**2)
    pairvelTime = ((i/1000), -(round(v, 3)))
    pairdisplTime = ((i/1000), -(round(currDispl, 3)))

        
    velocityoverTime.append(pairvelTime)
    displacementoverTime.append(pairdisplTime)


writeDisplacement(displacementoverTime)
writeVelocity(velocityoverTime)
    
    


