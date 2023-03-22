from decouple import config

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

API_KEY = config('API_KEY')

PARAMS = 'metric'
LANG = 'es'