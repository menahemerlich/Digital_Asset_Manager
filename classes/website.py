from classes.digital_asset import DigitalAsset
from classes.reportable import Reportable

class Website(DigitalAsset, Reportable):
    def __init__(self, name, cost, monthly_traffic: int, monetization_rate: float):
        super().__init__(name, cost)
        self.__monthly_traffic = monthly_traffic
        self.__monetization_rate = monetization_rate

    def asset_type(self):
        return "WEBSITE"

    def calculate_value(self):
        value = self.__monthly_traffic * self.__monetization_rate * 12
        return value

    def to_report_line(self):
        return f"{self.asset_type()}, {self.get_name}, {self.get_registration_data}, {self.get_cost}, {self.__monthly_traffic}, {self.__monetization_rate}, {self.calculate_value()}"

