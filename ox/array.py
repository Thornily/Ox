from types import ArrayType
from typing import Iterable

class Array(ArrayType):
    def __init__(self, iterable: Iterable):
        self.data = iterable
    
    def __repr__(self):
        return f'[{str(self.data).replace(",", "")}]'
    
    def __str__(self):
        return self.__repr__()

print(Array([1,2,3,4,5,6]))