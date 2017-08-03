from application.models.util import *

class User (Model):
  UID                   = PrimaryKeyField()
  first_name            = CharField(max_length=100)
  last_name             = CharField(max_length=100)
  middle_initial        = CharField(null=True, max_length=1) #Why do we need this?
  email                 = CharField(max_length=100)
  isAdmin              = BooleanField(default=False)  
  time                  = TextField()
  token                 = TextField()
  class Meta:
    database = getDB("bfm")

 