import requests
from translate import Translator


conditions = {
    'небольшая облачность': 'https://catherineasquithgallery.com/uploads/posts/2021-02/1612766963_99-p-fon-goluboe-nebo-s-oblakami-dlya-prezentat-112.jpg',
    'ясно': 'https://klike.net/uploads/posts/2023-02/1675232131_3-2.jpg',
    'пасмурно': 'https://grizly.club/uploads/posts/2023-01/1673056293_grizly-club-p-tekstura-pasmurnogo-neba-21.jpg',
    'плотный туман': 'https://www.sunhome.ru/i/foto/55/tuman-v5.orig.jpg',
    'переменная облачность': 'https://cs9.pikabu.ru/post_img/2017/06/28/11/og_og_149867949222613491.jpg',
    'небольшой дождь': 'https://www.fonstola.ru/images/201111/fonstola.ru_52367.jpg',
    'облачно с прояснениями': 'https://zp-news.ru/img/20231113/cb7d6bef8ab831669b9da6c879d7893e.jpg',
    'мгла': 'https://get.pxhere.com/photo/tree-snow-winter-black-and-white-fog-mist-morning-frost-dawn-atmosphere-weather-haze-monochrome-season-trees-blizzard-freezing-monochrome-photography-atmospheric-phenomenon-winter-storm-282562.jpg',
    'туман': 'https://gas-kvas.com/grafic/uploads/posts/2023-10/1696529473_gas-kvas-com-p-kartinki-tuman-7.jpg'
}


translator = Translator(from_lang="russian", to_lang="english")
API_key = "4ff8a60a7df18b3681fb71cd130349ac"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def get_weather(city):
    final_url = base_url + "appid=" + API_key + \
        "&q=" + translator.translate(city) + "&lang=ru"
    weather_data = requests.get(final_url).json()
    state = weather_data['weather'][0]['description']
    temp = weather_data['main']['temp'] - 273.15
    pressure = weather_data['main']['pressure']
    humidity = weather_data['main']['humidity']
    wind = weather_data['wind']['speed']
    return state, temp, pressure, humidity, wind


def get_tip(temp, state, humidity, wind):
    msg_temp, msg_state, msg_wind, msg_hum = '', '', '', ''
    if temp >= 20:
        msg_temp = 'Наденьте лёгкую одежду'
    elif 20 > temp > 10:
        msg_temp = 'Возьмите с собой кофту или легкую куртку'
    elif temp <= 10:
        msg_temp = 'Наденьте тёплую одежду, куртку'

    if state == 'ясно':
        msg_state = ', возьмите кепку,'
    elif state == 'пасмурно' or 'дождь' in state:
        msg_state = ', возьмите зонт,'

    if wind >= 10:
        msg_wind = ' не забудьте ветровку'

    if humidity <= 30:
        msg_hum = ' и не забудьте бутылку воды'

    msg = msg_temp + msg_state + msg_wind + msg_hum
    return msg
