from flask import Flask
from flask import url_for
from flask import request
from flask import redirect
from flask import render_template

from config import LANG
from config import PARAMS
from config import API_KEY
from config import BASE_URL

from functions import tokio, temp_tokio, min_temp_tokio, max_temp_tokio
from functions import seul, temp_seul, min_temp_seul, max_temp_seul
from functions import delhi, temp_delhi, min_temp_delhi, max_temp_delhi
from functions import bombai, temp_bombai, min_temp_bombai, max_temp_bombai
from functions import saopaulo, temp_saopaulo, min_temp_saopaulo, max_temp_saopaulo
from functions import mexicocity, temp_mexicocity, min_temp_mexicocity, max_temp_mexicocity
from functions import newyork, temp_newyork, min_temp_newyork, max_temp_newyork
from functions import jakarta, temp_jakarta, min_temp_jakarta, max_temp_jakarta
from functions import shangai, temp_shangai, min_temp_shangai, max_temp_shangai

import requests

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        
        try:
            city = request.form['city']
            
            url = (f'{BASE_URL}appid={API_KEY}&q={city}&units={PARAMS}&lang={LANG}')
            response = requests.get(url).json()
            
            temp = round(response['main']['temp'])
            min_temp = round(response['main']['temp_min'])
            max_temp = round(response['main']['temp_max'])
            humidity = round(response['main']['humidity'])
            pressure = round(response['main']['pressure'])
            visibility = round(response['visibility']/1000)
            wind = round(response['wind']['speed'])
            
            return render_template('index.html',
                                    city=city,
                                    temp=temp,
                                    min_temp=min_temp,
                                    max_temp=max_temp,
                                    humidity=humidity,
                                    pressure=pressure,
                                    visibility=visibility,
                                    wind=wind,
                                    tokio=tokio,
                                    temp_tokio=temp_tokio,
                                    min_temp_tokio=min_temp_tokio,
                                    max_temp_tokio=max_temp_tokio,
                                    seul=seul,
                                    temp_seul=temp_seul,
                                    min_temp_seul=min_temp_seul,
                                    max_temp_seul=max_temp_seul,
                                    delhi=delhi,
                                    temp_delhi=temp_delhi,
                                    min_temp_delhi=min_temp_delhi,
                                    max_temp_delhi=max_temp_delhi,
                                    bombai=bombai,
                                    temp_bombai=temp_bombai,
                                    min_temp_bombai=min_temp_bombai,
                                    max_temp_bombai=max_temp_bombai,
                                    saopaulo=saopaulo,
                                    temp_saopaulo=temp_saopaulo,
                                    min_temp_saopaulo=min_temp_saopaulo,
                                    max_temp_saopaulo=max_temp_saopaulo,
                                    mexicocity=mexicocity,
                                    temp_mexicocity=temp_mexicocity,
                                    min_temp_mexicocity=min_temp_mexicocity,
                                    max_temp_mexicocity=max_temp_mexicocity,
                                    newyork=newyork,
                                    temp_newyork=temp_newyork,
                                    min_temp_newyork=min_temp_newyork,
                                    max_temp_newyork=max_temp_newyork,
                                    jakarta=jakarta,
                                    temp_jakarta=temp_jakarta,
                                    min_temp_jakarta=min_temp_jakarta,
                                    max_temp_jakarta=max_temp_jakarta,
                                    shangai=shangai,
                                    temp_shangai=temp_shangai,
                                    min_temp_shangai=min_temp_shangai,
                                    max_temp_shangai=max_temp_shangai)
        except:
            redirect(url_for('index'))
        
    return render_template('index.html',tokio=tokio,
                                        temp_tokio=temp_tokio,
                                        min_temp_tokio=min_temp_tokio,
                                        max_temp_tokio=max_temp_tokio,
                                        seul=seul,
                                        temp_seul=temp_seul,
                                        min_temp_seul=min_temp_seul,
                                        max_temp_seul=max_temp_seul,
                                        delhi=delhi,
                                        temp_delhi=temp_delhi,
                                        min_temp_delhi=min_temp_delhi,
                                        max_temp_delhi=max_temp_delhi,
                                        bombai=bombai,
                                        temp_bombai=temp_bombai,
                                        min_temp_bombai=min_temp_bombai,
                                        max_temp_bombai=max_temp_bombai,
                                        saopaulo=saopaulo,
                                        temp_saopaulo=temp_saopaulo,
                                        min_temp_saopaulo=min_temp_saopaulo,
                                        max_temp_saopaulo=max_temp_saopaulo,
                                        mexicocity=mexicocity,
                                        temp_mexicocity=temp_mexicocity,
                                        min_temp_mexicocity=min_temp_mexicocity,
                                        max_temp_mexicocity=max_temp_mexicocity,
                                        newyork=newyork,
                                        temp_newyork=temp_newyork,
                                        min_temp_newyork=min_temp_newyork,
                                        max_temp_newyork=max_temp_newyork,
                                        jakarta=jakarta,
                                        temp_jakarta=temp_jakarta,
                                        min_temp_jakarta=min_temp_jakarta,
                                        max_temp_jakarta=max_temp_jakarta,
                                        shangai=shangai,
                                        temp_shangai=temp_shangai,
                                        min_temp_shangai=min_temp_shangai,
                                        max_temp_shangai=max_temp_shangai)

if __name__ == '__main__':
    
    app.run(port=5000,debug=True)