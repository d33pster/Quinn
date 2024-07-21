
from os import getcwd, listdir

class Name:
    def __init__(self, type: str = "audio", directory: str = getcwd()):
        self.name = type + "-001"
        # self.directory = directory
        self.files = listdir(directory)
    
    @property
    def assign(self) -> str:
        # list dirs from the given dir
        # files = listdir(self.directory)

        while self.name in self.files:
            type = self.name.split("-")[0]
            updated_number = str(int(self.name.split("-")[1]) + 1)
            while len(updated_number) < 3:
                updated_number = "0" + updated_number
            
            self.name = type + "-" + updated_number
        
        return self.name
    
    def check(self, name: str) -> bool:
        if name in self.files:
            return True
        else:
            return False