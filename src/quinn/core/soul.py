
class Soul:
    NAME = "Quinn 1 point O"

    def __init__(self):
        self.__name = self.NAME
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.__name = name
    
    @name.deleter
    def name(self):
        self.__name = self.NAME