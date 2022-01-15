from random import randint

class Block():
    def __init__(self, size, name):
        self.size = size
        self.name = name
    

arr = []
with open('sometext.txt', 'r') as file:
    current = file.readlines()
    for curr in current:
        curr = curr.rstrip().split(',')
        currSize = int(curr[0])
        currName = curr[1]
        newBlock = Block(currSize, currName)
        arr.append(newBlock)

for i in arr:
    print(f"Size: {i.size}, Name: {i.name}")


