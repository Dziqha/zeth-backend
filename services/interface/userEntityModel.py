from abc import ABC, abstractmethod
from datetime import datetime

class UserEntityModel(ABC):

    def __init__(self, user_id : str = None, name : str = None, category : str = None):
        self.user_id = user_id
        self.name = name
        self.category = category
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def get_by_id(self):
        pass

    @abstractmethod
    def get_by_category(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod 
    def delete(self):
        pass