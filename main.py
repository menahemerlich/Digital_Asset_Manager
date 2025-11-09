from classes.website import Website
from classes.mobile_app import Mobile_app
from classes.asset_portfolio import AssetPortfolio

a = Mobile_app("gog", 20.5, 5, 7)
print(a.to_report_line())
AssetPortfolio.save_portfolio(a)