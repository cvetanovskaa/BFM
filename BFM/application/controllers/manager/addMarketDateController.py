'''All imports usually come before the app.route'''
from application import app
from flask import request
from application.models import *
from application.config import *
from application.logic.validation import check_session,getUserFromToken
from application.models.marketModel import Market   

from flask import \
    render_template, \
    session, \
    request, \
    url_for, \
    Markup, \
    redirect

@app.route('/manager/addMarket', methods=["POST","GET"])
@check_session()
def addMarketDate():
    if request.method == "GET":
        return render_template("views/manager/addMarket.html", config = config, isManager=True)
    elif request.method == "POST":
        user= getUserFromToken(session['token'])
        data=request.form
        new_market=Market.create(location=data['location'],date=data['time'],market_manager_id=user.UID)
        return redirect(url_for("marketView"))
        
   

