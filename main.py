import sqlite3

from flask import Flask, render_template, request
from werkzeug.utils import redirect

from data import db_session
from data.users import User


from werkzeug.utils import redirect
import matplotlib.pyplot as plt

from data import db_session
from flask import Flask, render_template, redirect
from data.users import User
from data.results_dog import Results_Dog
from data.results_drink import Results_Drink
from data.results import Results
from data.reqq import Requests
from data.resources import ResultsResource, Results_DogListResource, Results_DrinkListResource
from forms.user import RegisterForm, LoginForm, RequestsForm
from flask_login import LoginManager, logout_user, login_required
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'test_project'
login_manager = LoginManager()
login_manager.init_app(app)

if_auto = False
user_name = ''
user_email = ''
searching = ''
result = ''

user_id = 0

titles = ["тест 'какая/ой ты собака?'", "тест 'какой/ая ты напиток?'", "тест 'какая/ой ты кошка/кот?'",
          "тест 'какая/ой ты шиншилла?'"]

dog = {
    'бульдог': ['Сангвинник', 'Ассам', 'Кино', 'Силы', 'Желтый'],
    'пудель': ['Флегматик', 'Улун', 'Рисование', 'Богатство', 'Синий'],
    'гончая': ['Холерик', 'Фруктовый', 'Спорт', 'Бессмертие', 'Красный'],
    'бобтейл': ['Меланхолик', 'Нет', 'Книги', 'Любовь', 'Зеленый']
}

dog_inv = {
    '1': ['Сангвинник', 'Флегматик', 'Холерик', 'Меланхолик'],
    '2': ['Улун', 'Ассам', 'Фруктовый', 'Нет'],
    '3': ['Кино', 'Рисование', 'Спорт', 'Книги'],
    '4': ['Силы', 'Богатство', 'Любовь', 'Бессмертие'],
    '5': ['Желтый', 'Синий', 'Красный', 'Зеленый']
}

dog_results = {
    'бульдог': 0,
    'пудель': 0,
    'гончая': 0,
    'бобтейл': 0
}

drink = {
    'кофе': ['Волнение', 'Дождь', 'Осень', 'Детектив', 'Заранее'],
    'сок': ['Жизнерадостный', 'Солнце', 'Лето', 'Роман', 'Ничего'],
    'молочный коктейль': ['Мечтательный', 'Снег', 'Зима', 'Фэнтези', 'Когда как'],
    'чай': ['Задумчивый', 'Облачно', 'Весна', 'Фантастика', 'Прокрастинирую']
}

drink_inv = {
    '1': ['Волнение', 'Жизнерадостный', 'Мечтательный', 'Задумчивый'],
    '2': ['Дождь', 'Солнце', 'Снег', 'Облачно'],
    '3': ['Осень', 'Лето', 'Зима', 'Весна'],
    '4': ['Детектив', 'Роман', 'Фэнтези', 'Фантастика'],
    '5': ['Заранее', 'Ничего', 'Умею', 'Прокрастинирую']
}

drink_results = {
    'кофе': 0,
    'сок': 0,
    'молочный коктейль': 0,
    'чай': 0
}

last_drink = ''
dog_ins = [0, 0, 0, 0, 0]
dog_spisok = []

last_temp = ''
last_temp_num = ''

last_tea = ''
last_tea_num = ''

last_hobbie = ''
last_hobbie_num = ''

last_power = ''
last_power_num = ''

last_man = ''
last_man_num = ''

last_drink = ''
drink_ins = [0, 0, 0, 0, 0]
drink_spisok = []

last_char = ''
last_char_num = ''

last_wea = ''
last_wea_num = ''

last_time = ''
last_time_num = ''

last_genre = ''
last_genre_num = ''

last_color = ''
last_color_num = ''


@app.route("/")
def index():
    global if_auto, user_name, searching

    if not if_auto:
        return render_template("log_index.html", if_auto=if_auto, user=user_name)
    else:
        return render_template("log_index.html", if_auto=if_auto, user=user_name)


