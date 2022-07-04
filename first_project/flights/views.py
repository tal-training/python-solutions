from uuid import uuid4
from django.shortcuts import render
import modules.flights as fl
from modules.flights import Flight 
from .models import FlightModel
import uuid
# Create your views here.

from django.http import HttpResponse

def save_flights(flights:dict):
    for f in flights:        
        flight=FlightModel(key=uuid.uuid4(),*(Flight(f).__dict__.values()))
        flight.save()

def create_html():
    flights=fl.update_flights()["result"]["records"]
    save_flights(flights)
    html=f"""
    <link rel="stylesheet" href="/static/flights.css">
    <table id='flights'>
    {Flight(flights[0]).get_table_header()}
    """
    for f in flights:
        html+=Flight(f).to_html()+'\n'
    html+="<script src='/static/flights.js'></script>"
    return html 

def create_json():
    # for SPA version
    pass

def index(request):
    #return HttpResponse(Flight.objects.all())
    return HttpResponse(create_html())
    #return render()
