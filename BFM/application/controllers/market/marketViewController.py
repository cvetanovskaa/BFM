'''All imports usually come before the app.route'''
from application import app
from flask import request
from application.models import *
from application.config import *
from application.logic.validation import check_session
from application.models.marketModel import Market

from flask import \
    render_template, \
    session, \
    request, \
    url_for, \
    Markup, \
    redirect

@app.route('/marketView')
@check_session()
def marketView():
    markets=Market.select()
    return render_template("views/market/marketView.html", config = config, isManager=True, markets=markets)