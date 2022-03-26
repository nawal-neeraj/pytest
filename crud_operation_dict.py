from dict_crud.check.dict import GetVal


getval = GetVal.getInstance()
print(f"first instance==> {getval}")

getval_one = GetVal.getInstance()
print(f"Second instance==> {getval}")


getval.set("nawalTwo", "neerajTwo")
print("--------All_the_data--------")
print(getval_one._store_data)

print("--------get_value--------")
print(getval.get("nawalTwo"))

print("--------delete_value--------")
print(getval.delete("nawalTwo"))

print("--------get_empty_value--------")
print(getval.get("nawalTwo"))