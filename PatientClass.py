
class Patient:

    def __init__(self, i, n, add, p, vs):          #self parameter keeps variables separated by instances    
        self.__patient_ID = i          #double _ ensures the attributes are hidden;
        self.__name = n
        self.__address = add             #this protects the attributes and makes the mutator method 
        self.__phone = p                   #the only way to change
        self.__veteran_status = vs
    
    def get_ID(self):
        return self.__patient_ID

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_phone(self):
        return self.__phone
    
    def get_veteran_status(self):
        return self.__veteran_status