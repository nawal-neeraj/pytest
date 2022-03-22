class Singleton:
    _instacne = None
    
    def __init__(self) -> None:
        if Singleton._instacne != None:
            raise Exception("Singleton class")
        Singleton._instacne = self
        self.number = 0
        
    def getInstance():
        if Singleton._instacne == None:
            Singleton()
        return Singleton._instacne
    
    def increment(self):
        incr = self.number = self.number + 1 
        return incr
    
    def decrement(self):
        decr = self.number = self.number - 1
        return decr
        
        
j = Singleton.getInstance()
s = Singleton.getInstance()
g = Singleton.getInstance()

first_instance = j.increment()
print(f"Count {first_instance} || and memory alocation {j}")

second_instance = s.increment()
print(f"Count {second_instance} || and memory alocation {s}")

third_instance = g.decrement()
print(f"Count {third_instance} || and memory alocation {g}")

