# print("Отобразить 16 фильмов")

from flask import Flask, render_template

app = Flask(__name__)

import urllib.request, json 
with urllib.request.urlopen("http://tv.tenet.ua/iptv/all11/ajax.php?page=film&parentid=n&pagenum=0&keyword=&order=2&desc=0&moreparam=gofilm&firstvizov=2&interval=16&pravoobladatelid=1&canplayhls=1&hotelid=0&devtype=json&macaddr=3C:BD:3E:C6:62:60&agent=AndroidTV&serialnum=35464022664247&ipadress=192.168.100.42&sid=9SF4VfheFfeBiup9PsAkm2laboTtSDmv&api_version=2") as url:
    data = json.load(url)
film_name = data['name']
url_img = data['FLM_PIC_S']
film_year = data['FLM_YEAR']
film_description = data['description']
film_rating = data['rating']
for i in range(len(film_name)):
    if film_rating[i] != 0:
        print(f"{i} + {film_rating[i]}")
        

@app.route("/")
def homepage():
    return render_template("index.html", len = len(film_name), 
    url_img = url_img,  
    film_name = film_name, 
    film_year = film_year, 
    film_rating = film_rating, 
    film_description = film_description
    )