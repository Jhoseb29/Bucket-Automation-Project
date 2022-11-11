
class File(object):

    def __init__(self) -> None:
        
        self.name = ''
        self.size = 0
        self.path = ''
    
    def __str__(self) -> str:
        return f'{self.name} {self.size} {self.path}'