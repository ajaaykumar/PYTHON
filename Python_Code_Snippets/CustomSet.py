""" 
https://www.youtube.com/watch?v=vCglQxt88VI

Why set items can't be indexed? The real reason | 2MinutesPy
"""
class CustomSet:
    def __init__(self, capacity=10) -> None:
        self.capacity = capacity
        self.table = [None] * self.capacity
    
    def hased(self, value):
        return hash(value) % self.capacity
    
    def add(self, value):
        index = self.hased(value)
        # Check for duplicates starting from the hased index
        while self.table[index] is not None:
            if self.table[index] == value:
                if self.table[index] == value:
                    return
            index = (index +1) % self.capacity
        
        self.table[index] = value

myset = CustomSet()
myset.add(2)
myset.add('Hi')
myset.add(12)
        







