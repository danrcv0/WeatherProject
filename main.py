from flask import Flask
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from functions import *
from g4f.client import Client


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()


@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        city = request.form["City"]

        try:
            state, temp, pressure, humidity, wind = get_weather(city=city)

            print(tip)

            first = [state, f'{int(temp)}℃', f'давление - {pressure}',
                     f'влажность - {humidity}%', f'скорость ветра - {wind}м/c']
            return render_template('main.html', city=city, condition=conditions[state], first=first, tip=f'{get_tip(temp, state, humidity, wind)}😇')
        except:
            first = ['', '', '', '', '']
            return render_template('main.html', city='Вы уверены, что указали город верно?', condition=conditions['пасмурно'], first=first, tip='')

    state, temp, pressure, humidity, wind = get_weather(city="Ростов-на-Дону")
    first = [state, f'{int(temp)}℃', f'давление - {pressure}',
             f'влажность - {humidity}%', f'скорость ветра - {wind}м/c']
    info = ['Росто́в-на-Дону́ (сокращённо часто — Ростов) — крупнейший город на юго-западе России, административный центр Южного федерального округа и Ростовской области.',
            'Город воинской славы (2008).', 'Основан в 1749 году.', 'Население 1 140 487 человек (2024)', 'Климат Ростова-на-Дону умеренно континентальный.', 'Часовой пояс	UTC+3:00']
    return render_template('main.html', city="Ростов-на-Дону",  condition=conditions[state], first=first, tip=f'{get_tip(temp, state, humidity, wind)}😇', info=info)


@app.route("/API/<city>")
def Delete(city):
    try:
        state, temp, pressure, humidity, wind = get_weather(city=city)
        result = {
            "Город": city,
            "состояние": state,
            "температура": temp,
            "давление": pressure,
            "влажность": humidity,
            "скорость ветера": wind,
            "рекомендация": tip
        }
        return render_template('API.html', result=result)
    except:
        return render_template('API.html', result={"Город:'Вы уверены, что указали город верно?'"})


if __name__ == "__main__":
    app.run()
