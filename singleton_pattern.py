class Singleton:
    _instance = None
    
    def __init__(self) -> None:
        if Singleton._instance != None:
            raise Exception("Singlogton Class")
        Singleton._instance = self
    
    def getinstance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance
    
    
s = Singleton.getinstance()
print(s)

b = Singleton.getinstance()
print(b)
    