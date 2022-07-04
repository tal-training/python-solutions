import urllib.request
import json
import time

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

def update_flights():
    r=urllib.request.urlopen('https://data.gov.il/api/3/action/datastore_search?resource_id=e83f763b-b7d7-479e-b172-ae981ddc6de5&limit=15')
    return json.loads(r.read().decode())

if __name__ == '__main__':
    while True:
        flights=update_flights()["result"]["records"]
        html=f"""
        <link rel="stylesheet" href="flights.css">
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