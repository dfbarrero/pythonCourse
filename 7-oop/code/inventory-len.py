class Inventory:
    def __init__(self, items=[]): 
        self._items = items    

    def __str__(self):  
        return ': '.join(self._items)

    def __len__(self):
        return len(self._items)

if __name__ == '__main__':
    inventory = Inventory(["map", "key"]) 
    print(inventory)        # Outputs "map: key"
    print(len(inventory))   # Outputs "2"
