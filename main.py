from flask import Flask
from flask import url_for, request

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