@app.route("/search", methods=['GET', 'POST'])
def search():
    global if_auto, user_name, titles, searching

    searching = request.args['title'].lower().split()

    ready = []

    for title in titles:
        for i in searching:
            count = 0
            if i in title:
                count += 1
        if count == len(i.split()):
            ready.append(title)

    if not if_auto:
        return render_template("search_index.html", titles=titles, request=ready, if_auto=if_auto, user=user_name)

    else:
        return render_template("search_index.html", if_auto=if_auto, user=user_name, titles=titles, request=searching)


@app.route("/auto", methods=['GET', 'POST'])
def auto():
    return render_template('auto.html', title='Авторизация')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/dog_test_1", methods=['POST', 'GET'])
def dog_1():
    global dog_spisok, dog, dog_results, result, last_temp, dog_ins, last_temp, last_temp_num
    if request.method == 'POST':

        result = request.form.get('temperament')

        for key in dog:
            if dog[key][0] == result:
                dog_ins[0] += 1
                if dog_ins[0] > 1:
                    dog_spisok.remove(last_temp)
                    dog_results[last_temp_num] -= 1
                dog_results[key] += 1
                last_temp_num = key
                dog_spisok.append(result)
                last_temp = result
        return redirect("/dog_test_2")
    else:

        return render_template("dog_test_1.html", head='Какая вы собака?', if_auto=if_auto, user=user_name,
                               result=result,
                               title='Какой у вас темперамент?', first='Холерик',
                               second='Флегматик', third='Сангвинник', fourth='Меланхолик', source='/dog_test_1',
                               id_1='Holeric', id_2='Flegmatic', id_3='Sangvinnic', id_4='Melanholic',
                               value_1='Холерик',
                               value_2='Флегматик', value_3='Сангвинник', value_4='Меланхолик', name='temperament',
                               spisok=dog_spisok, message='Дальше', progress='0%', count=dog_ins,
                               picture='static/img/dog_1.jpg')


@app.route("/dog_test_2", methods=['POST', 'GET'])
def dog_2():
    global dog_spisok, dog, dog_results, result, dog_ins, last_tea, last_tea_num

    if request.method == 'POST':

        result = request.form.get('tea')

        for key in dog:
            if dog[key][1] == result:
                dog_ins[1] += 1
                if dog_ins[1] > 1:
                    dog_spisok.remove(last_tea)
                    dog_results[last_tea_num] -= 1
                dog_results[key] += 1
                last_tea_num = key
                dog_spisok.append(result)
                last_tea = result
        return redirect("/dog_test_3")
    else:

        return render_template("dog_test_1.html", head='Какая вы собака?', if_auto=if_auto, user=user_name,
                               result=result,
                               title='Ваш любимый чай?', first='Я не пью чай',
                               second='Черный чай Ассам', third='Зеленый чай Молочный Улун',
                               fourth='Черный фруктовый чай', source='/dog_test_2',
                               id_1='Not', id_2='Assam', id_3='Ulun', id_4='Fruit',
                               value_1='Нет',
                               value_2='Ассам', value_3='Улун', value_4='Фруктовый', name='tea', spisok=dog_spisok,
                               message='Дальше', progress='20%', count=dog_ins, picture='static/img/dog_2.jpg')


@app.route("/dog_test_3", methods=['POST', 'GET'])
def dog_3():
    global dog_spisok, dog, dog_results, result, dog_ins, last_hobbie, last_hobbie_num

    if request.method == 'POST':

        result = request.form.get('hobbie')

        for key in dog:
            if dog[key][2] == result:
                dog_ins[2] += 1
                if dog_ins[2] > 1:
                    dog_spisok.remove(last_hobbie)
                    dog_results[last_hobbie_num] -= 1
                dog_results[key] += 1
                last_hobbie_num = key
                dog_spisok.append(result)
                last_hobbie = result
        return redirect("/dog_test_4")
    else:

        return render_template("dog_test_1.html", head='Какая вы собака?', if_auto=if_auto, user=user_name,
                               result=result,
                               title='Чем вы предпочли бы заняться?', first='Просмотром фильма или сериала',
                               second='Рисованием', third='Чтением книги', fourth='Спортом', source='/dog_test_3',
                               id_1='Film', id_2='Draw', id_3='Book', id_4='Sport',
                               value_1='Кино',
                               value_2='Рисование', value_3='Книги', value_4='Спорт', name='hobbie', spisok=dog_spisok,
                               message='Дальше', progress='40%', count=dog_ins, picture='static/img/dog_3.jpeg')


