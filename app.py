# print("Отобразить 16 фильмов")

from flask import Flask, render_template

app = Flask(__name__)

import urllib.request, json 
with urllib.request.urlopen()
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
