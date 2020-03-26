from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '</br>'.join(['Человечество вырастает из детства.',
                         'Человечеству мала одна планета.',
                         'Мы сделаем обитаемыми безжизненные пока планеты.',
                         'И начнем с Марса!',
                         'Присоединяйся!'])


@app.route('/image_mars')
def image_mars():
    return '''<h1>Жди нас, Марс!</h1>
    <img src="{}" alt="здесь должна была быть картинка, но не нашлась">
        <p>Вот она какая, красная планета.</p>'''.format(url_for('static', filename='mars.jpg'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
