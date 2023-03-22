from config import LANG
from config import PARAMS
from config import API_KEY
from config import BASE_URL

import requests

"""
Tokio
"""

tokio = 'Tokio'
            
url_tokio = (f'{BASE_URL}appid={API_KEY}&q={tokio}&units={PARAMS}&lang={LANG}')
tokio_response = requests.get(url_tokio).json()

temp_tokio = round(tokio_response['main']['temp'])
min_temp_tokio = round(tokio_response['main']['temp_min'])
max_temp_tokio = round(tokio_response['main']['temp_max'])

"""
Seul
"""

seul = 'Seul'
            
url_seul = (f'{BASE_URL}appid={API_KEY}&q={seul}&units={PARAMS}&lang={LANG}')
seul_response = requests.get(url_seul).json()

temp_seul = round(seul_response['main']['temp'])
min_temp_seul = round(seul_response['main']['temp_min'])
max_temp_seul = round(seul_response['main']['temp_max'])

"""
Delhi
"""

delhi = 'Delhi'
            
url_delhi = (f'{BASE_URL}appid={API_KEY}&q={delhi}&units={PARAMS}&lang={LANG}')
delhi_response = requests.get(url_delhi).json()

temp_delhi = round(delhi_response['main']['temp'])
min_temp_delhi = round(delhi_response['main']['temp_min'])
max_temp_delhi = round(delhi_response['main']['temp_max'])

"""
Bombai
"""

bombai = 'Bombai'
        
url_bombai = (f'{BASE_URL}appid={API_KEY}&q={bombai}&units={PARAMS}&lang={LANG}')
bombai_response = requests.get(url_bombai).json()

temp_bombai = round(bombai_response['main']['temp'])
min_temp_bombai = round(bombai_response['main']['temp_min'])
max_temp_bombai = round(bombai_response['main']['temp_max'])

"""
Sao Paulo
"""

saopaulo = 'Sao Paulo'
        
url_saopaulo = (f'{BASE_URL}appid={API_KEY}&q={saopaulo}&units={PARAMS}&lang={LANG}')
saopaulo_response = requests.get(url_saopaulo).json()

temp_saopaulo = round(saopaulo_response['main']['temp'])
min_temp_saopaulo = round(saopaulo_response['main']['temp_min'])
max_temp_saopaulo = round(saopaulo_response['main']['temp_max'])

"""
Ciudad de México
"""

mexicocity = 'Ciudad de México'
        
url_mexicocity = (f'{BASE_URL}appid={API_KEY}&q={mexicocity}&units={PARAMS}&lang={LANG}')
mexicocity_response = requests.get(url_mexicocity).json()

temp_mexicocity = round(mexicocity_response['main']['temp'])
min_temp_mexicocity = round(mexicocity_response['main']['temp_min'])
max_temp_mexicocity = round(mexicocity_response['main']['temp_max'])

"""
New York
"""

newyork = 'Nueva York'
        
url_newyork = (f'{BASE_URL}appid={API_KEY}&q={newyork}&units={PARAMS}&lang={LANG}')
newyork_response = requests.get(url_newyork).json()

temp_newyork = round(newyork_response['main']['temp'])
min_temp_newyork = round(newyork_response['main']['temp_min'])
max_temp_newyork = round(newyork_response['main']['temp_max'])

"""
Jakarta
"""

jakarta = 'Jakarta'
        
url_jakarta = (f'{BASE_URL}appid={API_KEY}&q={jakarta}&units={PARAMS}&lang={LANG}')
jakarta_response = requests.get(url_jakarta).json()

temp_jakarta = round(jakarta_response['main']['temp'])
min_temp_jakarta = round(jakarta_response['main']['temp_min'])
max_temp_jakarta = round(jakarta_response['main']['temp_max'])

"""
Shangai
"""

shangai = 'Shangai'
        
url_shangai = (f'{BASE_URL}appid={API_KEY}&q={shangai}&units={PARAMS}&lang={LANG}')
shangai_response = requests.get(url_shangai).json()

temp_shangai = round(shangai_response['main']['temp'])
min_temp_shangai = round(shangai_response['main']['temp_min'])
max_temp_shangai = round(shangai_response['main']['temp_max'])