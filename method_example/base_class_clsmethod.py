class BaseClass:
    
    _classvariable = None
    
    def __init__(self, val):
        self.instance_varable = val
        
    def show_variable(self):
        print(f"instance variable update direct from init: {self.instance_varable}")
        
    def show_class_variable(cls):
        print(f"class variable update direct from init: {cls._classvariable}")
        
    def update_instance_variable(self):
        self.instance_varable = None
        
        
    @classmethod
    def update_class_varable(cls, val):
        cls._classvariable = val
        
