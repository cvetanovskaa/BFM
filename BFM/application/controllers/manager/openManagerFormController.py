'''All imports usually come before the app.route'''
from application import app
from flask import request
from application.models import *
from application.config import *
from application.logic.validation import check_session
from application.models.vendortomarketModel import Vendortomarket
from application.models.marketModel import Market
from flask import \
    render_template, \
    session, \
    request, \
    url_for, \
    Markup, \
    redirect

@app.route('/manager/open/<int:MID>/')
@check_session()
def openManagerForm(MID):
    if request.method == "GET":
         managerForm=Market.get(Market.MID==MID)
         vendors = Vendortomarket.select().where(Vendortomarket.mid==managerForm.MID)
         return render_template("views/manager/openManagerForm.html",vendors=vendors, config = config, managerForm=managerForm, isManager=True,)
    
    elif request.method == "POST":
         market=Market.get(Market.MID==MID)
    return render_template("views/manager/openManagerForm.html", config = config, market=market, isManager=True,)
        
   

