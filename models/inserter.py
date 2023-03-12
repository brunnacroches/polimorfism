from typing import Dict, Type
from models.repository import Repository

class Inserter:
    def __init__(self, repository: Type[Repository]) ->  None:
        self.__repo = repository
    
    def insert_data(self, name: str, age: int) -> Dict:
        record = self.__repo.select(name)
        if record:
            raise Exception('The record already exists')
        
        new_record = self.__repo.insert(name, age)
        return new_record
