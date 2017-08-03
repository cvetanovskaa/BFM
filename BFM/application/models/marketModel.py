from application.models.util import *
from application.models.userModel import User

class Market (Model):
  MID                   = PrimaryKeyField()
  date                  = CharField(max_length=100)
  location              = CharField(max_length=100)
  market_manager        = ForeignKeyField(User)
  customer_count        = IntegerField(default=0)
  event                 = CharField(max_length=100,default="")
  weather               = CharField(max_length=100,default="")
  comments              = CharField(max_length=100,default="")
  vendors               = CharField(null=True)
  
  class Meta:
    database = getDB("bfm")

 