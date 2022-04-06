from dict_crud.check.dict import GetVal


getval = GetVal.getInstance()


def add_values(value1, value2):
    
    getval.set(value1, value2)
    
    print("--------All_the_data--------")
    print(getval._store_data)

add_values("nawalTwo", "neerajTwo")
add_values("nawalOne", "neerajOne")
add_values("nawalThree", "neerajThree")
add_values("nawalTFour", "neerajFour")