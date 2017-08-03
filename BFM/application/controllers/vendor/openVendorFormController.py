'''All imports usually come before the app.route'''
from application import app
from application.models import *
from application.config import *
from application.models import model
from application.models.vendortomarketModel import Vendortomarket
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
      

@app.route('/vendor/open/<int:VMID>/', methods=["POST","GET"])
def openVendorForm(VMID):
  if request.method == "GET":
    form = Vendortomarket.get(Vendortomarket.VMID == VMID) 
    marketTimes = retrieveMarkets()
    return render_template("views/vendor/vendorForm.html", isManager=True, config = config, marketTimes=marketTimes, form = form)
  elif request.method == "POST":
    flash("Your sales have been recorded")
    marketTimes = retrieveMarkets()
    data = request.form
    vendorType = "NA"
    form = 0
    MID = data['MID']
    producedSales = data['producedSales']
    plantSales = data['plantSales']
    artCraftSales   = data['artCraftSales']
    processedSales = data['processedSales']
    fiberSales = data['fiberSales']
    vendorMarket = model.Vendortomarket(vendor_type=vendorType,mid=MID,produced_sales=producedSales,plant_sales=plantSales,art_craft_sales=artCraftSales,processed_sales=processedSales,fiber_sales=fiberSales).save()
    return render_template("views/vendor/vendorForm.html", isManager=True, config = config, marketTimes=marketTimes, form=form)
        
   

