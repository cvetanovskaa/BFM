'''All imports usually come before the app.route'''
from application import app
from flask import request
from application.models import *
from application.config import *
from application.logic.validation import check_session
from application.models.marketModel import Market
from application.models.vendortomarketModel import Vendortomarket
from flask import \
    render_template, \
    session, \
    request, \
    url_for, \
    Markup, \
    redirect

@app.route('/manager/managerForm/', methods=["POST","GET"])
@check_session()
def managerForm():
    if request.method == "GET":
        markets=Market.select()
        return render_template("views/manager/managerForm.html",date=0, config = config, isManager=True, markets=markets)
    elif request.method == "POST":
        data=request.form
        print data
        if data['postForm']=="select":
            market=Market.get(Market.MID==data['MID'])
            vendors=Vendortomarket.select().where(Vendortomarket.mid==data['MID'])
            processed_sales=0
            produced_sales=0
            plant_sales=0
            art_craft_sales=0
            fiber_sales=0
            other_sales=0
            
            for vendor in vendors:
                processed_sales += vendor.processed_sales
                produced_sales += vendor.produced_sales
                plant_sales += vendor.plant_sales
                art_craft_sales += vendor.art_craft_sales
                fiber_sales += vendor.fiber_sales
            total=processed_sales+produced_sales+plant_sales+art_craft_sales+fiber_sales
            return render_template("views/manager/managerForm.html", processed_sales = processed_sales,
                                                                     produced_sales  = produced_sales,
                                                                     plant_sales     = plant_sales,
                                                                     art_craft_sales = art_craft_sales,
                                                                     fiber_sales     = fiber_sales,
                                                                     config = config, 
                                                                     total = total,
                                                                     date=1,
                                                                     market=market,
                                                                     isManager=True)
        elif data['postForm']=="submit":
            market=Market.get(date=data['date'])
            market.event=data['event']
            market.weather=data['weather']
            market.comments=data['specialComments']
            vendors=request.form.getlist('vendorList')
            market.vendors=', '.join(vendors)
            market.save()
            return redirect(url_for("marketView"))
        
   


