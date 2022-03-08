tuple_value = {"name": "nawal", "program": "python", "level": "beginer"}

new_dict = {steps: value for (steps, value) in tuple_value.items() }
update_value = new_dict.values()
print(f"values {new_dict.values()}")

new_tuple = {"org": "value"}
for dict in new_dict:
    tuple_value.update(new_tuple)  
print(tuple_value)



class Callfunc:
    def __init__(self) -> None:
        pass 
    
    def __call__(self, a, b):
         print(f"using call function {a + b}")
        
callinstance = Callfunc()

callinstance(2,3)
