#pip install tinydb
# (db.all())

from flask import Flask, render_template, request,make_response
import requests
from datetime import datetime
from tinydb import TinyDB, Query

db = TinyDB('FLASK/4 - IP weather/data/visit.json')
app = Flask(__name__)

@app.route('/') 
def index():
    ura_obsika = datetime.now()
# Pridobi IP naslov obiskovalca 
    if request.headers.get('X-Forwarded-For'): 
        ip = request.headers.get('X-Forwarded-For').split(',')[0] 
    else:
        ip = request.remote_addr  
    print(ip)  # Za debugging return  f"Vaš IP je: {ip}"`
    lokacija_ip_url  = f"https://free.freeipapi.com/api/json/{ip}"
    podatki_ip = requests.get(lokacija_ip_url).json()
    print(podatki_ip)
    drzava = podatki_ip["countryName"]
    dni = "1"
    lat = podatki_ip["latitude"]
    lon = podatki_ip["longitude"]
    vreme_kordinate_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m&forecast_days={dni}"
    #vreme_kordinate_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m&forecast_days=1"
    podatki_vreme = requests.get(vreme_kordinate_url).json()
    #print(podatki_vreme)
    #time = podatki_vreme["current"]["time"]
    #temperature = podatki_vreme["current"]["temperature_2m"]
    cas_sez = podatki_vreme["hourly"]["time"]
    datumi = []
    ure = []
    for cas in cas_sez:
        d, u = cas.split("T")  # razdeli "2026-03-11T01:00" v datum in uro
        datumi.append(d)
        ure.append(u)

    temp = podatki_vreme["hourly"]["temperature_2m"]
    print(temp)

    temp_time_zip = list(zip(datumi, ure, temp))
    print(f"SKUPAJ zip: {temp_time_zip}")
    #print(temp_time_zip["2026-03-10T00:00"])
    #for podatek_vreme in temp_time_zip:
        #print(podatek_vreme)
    db.insert({'ip':ip, 'time':ura_obsika})
    return render_template("index.html", ip=ip, lokacija=drzava,napoved=temp_time_zip)

@app.route('/obiskovalci') 
def obsikovalci():
    User = Query()
    vsi_zapisi = db.all()
    return render_template("obiskovalci.html", sez = vsi_zapisi)



app.run(debug=True)