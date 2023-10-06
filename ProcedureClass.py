class Procedure:

    def __init__(self, n, d, np, ch, p):          #self parameter keeps variables separated by instances    
        self.__name_pro = n
        self.__date = d
        self.__name_prac = np
        self.__charge = ch
        self.__patientID = p
        self.total = 0


    def get_name_pro(self):
        return self.__name_pro
    
    def get_name_prac(self):
        return self.__name_prac
    
    def get_date(self):
        return self.__date
        
    def get_charge(self):
        return self.__charge
    
    def get_patientID(self):
        return self.__patientID

