import datetime
from abc import ABC, abstractmethod

class DigitalAsset(ABC):
    def __init__(self, name: str, cost: float):
        self.__name = name
        self.__registration_date = datetime.datetime.now()
        self.__cost = cost

    @property
    def get_name(self):
        return self.__name

    @property
    def get_registration_data(self):
        return self.__registration_date.isoformat()

    @property
    def get_cost(self):
        return self.__cost

    @abstractmethod
    def calculate_value(self):
        pass

    @abstractmethod
    def asset_type(self):
        pass