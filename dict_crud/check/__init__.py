import abc

class DictStore:
    
    @abc.abstractmethod
    def set(self, key:str, value:str):
        raise NotImplemented
    
    @abc.abstractmethod
    def set(self, key:str, value:str):
        raise NotImplemented
    
    @abc.abstractmethod
    def get(self, key:str, value:str):
        raise NotImplemented
    
    @abc.abstractmethod
    def delete(self, key:str, value:str):
        raise NotImplemented
        
    @abc.abstractmethod
    def clear(self, key:str, value:str):
        raise NotImplemented