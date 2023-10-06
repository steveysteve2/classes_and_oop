
class Phone:

    def __init__(self, m, l, rp):          #self parameter keeps variables separated by instances    
        self.__manufact = m          #double _ ensures the attributes are hidden;
        self.__model = l             #this protects the attributes and makes the mutator method 
        self.__retail_price = rp     #the only way to change
    
    def set_manufact(self, m):
        self.__manufact = m

    def set_model(self, l):
        self.__model = l
    
    def set_retail_price(self, rp):
        self.__retail_price = rp
    
    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model
    
    def get_retail_price(self):
        return self.__retail_price
