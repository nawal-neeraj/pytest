class BaseClass:
    
    _classvariable = None
    
    def __init__(self):
        self.instance_varable = None
        
    def show_variable(self):
        print(f"instance variable not updated: {self.instance_varable}")
        
    def show_class_variable(cls):
        print(f"class variable updated using class method: {cls._classvariable}")
        
        
    def update_instance_variable(self, val):
        self.instance_varable = val
        
        
    @classmethod
    def update_class_varable(cls, val):
        cls._classvariable = val
        
