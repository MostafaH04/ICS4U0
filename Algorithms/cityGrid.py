from random import randint, getrandbits
from building import Building
import time
from person import Person

class CityGrid():
    '''
    A 2D city grid object comprised of building and people objects

    Attributes
    ----------
    possibleBuildingNames: str[]
        Holds possible building names for random building generator to use
        Set to ["coffee shops", "house", "school"] by default
    
    dimesions: tuple
        Holds sizes for both the height and width of the city grid in the format (length,width)
        Set to (200, 200) by default

    buildingNum: int
        Holds the number of buildings to be placed on the grid (thus also the number of buildings on the grid)
        Set to 25000 by default
    
    grid: building & person[][]
        Contains the 2 dimensional list that stores the people and building objects

    buildings: Building[]
        A list of the building objects placed on the current city grid
    
    people: People[]
        A list of the people objects placed on the current city grid

    Methods
    -------
    sortBuildingsOnDist(targetPosition: tuple) -> None
        Uses an implmentation of selection sort, to sort the list of buildings
        based on their distance from a target position
    
    addPerson(name: str, age:int, position: tuple) 

    '''
    def __init__(self, length = 200, width = 200, buildingNum = 25000, possibleNames = ["coffee shop", "house", "school"]):
        self.possibleBuildingNames = possibleNames
        self.dimensions = (length, width)
        self.buildingNum = buildingNum
        self.grid = None
        self.buildings = self._createGrid()
        self.people = []
    
    def _selectionSort(self,target): # New with resubmition
        # Sort Method: Selection Sort
        # Time Complexity: O(n^2)
        arr = self.buildings
        sortedArr = []
        wantedLen = len(arr)
        while len(sortedArr) < wantedLen:
            maxNum = 0
            
            for i in range(1, len(arr)):
                maxDist = self._distance(arr[maxNum].position, target)
                iDist = self._distance(arr[i].position, target)
                if iDist > maxDist:
                    maxNum = i
            sortedArr.insert(0, arr.pop(maxNum))


        
        return sortedArr

    def sortBuildingsOnDist(self, targetPosition):

        print("before:")
        self._dispArr(self.buildings[:20])
        self._dispArr(self.buildings[-20:])
       
        startTime = time.time()
        
        sortedArr = self._selectionSort(targetPosition)
        
        timeDiff = (time.time()-startTime)
        with open("timeDataSelection.csv", "a") as file:
            file.write(f"{self.buildingNum},{timeDiff}\n")
        
        self.buildings = sortedArr

        print("after:")
        self._dispArr(self.buildings[:20])
        self._dispArr(self.buildings[-20:])

        return None

    def addPerson(self, name, age, position):
        name = name
        age = age
        posX, posY = position
        if self._emptyLocation(position):
            newPerson = Person(name, age, position)
            self.grid[posY][posX] = newPerson
            self.people.append(newPerson)
            return True
        else:
            return False
    
    def _linearSearch(self, target): # New with resubmition
        # Search Method: Linear Search
        # Time Complexity: O(n)

        for i in range(len(self.people)):
            if self.people[i].name.upper() == target.upper():
                return i
        return None

    def findNamedPerson(self, name):
        
        print("before:")
        self._dispArr(self.people[:20])
        self._dispArr(self.people[-20:])

        startTime = time.time()
        self.people = self._quickSort(self.people)
        timeDiff = (time.time()-startTime)

        with open("timeDataQuick.csv", "a") as file:
            file.write(f"{len(self.people)},{timeDiff}\n")  

        print("after:")
        self._dispArr(self.people[:20])
        self._dispArr(self.people[-20:])

        startTime = time.time()
        personPos = self._linearSearch(name)
        timeDiff = (time.time()-startTime)

        with open("timeDataLinear.csv", "a") as file:
            file.write(f"{len(self.people)},{timeDiff}\n")
        
        return self.people[personPos]


    def _insertionSort(self): # New with resubmition
        # Sort Method: Insertion Sort
        # Time Complexity: O(n^2)
        arr = self.people

        for currPointer in range(1, len(arr)):
            while currPointer > 0 and arr[currPointer-1].age > arr[currPointer].age:            
                temp = arr[currPointer]
                arr[currPointer] = arr[currPointer-1]
                arr[currPointer-1] = temp
                currPointer -= 1
        
        return arr
    

    def sortOnAge(self):

        print("before:")
        self._dispArr(self.people[:20])
        self._dispArr(self.people[-20:])

        startTime = time.time()
        
        self.people = self._insertionSort()
        
        timeDiff = (time.time()-startTime)
        with open("timeDataInsertion.csv", "a") as file:
            file.write(f"{len(self.people)},{timeDiff}\n")
        
        print("after:")
        self._dispArr(self.people[:20])
        self._dispArr(self.people[-20:])

        return None

    def createDistanceMap(self, reference): # New with resubmition
        distMap = []
        for i in self.buildings:
            distMap.append(self._distance(i.position, reference))
        return distMap

    def _binarySearch(self, arr, target): # New with resubmition
        # Search Method: Binary Search
        # Time Complexity: O(logn) (without including sort function)
        left = 0
        right = len(arr) - 1
        while left <= right:
            piv = left + (right - left)//2
            if arr[piv] == target:
                return piv
            elif arr[piv] < target:
                left = piv + 1
            else:
                right = piv - 1
        
        return None

    def findLocation(self, targetDistance, reference):

        self.buildings.sort(key = lambda x:self._distance(x.position, reference))
        
        distMap = self.createDistanceMap(reference)

        startTime = time.time()
        
        buildingPos = self._binarySearch(distMap, targetDistance)

        timeDiff = (time.time()-startTime)
        with open("timeDataBinary.csv", "a") as file:
            file.write(f"{self.buildingNum},{timeDiff}\n")

        if buildingPos != None:
            return self.buildings[buildingPos]
        else:
            return None

    def _createGrid(self):
        gridLength, gridWidth = self.dimensions
        self.grid = []
        buildingArr = []
        
        for i in range(gridWidth):
            self.grid.append([])
            for j in range(gridLength):
                self.grid[i].append(None)

        count = 0
        for currBuild in range(self.buildingNum):
            positionPicked = False
            while positionPicked != True:
                y,x = (randint(0, gridWidth-1), randint(0, gridLength-1))
                if self.grid[y][x] == None:
                    positionPicked = True
            count += 1
            openStatus = bool(getrandbits(1))
            name = self.possibleBuildingNames[randint(0,len(self.possibleBuildingNames)-1)]
            currBuilding = Building(currBuild, name, (x,y), openStatus)

            self.grid[y][x] = currBuilding
            buildingArr.append(currBuilding)
        
        return buildingArr
    
    def _emptyLocation(self, target):
        x,y = target
        if self.grid[y][x] == None:
            return True
        
        return False

    def _distance(self, referencePosition, targetPosition):
        xRef, yRef = referencePosition
        xTarget, yTarget = targetPosition

        squareDiffX = abs(xRef - xTarget) ** 2
        squareDiffY = abs(yRef - yTarget) ** 2
        
        return (squareDiffX + squareDiffY) ** (1/2)

    def _dispArr(self, arr):
        for elem in arr:
            print(elem)

    def _quickSort(self, arr):
        # Sort Method: Quick Sort
        # Time Complexity: O(n*logn)

        piv = arr.pop(-1)
        pivName = piv.name.upper()
        pivArr = [piv]

        left = []
        right = []

        for i in arr:
            name = i.name.upper()
            compCharPick = 0
            while compCharPick+1 < min(len(name), len(pivName)) and ord(name[compCharPick]) == ord(pivName[compCharPick]):
                compCharPick += 1
            
            compCharName = ord(name[compCharPick])
            compCharPiv = ord(pivName[compCharPick])

            if compCharName == compCharPiv:
                if len(pivName) < len(name):
                    pivArr.append(i)
                else:
                    pivArr.insert(0, i)
            elif compCharName < compCharPiv:
                left.append(i)
            else:
                right.append(i)
        
        if len(right) > 1:
            right = self._quickSort(right)
        if len(left) > 1:
            left = self._quickSort(left)        

        return left + pivArr + right                   
            
