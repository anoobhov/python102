from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class square(shape):
    def __init__(self):
        self.side=4

    def calculate_area(self):
        return self.side*self.side      #if this not implemented then the code would throw an error



square=square()