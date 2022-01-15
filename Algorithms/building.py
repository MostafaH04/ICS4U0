class Building():
    def __init__(self, number, name, position, openStatus):
        self.number = number
        self.name = name
        self.position = position
        self.openStatus = openStatus
    
    def __str__(self):
        num = self.number
        name = self.name
        pos = self.position
        openStat = self.openStatus
        return f"number:{num}, name: {name}, position: {pos}, open: {openStat}"