@app.route("/dog_test_4", methods=['POST', 'GET'])
def dog_4():
    global dog_spisok, dog, dog_results, result, dog_ins, last_power, last_power_num

    if request.method == 'POST':

        result = request.form.get('wish')

        for key in dog:
            if dog[key][3] == result:
                dog_ins[3] += 1
                if dog_ins[3] > 1:
                    dog_spisok.remove(last_power)
                    dog_results[last_power_num] -= 1
                dog_results[key] += 1
                last_power_num = key
                dog_spisok.append(result)
                last_power = result

        return redirect("/dog_test_5")
    else:

        return render_template("dog_test_1.html", head='Какая вы собака?', if_auto=if_auto, user=user_name,
                               result=result,
                               title='Что бы вы выбрали?', first='Богатство',
                               second='Любовь', third='Сверхъестественные силы', fourth='Бессмертие',
                               source='/dog_test_4',
                               id_1='Money', id_2='Love', id_3='Powers', id_4='Deathless',
                               value_1='Богатство',
                               value_2='Любовь', value_3='Силы', value_4='Бессмертие', name='wish', spisok=dog_spisok,
                               message='Дальше', progress='60%', count=dog_ins, picture='static/img/dog_4.webp')


@app.route("/dog_test_5", methods=['POST', 'GET'])
def dog_5():
    global dog_spisok, dog, dog_results, result, dog_ins, last_color, last_color_num

    if request.method == 'POST':

        result = request.form.get('color')

        for key in dog:
            if dog[key][4] == result:
                dog_ins[4] += 1
                if dog_ins[4] > 1:
                    dog_spisok.remove(last_color)
                    dog_results[last_color_num] -= 1
                dog_results[key] += 1
                last_color_num = key
                dog_spisok.append(result)
                last_color = result

        return redirect("/dog_results")
    else:

        return render_template("dog_test_1.html", head='Какая вы собака?', if_auto=if_auto, user=user_name,
                               result=result,
                               title='Ваш любимый цвет?', first='Синий',
                               second='Желтый', third='Зеленый', fourth='Красный', source='/dog_test_5',
                               id_1='Blue', id_2='Yellow', id_3='Green', id_4='Red',
                               value_1='Синий',
                               value_2='Желтый', value_3='Зеленый', value_4='Красный', name='color', spisok=dog_spisok,
                               message='Завершить', progress='80%', count=dog_ins, picture='static/img/dog_5.jfif')


@app.route("/dog_results", )
def result_dog():
    global dog_spisok, dog, dog_results, result, user_id, dog_inv

    maximum = 0
    for key in dog_results:
        if dog_results[key] > maximum:
            maximum = dog_results[key]
            result = key

    new_spisok = []
    for key in dog_inv:
        for item in dog_spisok:
            if item in dog_inv[key] and item not in new_spisok:
                new_spisok.append(item)

    db_sess = db_session.create_session()
    res = Results_Dog(
        dog_1=dog_spisok[0],
        dog_2=dog_spisok[1],
        dog_3=dog_spisok[2],
        dog_4=dog_spisok[3],
        dog_5=dog_spisok[4],
        user_id=user_id
    )
    db_sess.add(res)
    db_sess.commit()

    db_sess = db_session.create_session()
    ress = Results(
        dog=result,
        user_id=user_id
    )
    db_sess.add(ress)
    db_sess.commit()

    return render_template("result_dog.html", title=result, spis=dog_spisok)


