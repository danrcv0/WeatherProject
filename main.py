from flask import Flask
from flask import Flask, request, render_template, redirect
from functions import *


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


            first = [state, f'{int(temp)}℃', f'давление - {pressure}',
                     f'влажность - {humidity}%', f'скорость ветра - {wind}м/c']
            return render_template('main.html', city=city, condition=conditions[state], first=first, tip=f'{get_tip(temp, state, humidity, wind)}😇')
        except:
            first = ['', '', '', '', '']
            return render_template('main.html', city='Вы уверены, что указали город верно?', condition=conditions['пасмурно'], first=first, tip='')

    state, temp, pressure, humidity, wind = get_weather(city="Ростов-на-Дону")
    first = [state, f'{int(temp)}℃', f'давление - {pressure}',
             f'влажность - {humidity}%', f'скорость ветра - {wind}м/c']
   
    return render_template('main.html', city="Ростов-на-Дону",  condition=conditions[state], first=first, tip=f'{get_tip(temp, state, humidity, wind)}😇')


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
