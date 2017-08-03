# See the configure documentation for more about
# this library.
# http://configure.readthedocs.io/en/latest/#
from configure import Configuration
from datetime import timedelta
from application.config import config
from application.models import getModelFromName
from functools import wraps
from flask import request, redirect, url_for, session, abort, flash, app
import os, re, time
from application.models import model
from application import app
from time import strptime


def getUserFromEmail(email):
  T = model.User
  q = model.User.select().where(T.email == email)
  if q.exists():
    for row in q:
      return row
  else:
    return False

def tokenExsist(tok):
  '''Checks to make sure that the token exist in our system'''
  T = model.User
  q = model.User.select().where(T.token == tok)
  if q.exists():
    return True
  else:
    return False

def tokenOk(tok):
  token = tokenExsist(tok)
  if token != False:
    T = model.User
    user = T.get(T.token == tok)
    now  = time.time()
    isTokenValid = False
    timeLeft     = (now - float(user.time))
    if user.isAdmin == True:
      isTokenVaild = timeLeft < (config.application.tokenTimeout * 60 * 5)
    else:
      isTokenVaild = timeLeft < (config.application.tokenTimeout * 60)
    if isTokenVaild:
      print "We have {0} left.".format(timeLeft)
      return True
  return False

def getUserFromToken(tok):
  acceptToken = tokenExsist(tok)
  if acceptToken == True:
    try:
      T = model.User
      for row in T.select().where(T.token==tok):
        return row
    except Exception as e:
      print e
  return None
  
def setSessionVariables(tok):
  user  = getUserFromToken(tok)
  session['email'] = user.email
  session['token']   = tok
  return True
  
def check_session ():
  def decorator (fun):
    @wraps(fun)
    def decorated_fun (*args, **kwargs):
      if session.get('token') and session.get('email'):
        session.permanent=True
        app.permanent_session_lifetime = timedelta(minutes=60)
        return fun(*args, **kwargs)
      else:
        flash("System could not find session, may be expired.")
        return redirect(url_for("getEmail"), code = 302)
    return decorated_fun
  return decorator
  
  

