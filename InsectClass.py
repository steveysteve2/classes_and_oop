import random

class Insect:

    def __init__(self, w, l, n):          #self parameter keeps variables separated by instances    
        self.wings = w
        self.legs = l
        self.lenfly = 0
        self.name = n

    def lenflight(self):
        self.lenfly = random.randint(1,10)
    
    def get_len(self):
        return self.lenfly
    
    def get_name(self):
        return self.name