#-----------------------------------------------------------------------------
# Name:        Algorithms Assigment
# Purpose:     Implmenting Sorting and Searching algorithms to sort and 
#              search through an array of some objects
#
# References: 	This program uses the python random, time and os libraries, as
#               well as the matplotlib library to plot the collected data:
#               https://docs.python.org/3/library/random.html
#               https://docs.python.org/3/library/time.html
#               https://matplotlib.org/
#               
#               This program also uses a list of multiple names for random
#               object generation:
#               https://gist.github.com/ruanbekker/a1506f06aa1df06c5a9501cb393626ea
#                  
#               
#
# Author:      Mostafa Hussein
# Created:     15-Nov-2021
# Updated:     19-Nov-2021
#-----------------------------------------------------------------------------

from os import name
from cityGrid import CityGrid
from random import randint

# Load names
with open("names.txt", "r") as namesFile:
    possibleNames = namesFile.readline().split(",")

def createPerson(currCity, number):
    pickedNames = []
    for i in range(number):
        success = False
        name = possibleNames[randint(0,len(possibleNames)-1)]
        age = randint(1,99)
        while success == False:
            posX = randint(0,999)
            posY = randint(0,999)
            position = (posX,posY)
            success = currCity.addPerson(name, age, position)
        pickedNames.append(name)
    return pickedNames

for i in range(1, 100000, 1000):
    for j in range(3):
        newCity = CityGrid(1000,1000,i)
        tempPersPos = (0,0)
        newCity.sortBuildingsOnDist(tempPersPos)
        
        pickedNames = createPerson(newCity, i)
        
        newCity.sortOnAge()
        currPerson = None
        while currPerson == None:
            if len(pickedNames) == 1:
               nameToFind = pickedNames[0]
            else:
                nameToFind = pickedNames[randint(0,len(pickedNames)-1)]
            currPerson = newCity.findNamedPerson(nameToFind)
        maxPossDist = int((2*(999**2))**(1/2))
        distToFind = randint(0,maxPossDist)
        newCity.findLocation(distToFind, (0,0))
