from dict_crud.check import DictStore
from typing import Dict
        
class GetVal(DictStore):
    _instance = None
    
    def __init__(self):
        if GetVal._instance != None:
            raise Exception("Singleton class")
        GetVal._instance = self
        
        self._store_data: Dict[str, str] = {}
        
    def getInstance():
        if GetVal._instance == None:
            GetVal()
        return GetVal._instance
        
    def set(self, key, value):
        self._store_data.update({key:value})
    
    def _get(self, key):
        v = self._store_data.get(key)
        return v
    
    def get(self, key):
        v = self._get(key)
        return v
    
    def delete(self, key):
        del self._store_data[key]
        

getval = GetVal.getInstance()