import urllib.request
import json
import time
import datetime
import sqlite3
import http.server
import threading

class FlightsHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        return "post"

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes(make_response(),'utf8'))
        #self.send_response(make_response())

class Flight:
    def __init__(self, flight:dict):
        self.company=flight['CHOPERD']
        self.date=flight['CHSTOL']
        self.city=flight["CHLOC1TH"]
        self.country=flight["CHLOC1CH"]
        self.status=flight["CHRMINH"]
    
    def to_html(self):
        html_row="<tr>"
        for p in self.__dict__:
            html_row+=f"<td id='{p}'>{self.__dict__[p]}</td>"
        return html_row

    def get_table_header(self):
        html_row="<tr>"
        for p in self.__dict__:
            html_row+=f"<th>{p}</th>"
        return html_row.title()

def make_response():
        flights=update_flights()["result"]["records"]
        save_flights(flights)
        # Note meta header required for hebrew 
        html=f"""              
        <head>
        <meta charset="UTF-8">
        </head>
        <link rel="stylesheet" href="flights.css">
        <h3>Last Updated: {datetime.datetime.now()}</h3>
        <table id='flights'>
        {Flight(flights[0]).get_table_header()}
        """
        for f in flights:
            html+=Flight(f).to_html()+'\n'
        html+="<script src='flights.js'></script>"
        return html

def save_flights(flights:dict):
    con=sqlite3.connect("flights.db")
    cur=con.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS FLIGHTS {str(tuple(Flight(flights[1]).__dict__))}")
    for f in flights:
        fo=Flight(f)
        sql=f"INSERT INTO FLIGHTS VALUES {str(tuple(fo.__dict__.values()))}"
        cur.execute(sql)
        con.commit()
    con.close()

def update_flights():
    r=urllib.request.urlopen('https://data.gov.il/api/3/action/datastore_search?resource_id=e83f763b-b7d7-479e-b172-ae981ddc6de5&limit=15')
    return json.loads(r.read().decode())

def start_server():
    server=http.server.HTTPServer(("localhost",8090),http.server.SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    t = threading.Thread(target=start_server, args=())
    t.start()
    while True:
        flights=update_flights()["result"]["records"]
        save_flights(flights)
        # Note meta header required for hebrew 
        html=f"""              
        <head>
        <meta charset="UTF-8">
        </head>
        <link rel="stylesheet" href="flights.css">
        <h3>Last Updated: {datetime.datetime.now()}</h3>
        <table id='flights'>
        {Flight(flights[0]).get_table_header()}
        """
        for f in flights:
            html+=Flight(f).to_html()+'\n'
        html+="<script src='flights.js'></script>" 
        f=open("flights.html",'w')
        f.write(html)
        f.close()
        time.sleep(120)