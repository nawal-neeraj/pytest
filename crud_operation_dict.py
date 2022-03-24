from dict_crud.check.dict import getval


getval.set("nawalTwo", "neerajTwo")
print("--------All_the_data--------")
print(getval._store_data)

print("--------get_value--------")
print(getval.get("nawalTwo"))

print("--------delete_value--------")
print(getval.delete("nawalTwo"))