from datetime import date as d

class Student:

    def __init__(self, i, n, dob, c):          #self parameter keeps variables separated by instances    
        self.__Student_ID = i          #double _ ensures the attributes are hidden;
        self.__Name = n
        self.__dob = dob             #this protects the attributes and makes the mutator method 
        self.__class = c.lower()
        self.__register = ''
        self.age = 0                   #the only way to change
    
    def calc_age(self):
        current_year = d.today().year
        doblist = self.__dob.split('/')
        year = int(doblist[2])
        self.__age = current_year-year

    def calc_register_date(self):
        if self.__class == 'f':
            self.__register = "4/10 - 4/12"
        elif self.__class == 's':
            self.__register =  "4/7 - 4/9"
        elif self.__class == 'jr':
            self.__register == "4/4 - 4/6"
        elif self.__class == 'sr':
            self.__register == "4/1 - 4/3"
        else:
            return "Please enter valid classfication"
        
    def get_age(self):
        return self.__age
    
    def get_register(self):
        return self.__register