@app.route("/drink_test_1", methods=['POST', 'GET'])
def drink_1():
    global drink_spisok, drink, drink_results, result, last_char, drink_ins, last_char_num
    if request.method == 'POST':

        result = request.form.get('character')

        for key in drink:
            if drink[key][0] == result:
                drink_ins[0] += 1
                if drink_ins[0] > 1:
                    drink_spisok.remove(last_char)
                    drink_results[last_char_num] -= 1
                drink_results[key] += 1
                last_char_num = key
                drink_spisok.append(result)
                last_char = result
        return redirect("/drink_test_2")
    else:

        return render_template("dog_test_1.html", head='Какой вы напиток?', if_auto=if_auto, user=user_name,
                               result=result,
                               title='Как бы вы охарактеризовали себя?', first='Я жизнерадостный человек',
                               second='Я задумчивый человек', third='Я мечтательный человек',
                               fourth='Я много волнуюсь о различных вещах', source='/drink_test_1',
                               id_1='Happy', id_2='Think', id_3='Dream', id_4='Care',
                               value_1='Жизнерадостный',
                               value_2='Задумчивый', value_3='Мечтательный', value_4='Волнение', name='character',
                               spisok=drink_spisok, message='Дальше', progress='0%', count=drink_ins,
                               picture='static/img/drink_1.jpg')


@app.route("/drink_test_2", methods=['POST', 'GET'])
def drink_2():
    global drink_spisok, drink, drink_results, result, drink_ins, last_wea, last_wea_num

    if request.method == 'POST':

        result = request.form.get('weather')

        for key in drink:
            if drink[key][1] == result:
                drink_ins[1] += 1
                if drink_ins[1] > 1:
                    drink_spisok.remove(last_wea)
                    drink_results[last_wea_num] -= 1
                drink_results[key] += 1
                last_wea_num = key
                drink_spisok.append(result)
                last_wea = result
        return redirect("/drink_test_3")
    else:

        return render_template("dog_test_1.html", head='Какой вы напиток?', if_auto=if_auto, user=user_name,
                               result=result,
                               title='Ваша любимая погода?', first='Дождливая',
                               second='Солнечная', third='Облачная',
                               fourth='Снежная', source='/drink_test_2',
                               id_1='Rainy', id_2='Sunny', id_3='Cloudy', id_4='Snow',
                               value_1='Дождь',
                               value_2='Солнце', value_3='Облачно', value_4='Снег', name='weather', spisok=drink_spisok,
                               message='Дальше', progress='20%', count=drink_ins, picture='static/img/drink_2.jpg')


@app.route("/drink_test_3", methods=['POST', 'GET'])
def drink_3():
    global drink_spisok, drink, drink_results, result, drink_ins, last_time, last_time_num

    if request.method == 'POST':

        result = request.form.get('time')

        for key in drink:
            if drink[key][2] == result:
                drink_ins[2] += 1
                if drink_ins[2] > 1:
                    drink_spisok.remove(last_time)
                    drink_results[last_time_num] -= 1
                drink_results[key] += 1
                last_time_num = key
                drink_spisok.append(result)
                last_time = result
        return redirect("/drink_test_4")
    else:

        return render_template("dog_test_1.html", head='Какой вы напиток?', if_auto=if_auto, user=user_name,
                               result=result,
                               title='Ваше любимое время года?', first='Зима',
                               second='Лето', third='Осень', fourth='Весна', source='/drink_test_3',
                               id_1='Winter', id_2='Summer', id_3='Autumn', id_4='Spring',
                               value_1='Зима',
                               value_2='Лето', value_3='Осень', value_4='Весна', name='time', spisok=drink_spisok,
                               message='Дальше', progress='40%', count=drink_ins, picture='static/img/drink_3.jpg')


