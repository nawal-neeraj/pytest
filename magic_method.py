class Callfunc:
   
    def __init__(self) -> None:
        pass
    
    def __call__(self, a, b):
         print(f"using call function {a + b}")
         print(Callfunc.name)
    
    def display(self):
        
        print("member method")
        
#Creating instance of class
callinstance = Callfunc()

#accessing __call__ method
callinstance(2,3)

#accessing member method
callinstance.display()