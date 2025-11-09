from classes.digital_asset import DigitalAsset
from classes.reportable import Reportable

class Mobile_app(DigitalAsset, Reportable):
    def __init__(self, name, cost, downloads: int, avg_rating: float):
        super().__init__(name, cost)
        self.__downloads = downloads
        self.__avg_rating = avg_rating

    def asset_type(self):
        return "MOBILE_APP"

    def calculate_value(self):
        value = self.__downloads * 0.5 + self.__avg_rating * 1000
        return value

    def to_report_line(self):
        return f"{self.asset_type()}, {self.get_name}, {self.get_registration_data}, {self.get_cost}, {self.__downloads}, {self.__avg_rating}, {self.calculate_value()}"



