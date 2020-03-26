from flask import Flask
from flask import url_for, request
import os

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
        <p>Вот она какая, красная планета.</p>'''.format(url_for('static', filename='img/mars.jpg'))


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css"
                    href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img width="200" height="200" src="{url_for('static', filename='img/mars.jpg')}"
                    alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-primary" role="alert">
                      Мы сделаем обитаемыми безжиненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                                integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static',
                                                                                      filename='css/style.css')}" />
                                <title>Отбор астронавтов</title>
                              </head>
                              <body>
                                <h2 align="center">Анкета претендента</h2>
                                <h3 align="center">на участие в миссии</h3>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="second_name" class="form-control" id="second_name" placeholder="Введите фамилию" name="second_name">
                                        <input type="first_name" class="form-control" id="first_name" placeholder="Введите имя" name="first_name">
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у вас образование?</label>
                                            <select class="form-control" id="classSelect" name="education">
                                                <option>Начальное (1-4 класс)</option>
                                                <option>Основное (5-9 класс)</option>
                                                <option>Среднее (10-11 класс)</option>
                                                <option>Начальное (ПТУ, профессиональный лицей)</option>
                                                <option>Среднее (техникум, колледж)</option>
                                                <option>Бакалавриат (I-IV курс вуза)</option>
                                                <option>Специалитет (V курс)</option>
                                                <option>Магистратура (V курс)</option>
                                                <option>Аспирантура</option>
                                                <option>Докторантур</option>
                                            </select>
                                        </div>
                                        <div class="form-group">
                                            <label for="form-check">Кем Вы хотите работать?</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="work" value="Инженер-исследователь">
                                              <label class="form-check-label" for="Инженер-исследователь">
                                                Инженер-исследователь
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="work" value="Пилот">
                                              <label class="form-check-label" for="Пилот">
                                                Пилот
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="work" value="Строитель">
                                              <label class="form-check-label" for="Строитель">
                                                Строитель
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="work" value="Экзобиолог">
                                              <label class="form-check-label" for="Экзобиолог">
                                                Экзобиолог
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="work" value="Врач">
                                              <label class="form-check-label" for="Врач">
                                                Врач
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="work" value="Инженер по терраформированию">
                                              <label class="form-check-label" for="Инженер по терраформированию">
                                                Инженер по терраформированию
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="work" value="Климатолог">
                                              <label class="form-check-label" for="Климатолог">
                                                Климатолог
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="work" value="Специалист по радиационной защите">
                                              <label class="form-check-label" for="Специалист по радиационной защите">
                                                Специалист по радиационной защите
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="work" value="Астрогеолог">
                                              <label class="form-check-label" for="Астрогеолог">
                                                Астрогеолог
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="work" value="Инженер жизнеобеспечения">
                                              <label class="form-check-label" for="Инженер жизнеобеспечения">
                                                Инженер жизнеобеспечения
                                              </label>
                                            </div>
                                         </div>
                                         <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Записаться</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['second_name'])
        print(request.form['first_name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['work'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def planet_name(planet_name):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css"
                        href="{url_for('static', filename='css/style.css')}" />
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        <p>Эта планета близка к Земле;</p>
                        <div class="alert alert-success" role="alert">
                          На ней много необходимых ресурсов;
                        </div>
                        <div class="alert alert-primary" role="alert">
                          На ней есть вода и атмосфера;
                        </div>
                        <div class="alert alert-warning" role="alert">
                          На ней есть небольшое магнитное поле;
                        </div>
                        <div class="alert alert-danger" role="alert">
                          Наконец, она просто красива!
                        </div>
                      </body>
                    </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css"
                            href="{url_for('static', filename='css/style.css')}" />
                            <title>Результаты</title>
                          </head>
                          <body>
                            <h1>Результаты отбора</h1>
                            <p>Претендента на участие в миссии {nickname}</p>
                            <div class="alert alert-success" role="alert">
                              Поздравляем! Ваш рейтинг после {level} этапа отбора
                            </div>
                            <p>составляет {rating}</p>
                            <div class="alert alert-warning" role="alert">
                              Желаем удачи!
                            </div>
                          </body>
                        </html>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                             integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static',
                                                                                  filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h2 align="center">Загрузка фотографии</h2>
                            <p align="center">для участия в миссии</p>
                            <form align="center" method="post" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Выберите файл</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                            <img src={url_for('static', filename='img/photo.png')}>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        with open('static/img/photo.png', 'wb') as file:
            file.write(f.read())
        return "Форма отправлена"


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css"
                        href="{url_for('static', filename='css/style.css')}" />
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1 align="center">Пейзажи Марса</h1>
                        <div align="center" id="carousel-example-generic" class="carousel slide" data-ride="carousel">
                          <ol class="carousel-indicators">
                            <li data-target="#carousel-example-generic" data-slide-to="1" class="active"></li>
                            <li data-target="#carousel-example-generic" data-slide-to="2"></li>
                            <li data-target="#carousel-example-generic" data-slide-to="0"></li>
                          </ol>
                          <div class="carousel-inner" role="listbox">
                            <div class="carousel-item active">
                              <img src="static\img\с1.jpg" alt="First slide">
                            </div>
                            <div class="carousel-item">
                              <img src="static\img\с2.jpg" alt="Second slide">
                            </div>
                            <div class="carousel-item">
                              <img src="static\img\с3.jpg" alt="Third slide">
                            </div>
                          </div>
                          <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">
                            <span class="icon-prev" aria-hidden="true"></span>
                            <span class="sr-only">Previous</span>
                          </a>
                          <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">
                            <span class="icon-next" aria-hidden="true"></span>
                            <span class="sr-only">Next</span>
                          </a>
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
