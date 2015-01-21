class Robot:
    def __init__(self, name, arms, legs, bomb): 
        self.name = name 
        self.arms = arms 
        self.legs = legs
        self.bomb = bomb
        self.pos = 0

    def explod(self, thing):
        print("i exploded")
        print(thing)
    
    def walk(self):
        self.pos += 1
      
    def walkbackword(self):
        self.pos -= 1

#this is a commment!!
