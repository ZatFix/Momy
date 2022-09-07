
from pyowm import OWM
from pyowm.utils.config import get_default_config

owm =   OWM('23232775d430e5fe2ac9a9c2cbdb8410')
language = get_default_config()
language['language'] = 'ru'
manager = owm.weather_manager()
observation = manager.weather_at_place('Жуковка')
weather = observation.weather
print('Сейчас', weather.detailed_status)
print("Облачность составляет", weather.clouds, "%")
temperature = owm
print("Температура:",weather.temperature('celsius').get('temp'))
print("Максимальная температура:",weather.temperature('celsius').get('temp_max'))
print("Минимальная температура:",weather.temperature('celsius').get('temp_min'))
print("Количество осадков:",weather.rain)
print("Ветер:",weather.wind())
one_call = manager.one_call(lat=53.858353, lon=27.311590)
print(one_call.forecast_daily[0].temperature('celsius'))
today = one_call.forecast_daily[0]
print(today.temperature("celsius").get("morn"))
print(today.temperature("celsius").get("day"))
print(today.temperature("celsius").get("eve"))
print(today.temperature("celsius").get("night"))
print(today.temperature("celsius").get("max"))
print(today.temperature("celsius").get("min"))
for i in range(7):
    today = one_call.forecast_daily[i]
    print("В этот день будет",today.detailed_status+ ",", "температура воздуха днём", today.temperature("celsius").get("day"))