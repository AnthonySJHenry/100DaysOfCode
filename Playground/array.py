class Array:
    size = 0
    elements = ()

    def __init__(self, size, elem) -> None:
        self.size = size
        self.elements = elem
    
    def __str__(self):
        return str(self.elements)
    
    def appendOne(self, n):
        self.elements = self.elements + tuple(str(n))
        self.size += 1
        
        
if __name__ == "__main__":
    elems = (50, 40, 30, 45)
    arx = Array(10, elems)
    print(arx)
    arx.appendOne(2)
    print(arx)
    