@app.route("/drink_test_4", methods=['POST', 'GET'])
def drink_4():
    global drink_spisok, drink, drink_results, result, drink_ins, last_genre, last_genre_num

    if request.method == 'POST':

        result = request.form.get('genre')

        for key in drink:
            if drink[key][3] == result:
                drink_ins[3] += 1
                if drink_ins[3] > 1:
                    drink_spisok.remove(last_genre)
                    drink_results[last_genre_num] -= 1
                drink_results[key] += 1
                last_genre_num = key
                drink_spisok.append(result)
                last_genre = result

        return redirect("/drink_test_5")
    else:

        return render_template("dog_test_1.html", head='Какой вы напиток?', if_auto=if_auto, user=user_name,
                               result=result,
                               title='Какой жанр книг вы бы предпочли?', first='Детектив',
                               second='Фантастика', third='Роман', fourth='Фэнтези',
                               source='/drink_test_4',
                               id_1='Детектив', id_2='Fantastic', id_3='Roman', id_4='Fantasy',
                               value_1='Богатство',
                               value_2='Фантастика', value_3='Роман', value_4='Фэнтези', name='genre',
                               spisok=drink_spisok,
                               message='Дальше', progress='60%', count=drink_ins, picture='static/img/drink_4.jpg')


@app.route("/drink_test_5", methods=['POST', 'GET'])
def drink_5():
    global drink_spisok, drink, drink_results, result, drink_ins, last_man, last_man_num

    if request.method == 'POST':

        result = request.form.get('manage')

        for key in drink:
            if drink[key][4] == result:
                drink_ins[4] += 1
                if drink_ins[4] > 1:
                    drink_spisok.remove(last_man)
                    drink_results[last_man_num] -= 1
                drink_results[key] += 1
                last_man_num = key
                drink_spisok.append(result)
                last_man = result

        return redirect("/drink_results")
    else:

        return render_template("dog_test_1.html", head='Какой вы напиток?', if_auto=if_auto, user=user_name,
                               result=result,
                               title='Насколько вы организованны?', first='Я умею распределять свое время',
                               second='Я часто прокрастинирую и откладываю на потом', third='Я делаю все заранее',
                               fourth='Я часто ленюсь и ничего не делаю', source='/drink_test_5',
                               id_1='Blue', id_2='Yellow', id_3='Green', id_4='Red',
                               value_1='Умею',
                               value_2='Прокрастинирую', value_3='Заранее', value_4='Ничего', name='manage',
                               spisok=drink_spisok,
                               message='Завершить', progress='80%', count=drink_ins, picture='static/img/drink_5.webp')


@app.route("/drink_results", )
def result_drink():
    global drink_spisok, drink, drink_results, result, user_id, drink_inv

    maximum = 0
    for key in drink_results:
        if drink_results[key] > maximum:
            maximum = drink_results[key]
            result = key

    new_spisok = []
    for key in drink_inv:
        for item in drink_spisok:
            if item in drink_inv[key] and item not in new_spisok:
                new_spisok.append(item)

    db_sess = db_session.create_session()
    res = Results_Drink(
        drink_1=drink_spisok[0],
        drink_2=drink_spisok[1],
        drink_3=drink_spisok[2],
        drink_4=drink_spisok[3],
        drink_5=drink_spisok[4],
        user_id=user_id
    )
    db_sess.add(res)
    db_sess.commit()

    db_sess = db_session.create_session()
    ress = Results(
        drink=result,
        user_id=user_id
    )
    db_sess.add(ress)
    db_sess.commit()

    return render_template("result_dog.html", head='Какой вы напиток?', title=result, spis=drink_spisok)


