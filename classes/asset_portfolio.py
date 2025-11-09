from classes.digital_asset import DigitalAsset

class AssetPortfolio:
    def __init__(self, assets:list[DigitalAsset], filename: str = "digital_assets.csv"):
        self.__assets = assets
        self.__filename = filename

    def add_asset(self, asset: DigitalAsset):
        self.__assets.append(asset)

    def calculate_total_net_worth(self):
        total = 0
        for asset in self.__assets:
            total += (asset.calculate_value() - asset.get_cost)
        total = round(total, 2)
        return total

    def save_portfolio(self):
        f = open(self.__filename, "w")
        f.write(f"Cost\n")
        f.close()
        f = open(self.__filename, "a")
        for asset in self.__assets:
            f.write(asset.to_report_line())
        f.close()

    def load_portfolio(self):
        self.__assets = []







