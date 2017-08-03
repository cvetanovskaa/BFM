'''All imports usually come before the app.route'''
from application import app
from application.models import *
from application.config import *
from application.models import model
import time

from flask import \
    render_template, \
    session, \
    request, \
    url_for, \
    Markup, \
    redirect, \
    flash

def retrieveMarkets():
  '''Use this to elminate old marketTimes'''
  T = model.Market()
  markets = T.select()
  if markets.exists():
    pass
  else:
    markets = None
  return markets
      

@app.route('/', methods=["POST","GET"])
def vendorForm():
  if request.method == "GET":
    marketTimes = retrieveMarkets()
    form = 0
    return render_template("views/vendor/vendorForm.html", config = config, marketTimes=marketTimes,form=form)
  elif request.method == "POST":
    flash("Your sales have been recorded")
    marketTimes = retrieveMarkets()
    data = request.form
    vend=request.form.getlist('vendorList')
    vt="N/A"
    MID = data['MID']
    producedSales = data['producedSales']
    plantSales = data['plantSales']
    artCraftSales   = data['artCraftSales']
    processedSales = data['processedSales']
    fiberSales = data['fiberSales']
    form = 0
    vendorMarket = model.Vendortomarket(vendor_type=', '.join(vend) ,mid=MID,produced_sales=producedSales,plant_sales=plantSales,art_craft_sales=artCraftSales,processed_sales=processedSales,fiber_sales=fiberSales).save()
    return render_template("views/vendor/vendorForm.html", config = config, marketTimes=marketTimes, form = form)
        
   

