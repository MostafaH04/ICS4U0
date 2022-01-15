class Person():
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
    
    def movePerson(self):
        yTranslation = int(input("How much forwards or backwards do you want to go? (positive = forward, negative = backward)"))
        xTranslation = int(input("How much forwards or backwards do you want to go? (positive = forward, negative = backward)"))

        self.position = (self.position[0] + xTranslation, self.position[1] + yTranslation)
        return None
    
    def __str__(self) -> str:
        name = self.name
        age = self.age
        pos = self.position
        
        return f"name: {name}, age: {age}, position: {pos}"