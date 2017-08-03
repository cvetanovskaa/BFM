from application.models import classes
from application.config import *
from application.models import model

T = model.User
new_user = model.User(first_name="Cody",last_name="Myers",middel_initial="D",email="admin@gmail.com",isAdmin=True,time="0",token="lsdkjfl").save()
new_user = model.User(first_name="Daryl",last_name="Sullivan",middel_initial="Z",email="manager@gmail.com",isAdmin=False,time="0",token="lsdkjfl").save()
new_user = model.User(first_name="My",last_name="Test",middel_initial="E",email="codymyers63@gmail.com",isAdmin=False,time="0",token="lsdkjfl").save()


T = model.Market
new_market = model.Market(date="10/20/2016",location="School",market_manager=1,customer_count="10",event="No",weather="sunny",comments="Nice day").save()
new_market = model.Market(date="10/22/2016",location="Kentucky",market_manager=2,customer_count="31",event="No",weather="cold",comments="Happy Halloween").save()
new_market = model.Market(date="10/23/2016",location="Berea",market_manager=3,customer_count="16",event="Yes",weather="cloudy",comments="little").save()



T = model.Vendortomarket
new_vendor = model.Vendortomarket(vendor_type="mystery", processed_sales=123, plant_sales = 12, mid = 1).save()
new_vendor = model.Vendortomarket(vendor_type="something", produced_sales=33, plant_sales = 33, mid = 1).save()