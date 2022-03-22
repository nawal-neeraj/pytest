tuple_value = {"name": "nawal", "program": "python", "level": "beginer"}

new_dict = {steps: value for (steps, value) in tuple_value.items() }
update_value = new_dict.values()

#only prints the values of tuple
print(f"values {new_dict.values()}")

#only prints the keys of tuple
print(f"values {new_dict.keys()}")


#updating tuples ----- similer to spread operater in Js
new_tuple = {"org": "value"}
for dict in new_dict:
    tuple_value.update(new_tuple)  
print(tuple_value)