@app.route('/register', methods=['GET', 'POST'])
def register():
    global if_auto, user_name, user_email, user_id

    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        if_auto = True
        user_name = user.name
        user_email = user.email
        user_id = user.id
        return redirect("/")
    return render_template('register.html', title='Регистрация', form=form, if_auto=if_auto, user=user_name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global if_auto, user_name, user_email, user_id

    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            if_auto = True
            user_name = user.name
            user_email = user.email
            user_id = user.id
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль. Возможно, требуется регистрация",
                               form=form)

    return render_template('login.html', title='Авторизация', form=form, if_auto=if_auto, user=user_name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/personal')
def person():
    form = RequestsForm()
    return render_template("personal.html", user=user_name, if_auto=if_auto, email=user_email, form=form)


def main_dog_diagram():
    con = sqlite3.connect("db/tests.db")
    cur = con.cursor()
    result_dog1 = cur.execute("""SELECT dog FROM results
                        WHERE dog = ?""", ("бульдог",)).fetchall()
    result_dog2 = cur.execute("""SELECT dog FROM results
                WHERE dog = ?""", ("пудель",)).fetchall()
    result_dog3 = cur.execute("""SELECT dog FROM results
                    WHERE dog = ?""", ("гончая",)).fetchall()
    result_dog4 = cur.execute("""SELECT dog FROM results
                    WHERE dog = ?""", ("бобтейл",)).fetchall()
    vals = [len(result_dog1), len(result_dog2), len(result_dog3), len(result_dog4)]
    idx_remove = []
    for el in vals:
        if el == 0:
            idx_remove.append(vals.index(el))
            vals.remove(el)
    labels = ["бульдог", "пудель", "гончая", "бобтейл"]
    if idx_remove:
        for el in idx_remove:
            labels.remove(labels[el])
    fig, ax = plt.subplots()
    ax.pie(vals, labels=labels, autopct='%1.1f%%')
    ax.axis("equal")
    plt.savefig('static/main_dog_diagram.png')


def info_dog_diagram1():
    con = sqlite3.connect("db/tests.db")
    cur = con.cursor()
    values_dog1 = {'Сангвинник': 0,
                   'Флегматик': 0,
                   'Холерик': 0,
                   'Меланхолик': 0}
    result_dog1 = cur.execute("""SELECT dog_1 FROM Results_dog""").fetchall()
    for el in result_dog1:
        values_dog1[el[0]] += 1
    vals1 = [values_dog1['Сангвинник'], values_dog1['Флегматик'], values_dog1['Холерик'], values_dog1['Меланхолик']]
    idx_remove1 = []
    for el in vals1:
        if el == 0:
            idx_remove1.append(vals1.index(el))
            vals1.remove(el)
    labels1 = ["Сангвинник", "Флегматик", "Холерик", "Меланхолик"]
    if idx_remove1:
        for el in idx_remove1:
            labels1.remove(labels1[el])
    fig1, ax1 = plt.subplots()
    ax1.pie(vals1, labels=labels1, autopct='%1.1f%%')
    ax1.axis("equal")
    plt.savefig('static/info_dog_diagram1.png')


def info_dog_diagram2():
    con = sqlite3.connect("db/tests.db")
    cur = con.cursor()
    values_dog2 = {'Улун': 0,
                   'Ассам': 0,
                   'Фруктовый': 0,
                   'Нет': 0}
    result_dog2 = cur.execute("""SELECT dog_2 FROM Results_dog""").fetchall()
    for el in result_dog2:
        values_dog2[el[0]] += 1
    vals2 = [values_dog2['Улун'], values_dog2['Ассам'], values_dog2['Фруктовый'], values_dog2['Нет']]
    idx_remove2 = []
    for el in vals2:
        if el == 0:
            idx_remove2.append(vals2.index(el))
            vals2.remove(el)
    labels2 = ["Улун", "Ассам", "Фруктовый", "Нет"]
    if idx_remove2:
        for el in idx_remove2:
            labels2.remove(labels2[el])
    fig2, ax2 = plt.subplots()
    ax2.pie(vals2, labels=labels2, autopct='%1.1f%%')
    ax2.axis("equal")
    plt.savefig('static/info_dog_diagram2.png')


def info_dog_diagram3():
    con = sqlite3.connect("db/tests.db")
    cur = con.cursor()
    values_dog3 = {'Кино': 0,
                   'Рисование': 0,
                   'Спорт': 0,
                   'Книги': 0}
    result_dog3 = cur.execute("""SELECT dog_3 FROM Results_dog""").fetchall()
    for el in result_dog3:
        values_dog3[el[0]] += 1
    vals3 = [values_dog3['Кино'], values_dog3['Рисование'], values_dog3['Спорт'], values_dog3['Книги']]
    idx_remove3 = []
    for el in vals3:
        if el == 0:
            idx_remove3.append(vals3.index(el))
            vals3.remove(el)
    labels3 = ["Кино", "Рисование", "Спорт", "Книги"]
    if idx_remove3:
        for el in idx_remove3:
            labels3.remove(labels3[el])
    fig3, ax3 = plt.subplots()
    ax3.pie(vals3, labels=labels3, autopct='%1.1f%%')
    ax3.axis("equal")
    plt.savefig('static/info_dog_diagram3.png')


def info_dog_diagram4():
    con = sqlite3.connect("db/tests.db")
    cur = con.cursor()
    values_dog4 = {'Силы': 0,
                   'Богатство': 0,
                   'Любовь': 0,
                   'Бессмертие': 0}
    result_dog4 = cur.execute("""SELECT dog_4 FROM Results_dog""").fetchall()
    for el in result_dog4:
        values_dog4[el[0]] += 1
    vals4 = [values_dog4['Силы'], values_dog4['Богатство'], values_dog4['Любовь'], values_dog4['Бессмертие']]
    idx_remove4 = []
    for el in vals4:
        if el == 0:
            idx_remove4.append(vals4.index(el))
            vals4.remove(el)
    labels4 = ["Силы", "Богатство", "Любовь", "Бессмертие"]
    if idx_remove4:
        for el in idx_remove4:
            labels4.remove(labels4[el])
    fig4, ax4 = plt.subplots()
    ax4.pie(vals4, labels=labels4, autopct='%1.1f%%')
    ax4.axis("equal")
    plt.savefig('static/info_dog_diagram4.png')


def info_dog_diagram5():
    con = sqlite3.connect("db/tests.db")
    cur = con.cursor()
    values_dog5 = {'Желтый': 0,
                   'Синий': 0,
                   'Красный': 0,
                   'Зеленый': 0}
    result_dog5 = cur.execute("""SELECT dog_5 FROM Results_dog""").fetchall()
    for el in result_dog5:
        values_dog5[el[0]] += 1
    vals5 = [values_dog5['Желтый'], values_dog5['Синий'], values_dog5['Красный'], values_dog5['Зеленый']]
    idx_remove5 = []
    for el in vals5:
        if el == 0:
            idx_remove5.append(vals5.index(el))
            vals5.remove(el)
    labels5 = ["Желтый", "Синий", "Красный", "Зеленый"]
    if idx_remove5:
        for el in idx_remove5:
            labels5.remove(labels5[el])
    fig5, ax5 = plt.subplots()
    ax5.pie(vals5, labels=labels5, autopct='%1.1f%%')
    ax5.axis("equal")
    plt.savefig('static/info_dog_diagram5.png')


@app.route('/statistics', methods=['GET', 'POST'])
def statistics():
    if if_auto:
        main_dog_diagram()
        return render_template('diagram.html')
    else:
        return render_template('diagram_error.html')


@app.route('/dog_more_info', methods=['GET', 'POST'])
def dog_more_info():
    info_dog_diagram1()
    info_dog_diagram2()
    info_dog_diagram3()
    info_dog_diagram4()
    info_dog_diagram5()
    return render_template('info_dog_diagram.html')


def main():
    db_session.global_init("db/tests.db")
    api.add_resource(Results_DogListResource, '/api/v2/results_dog')
    api.add_resource(Results_DrinkListResource, '/api/v2/results_drink')
    #
    # api.add_resource(Results_DrinkListResource, '/api/v2/results_cat')
    # api.add_resource(Results_DrinkListResource, '/api/v2/results_chinchilla')

    # для одного объекта
    api.add_resource(ResultsResource, '/api/v2/results/<int:results_id>')
    app.run(port=8080)


if __name__ == '__main__':
    db_session.global_init("db/tests.db")
    api.add_resource(Results_DogListResource, '/api/v2/results_dog')
    api.add_resource(Results_DrinkListResource, '/api/v2/results_drink')
    #
    # api.add_resource(Results_DrinkListResource, '/api/v2/results_cat')
    # api.add_resource(Results_DrinkListResource, '/api/v2/results_chinchilla')

    # для одного объекта
    api.add_resource(ResultsResource, '/api/v2/results/<int:results_id>')
    app.run(port=8080)


