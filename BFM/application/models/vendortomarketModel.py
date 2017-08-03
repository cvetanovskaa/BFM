from application.models.util import *
from application.models.marketModel import Market

class Vendortomarket (Model):
   vendor_type              = CharField(max_length=100)
   VMID                     = PrimaryKeyField()
   mid                      = ForeignKeyField(Market)
   processed_sales          = FloatField(default=0)
   produced_sales           = FloatField(default=0)
   plant_sales              = FloatField(default=0)
   art_craft_sales          = FloatField(default=0)
   fiber_sales              = FloatField(default=0)
   other_description        = CharField(null = True)
   other_sales              = FloatField(null = True)
   class Meta:
        database = getDB("bfm")

 