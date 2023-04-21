from flask_restful import Api
from werkzeug.utils import redirect
from data import db_session, constants
from flask import Flask, render_template, redirect, request
from data.diagrams.dog_diagrams import *
from data.diagrams.cat_diagrams import *
from data.diagrams.chin_diagrams import *
from data.diagrams.drink_diagrams import *
from data.users import User
from data.results.results_dog import Results_Dog
from data.results.results_drink import Results_Drink
from data.results.results_cat import Results_Cat
from data.results.results_chin import Results_Chin
from data.results.results import Results
from forms.user import RegisterForm, LoginForm, RequestsForm
from flask_login import LoginManager, logout_user, login_required
from data.resources import Results_DogListResource, Results_DrinkListResource, ResultsResource, Results_CatListResource, \
    Results_ChinchillaListResource


app = Flask(__name__)
api = Api(app)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SECRET_KEY'] = 'test_project'
login_manager = LoginManager()
login_manager.init_app(app)
con = sqlite3.connect("db/tests.db")
cur = con.cursor()


@app.route("/")
def index():
    if not constants.if_auto:
        return render_template("log_index.html", if_auto=constants.if_auto, user=constants.user_name)
    return render_template("log_index.html", if_auto=constants.if_auto, user=constants.user_name)


@app.route("/search", methods=['GET', 'POST'])
def search():
    constants.searching = request.args['title'].lower().split()

    ready = []

    for title in constants.titles:
        for i in constants.searching:
            count = 0
            if i in title:
                count += 1
        if count == len(i.split()):
            ready.append(title)

    if not constants.if_auto:
        return render_template("search_index.html", titles=constants.titles, request=ready, if_auto=constants.if_auto,
                               user=constants.user_name)
    return render_template("search_index.html", if_auto=constants.if_auto,
                           user=constants.user_name, titles=constants.titles, request=constants.searching)


@app.route("/auto", methods=['GET', 'POST'])
def auto():
    return render_template('auto.html', title='Авторизация')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/dog_test_1", methods=['POST', 'GET'])
def dog_1():
    if request.method == 'POST':

        constants.result = request.form.get('temperament')

        for key in constants.dog:
            if constants.dog[key][0] == constants.result:
                constants.dog_ins[0] += 1
                if constants.dog_ins[0] > 1:
                    constants.dog_spisok.remove(constants.last_temp)
                    constants.dog_results[constants.last_temp_num] -= 1
                constants.dog_results[key] += 1
                constants.last_temp_num = key
                constants.dog_spisok.append(constants.result)
                constants.last_temp = constants.result
        return redirect("/dog_test_2")
    return render_template("dog_test_1.html", head='Какая вы собака?', if_auto=constants.if_auto, user=constants.user_name,
                           result=constants.result,
                           title='Какой у вас темперамент?', first='Холерик',
                           second='Флегматик', third='Сангвинник', fourth='Меланхолик', source='/dog_test_1',
                           id_1='Holeric', id_2='Flegmatic', id_3='Sangvinnic', id_4='Melanholic',
                           value_1='Холерик',
                           value_2='Флегматик', value_3='Сангвинник', value_4='Меланхолик', name='temperament',
                           spisok=constants.dog_spisok, message='Дальше', progress='0%', count=constants.dog_ins,
                           picture='static/img/dog_1.jpg')


@app.route("/dog_test_2", methods=['POST', 'GET'])
def dog_2():
    if request.method == 'POST':

        constants.result = request.form.get('tea')

        for key in constants.dog:
            if constants.dog[key][1] == constants.result:
                constants.dog_ins[1] += 1
                if constants.dog_ins[1] > 1:
                    constants.dog_spisok.remove(constants.last_tea)
                    constants.dog_results[constants.last_tea_num] -= 1
                constants.dog_results[key] += 1
                constants.last_tea_num = key
                constants.dog_spisok.append(constants.result)
                constants.last_tea = constants.result
        return redirect("/dog_test_3")
    return render_template("dog_test_1.html", head='Какая вы собака?', if_auto=constants.if_auto, user=constants.user_name,
                           result=constants.result,
                           title='Ваш любимый чай?', first='Я не пью чай',
                           second='Черный чай Ассам', third='Зеленый чай Молочный Улун',
                           fourth='Черный фруктовый чай', source='/dog_test_2',
                           id_1='Not', id_2='Assam', id_3='Ulun', id_4='Fruit',
                           value_1='Нет',
                           value_2='Ассам', value_3='Улун', value_4='Фруктовый', name='tea', spisok=constants.dog_spisok,
                           message='Дальше', progress='20%', count=constants.dog_ins, picture='static/img/dog_2.jpg')


@app.route("/dog_test_3", methods=['POST', 'GET'])
def dog_3():
    if request.method == 'POST':

        constants.result = request.form.get('hobbie')

        for key in constants.dog:
            if constants.dog[key][2] == constants.result:
                constants.dog_ins[2] += 1
                if constants.dog_ins[2] > 1:
                    constants.dog_spisok.remove(constants.last_hobbie)
                    constants.dog_results[constants.last_hobbie_num] -= 1
                constants.dog_results[key] += 1
                constants.last_hobbie_num = key
                constants.dog_spisok.append(constants.result)
                constants.last_hobbie = constants.result
        return redirect("/dog_test_4")
    return render_template("dog_test_1.html", head='Какая вы собака?', if_auto=constants.if_auto, user=constants.user_name,
                           result=constants.result,
                           title='Чем вы предпочли бы заняться?', first='Просмотром фильма или сериала',
                           second='Рисованием', third='Чтением книги', fourth='Спортом', source='/dog_test_3',
                           id_1='Film', id_2='Draw', id_3='Book', id_4='Sport',
                           value_1='Кино',
                           value_2='Рисование', value_3='Книги', value_4='Спорт', name='hobbie', spisok=constants.dog_spisok,
                           message='Дальше', progress='40%', count=constants.dog_ins, picture='static/img/dog_3.jpeg')


@app.route("/dog_test_4", methods=['POST', 'GET'])
def dog_4():
    if request.method == 'POST':

        constants.result = request.form.get('wish')

        for key in constants.dog:
            if constants.dog[key][3] == constants.result:
                constants.dog_ins[3] += 1
                if constants.dog_ins[3] > 1:
                    constants.dog_spisok.remove(constants.last_power)
                    constants.dog_results[constants.last_power_num] -= 1
                constants.dog_results[key] += 1
                constants.last_power_num = key
                constants.dog_spisok.append(constants.result)
                constants.last_power = constants.result

        return redirect("/dog_test_5")
    return render_template("dog_test_1.html", head='Какая вы собака?', if_auto=constants.if_auto, user=constants.user_name,
                           result=constants.result,
                           title='Что бы вы выбрали?', first='Богатство',
                           second='Любовь', third='Сверхъестественные силы', fourth='Бессмертие',
                           source='/dog_test_4',
                           id_1='Money', id_2='Love', id_3='Powers', id_4='Deathless',
                           value_1='Богатство',
                           value_2='Любовь', value_3='Силы', value_4='Бессмертие', name='wish', spisok=constants.dog_spisok,
                           message='Дальше', progress='60%', count=constants.dog_ins, picture='static/img/dog_4.webp')


@app.route("/dog_test_5", methods=['POST', 'GET'])
def dog_5():
    if request.method == 'POST':

        constants.result = request.form.get('color')

        for key in constants.dog:
            if constants.dog[key][4] == constants.result:
                constants.dog_ins[4] += 1
                if constants.dog_ins[4] > 1:
                    constants.dog_spisok.remove(constants.last_color)
                    constants.dog_results[constants.last_color_num] -= 1
                constants.dog_results[key] += 1
                constants.last_color_num = key
                constants.dog_spisok.append(constants.result)
                constants.last_color = constants.result

        return redirect("/dog_results")
    return render_template("dog_test_1.html", head='Какая вы собака?', if_auto=constants.if_auto, user=constants.user_name,
                           result=constants.result,
                           title='Ваш любимый цвет?', first='Синий',
                           second='Желтый', third='Зеленый', fourth='Красный', source='/dog_test_5',
                           id_1='Blue', id_2='Yellow', id_3='Green', id_4='Red',
                           value_1='Синий',
                           value_2='Желтый', value_3='Зеленый', value_4='Красный', name='color', spisok=constants.dog_spisok,
                           message='Завершить', progress='80%', count=constants.dog_ins, picture='static/img/dog_5.jfif')


@app.route("/dog_results", )
def result_dog():
    maximum = 0
    for key in constants.dog_results:
        if constants.dog_results[key] > maximum:
            maximum = constants.dog_results[key]
            constants.result = key

    new_spisok = []
    for key in constants.dog_inv:
        for item in constants.dog_spisok:
            if item in constants.dog_inv[key] and item not in new_spisok:
                new_spisok.append(item)

    db_sess = db_session.create_session()
    res = Results_Dog(
        dog_1=(constants.dog_spisok)[0],
        dog_2=(constants.dog_spisok)[1],
        dog_3=(constants.dog_spisok)[2],
        dog_4=(constants.dog_spisok)[3],
        dog_5=(constants.dog_spisok)[4],
        user_id=constants.user_id
    )
    db_sess.add(res)
    db_sess.commit()

    db_sess = db_session.create_session()
    ress = Results(
        dog=constants.result,
        user_id=constants.user_id
    )
    db_sess.add(ress)
    db_sess.commit()

    return render_template("result_dog.html", title=constants.result, spis=constants.dog_spisok)


@app.route("/drink_test_1", methods=['POST', 'GET'])
def drink_1():
    if request.method == 'POST':

        constants.result = request.form.get('character')

        for key in constants.drink:
            if constants.drink[key][0] == constants.result:
                constants.drink_ins[0] += 1
                if constants.drink_ins[0] > 1:
                    constants.drink_spisok.remove(constants.last_char)
                    constants.drink_results[constants.last_char_num] -= 1
                constants.drink_results[key] += 1
                constants.last_char_num = key
                constants.drink_spisok.append(constants.result)
                constants.last_char = constants.result
        return redirect("/drink_test_2")
    return render_template("dog_test_1.html", head='Какой вы напиток?', if_auto=constants.if_auto, user=constants.user_name,
                           result=constants.result,
                           title='Как бы вы охарактеризовали себя?', first='Я жизнерадостный человек',
                           second='Я задумчивый человек', third='Я мечтательный человек',
                           fourth='Я много волнуюсь о различных вещах', source='/drink_test_1',
                           id_1='Happy', id_2='Think', id_3='Dream', id_4='Care',
                           value_1='Жизнерадостный',
                           value_2='Задумчивый', value_3='Мечтательный', value_4='Волнение', name='character',
                           spisok=constants.drink_spisok, message='Дальше', progress='0%', count=constants.drink_ins,
                           picture='static/img/drink_1.jpg')


@app.route("/drink_test_2", methods=['POST', 'GET'])
def drink_2():
    if request.method == 'POST':

        constants.result = request.form.get('weather')

        for key in constants.drink:
            if constants.drink[key][1] == constants.result:
                constants.drink_ins[1] += 1
                if constants.drink_ins[1] > 1:
                    constants.drink_spisok.remove(constants.last_wea)
                    constants.drink_results[constants.last_wea_num] -= 1
                constants.drink_results[key] += 1
                constants.last_wea_num = key
                constants.drink_spisok.append(constants.result)
                constants.last_wea = constants.result
        return redirect("/drink_test_3")
    return render_template("dog_test_1.html", head='Какой вы напиток?', if_auto=constants.if_auto, user=constants.user_name,
                           result=constants.result,
                           title='Ваша любимая погода?', first='Дождливая',
                           second='Солнечная', third='Облачная',
                           fourth='Снежная', source='/drink_test_2',
                           id_1='Rainy', id_2='Sunny', id_3='Cloudy', id_4='Snow',
                           value_1='Дождь',
                           value_2='Солнце', value_3='Облачно', value_4='Снег', name='weather', spisok=constants.drink_spisok,
                           message='Дальше', progress='20%', count=constants.drink_ins, picture='static/img/drink_2.jpg')


@app.route("/drink_test_3", methods=['POST', 'GET'])
def drink_3():
    if request.method == 'POST':

        constants.result = request.form.get('time')

        for key in constants.drink:
            if constants.drink[key][2] == constants.result:
                constants.drink_ins[2] += 1
                if constants.drink_ins[2] > 1:
                    constants.drink_spisok.remove(constants.last_time)
                    constants.drink_results[constants.last_time_num] -= 1
                constants.drink_results[key] += 1
                constants.last_time_num = key
                constants.drink_spisok.append(constants.result)
                constants.last_time = constants.result
        return redirect("/drink_test_4")
    return render_template("dog_test_1.html", head='Какой вы напиток?', if_auto=constants.if_auto, user=constants.user_name,
                           result=constants.result,
                           title='Ваше любимое время года?', first='Зима',
                           second='Лето', third='Осень', fourth='Весна', source='/drink_test_3',
                           id_1='Winter', id_2='Summer', id_3='Autumn', id_4='Spring',
                           value_1='Зима',
                           value_2='Лето', value_3='Осень', value_4='Весна', name='time', spisok=constants.drink_spisok,
                           message='Дальше', progress='40%', count=constants.drink_ins, picture='static/img/drink_3.jpg')


@app.route("/drink_test_4", methods=['POST', 'GET'])
def drink_4():
    if request.method == 'POST':

        constants.result = request.form.get('genre')

        for key in constants.drink:
            if constants.drink[key][3] == constants.result:
                constants.drink_ins[3] += 1
                if constants.drink_ins[3] > 1:
                    constants.drink_spisok.remove(constants.last_genre)
                    constants.drink_results[constants.last_genre_num] -= 1
                constants.drink_results[key] += 1
                constants.last_genre_num = key
                constants.drink_spisok.append(constants.result)
                constants.last_genre = constants.result

        return redirect("/drink_test_5")
    return render_template("dog_test_1.html", head='Какой вы напиток?', if_auto=constants.if_auto, user=constants.user_name,
                           result=constants.result,
                           title='Какой жанр книг вы бы предпочли?', first='Детектив',
                           second='Фантастика', third='Роман', fourth='Фэнтези',
                           source='/drink_test_4',
                           id_1='Детектив', id_2='Fantastic', id_3='Roman', id_4='Fantasy',
                           value_1='Богатство',
                           value_2='Фантастика', value_3='Роман', value_4='Фэнтези', name='genre',
                           spisok=constants.drink_spisok,
                           message='Дальше', progress='60%', count=constants.drink_ins, picture='static/img/drink_4.jpg')


@app.route("/drink_test_5", methods=['POST', 'GET'])
def drink_5():
    if request.method == 'POST':

        constants.result = request.form.get('manage')

        for key in constants.drink:
            if constants.drink[key][4] == constants.result:
                constants.drink_ins[4] += 1
                if constants.drink_ins[4] > 1:
                    constants.drink_spisok.remove(constants.last_man)
                    constants.drink_results[constants.last_man_num] -= 1
                constants.drink_results[key] += 1
                constants.last_man_num = key
                constants.drink_spisok.append(constants.result)
                constants.last_man = constants.result

        return redirect("/drink_results")
    return render_template("dog_test_1.html", head='Какой вы напиток?', if_auto=constants.if_auto, user=constants.user_name,
                           result=constants.result,
                           title='Насколько вы организованны?', first='Я умею распределять свое время',
                           second='Я часто прокрастинирую и откладываю на потом', third='Я делаю все заранее',
                           fourth='Я часто ленюсь и ничего не делаю', source='/drink_test_5',
                           id_1='Blue', id_2='Yellow', id_3='Green', id_4='Red',
                           value_1='Умею',
                           value_2='Прокрастинирую', value_3='Заранее', value_4='Ничего', name='manage',
                           spisok=constants.drink_spisok,
                           message='Завершить', progress='80%', count=constants.drink_ins, picture='static/img/drink_5.webp')


@app.route("/drink_results", )
def result_drink():
    maximum = 0
    for key in constants.drink_results:
        if constants.drink_results[key] > maximum:
            maximum = constants.drink_results[key]
            constants.result = key

    new_spisok = []
    for key in constants.drink_inv:
        for item in constants.drink_spisok:
            if item in constants.drink_inv[key] and item not in new_spisok:
                new_spisok.append(item)

    db_sess = db_session.create_session()
    res = Results_Drink(
        drink_1=(constants.drink_spisok)[0],
        drink_2=(constants.drink_spisok)[1],
        drink_3=(constants.drink_spisok)[2],
        drink_4=(constants.drink_spisok)[3],
        drink_5=(constants.drink_spisok)[4],
        user_id=constants.user_id
    )
    db_sess.add(res)
    db_sess.commit()

    db_sess = db_session.create_session()
    ress = Results(
        drink=constants.result,
        user_id=constants.user_id
    )
    db_sess.add(ress)
    db_sess.commit()

    return render_template("result_dog.html", head='Какой вы напиток?', title=constants.result, spis=constants.drink_spisok)


@app.route("/cat_test_1", methods=['POST', 'GET'])
def cat_1():
    if request.method == 'POST':

        constants.result = request.form.get('subject')

        for key in constants.cat:
            if constants.cat[key][0] == constants.result:
                constants.cat_ins[0] += 1
                if constants.cat_ins[0] > 1:
                    constants.cat_spisok.remove(constants.last_sub)
                    constants.cat_results[constants.last_sub_num] -= 1
                constants.cat_results[key] += 1
                constants.last_sub_num = key
                constants.cat_spisok.append(constants.result)
                constants.last_sub = constants.result
        return redirect("/cat_test_2")
    return render_template("dog_test_1.html", head='Какой вы кот?', if_auto=constants.if_auto, user=constants.user_name,
                           result=constants.result,
                           title='В какой области вы чувствуете себя более уверенно?', first='Математика',
                           second='Гуманитарные науки', third='Биология',
                           fourth='Искусство', source='/cat_test_1',
                           id_1='Maths', id_2='Gum', id_3='Biology', id_4='Art',
                           value_1='Математика',
                           value_2='Гуманитарные науки', value_3='Биология', value_4='Искусство', name='subject',
                           spisok=constants.cat_spisok, message='Дальше', progress='0%', count=constants.cat_ins,
                           picture='static/img/cat_1.jpg')


@app.route("/cat_test_2", methods=['POST', 'GET'])
def cat_2():
    if request.method == 'POST':

        constants.result = request.form.get('type')

        for key in constants.cat:
            if constants.cat[key][1] == constants.result:
                constants.cat_ins[1] += 1
                if constants.cat_ins[1] > 1:
                    constants.cat_spisok.remove(constants.last_type)
                    constants.cat_results[constants.last_type_num] -= 1
                constants.cat_results[key] += 1
                constants.last_type_num = key
                constants.cat_spisok.append(constants.result)
                constants.last_type = constants.result
        return redirect("/cat_test_3")
    return render_template("dog_test_1.html", head='Какой вы кот?', if_auto=constants.if_auto, user=constants.user_name,
                           result=constants.result,
                           title='Кем вы себя считаете?', first='Амбивертом',
                           second='Экстравертом', third='Интровертом',
                           fourth='Не знаю', source='/cat_test_2',
                           id_1='Ambi', id_2='Extra', id_3='Intro', id_4='Dont',
                           value_1='Амбиверт',
                           value_2='Экстраверт', value_3='Интроверт', value_4='Незнаю', name='type',
                           spisok=constants.cat_spisok,
                           message='Дальше', progress='20%', count=constants.cat_ins, picture='static/img/cat_2.jpg')


@app.route("/cat_test_3", methods=['POST', 'GET'])
def cat_3():
    if request.method == 'POST':

        constants.result = request.form.get('music')

        for key in constants.cat:
            if constants.cat[key][2] == constants.result:
                constants.cat_ins[2] += 1
                if constants.cat_ins[2] > 1:
                    constants.cat_spisok.remove(constants.last_mus)
                    constants.cat_results[constants.last_mus_num] -= 1
                constants.cat_results[key] += 1
                constants.last_mus_num = key
                constants.cat_spisok.append(constants.result)
                constants.last_mus = constants.result
        return redirect("/cat_test_4")
    return render_template("dog_test_1.html", head='Какой вы кот?', if_auto=constants.if_auto, user=constants.user_name,
                           result=constants.result,
                           title='Какую музыку предпочитаете?', first='Рок',
                           second='Рэп', third='Поп', fourth='Инди', source='/cat_test_3',
                           id_1='Rock', id_2='Rap', id_3='Pop', id_4='Indi',
                           value_1='Рок',
                           value_2='Рэп', value_3='Поп', value_4='Инди', name='music', spisok=constants.cat_spisok,
                           message='Дальше', progress='40%', count=constants.cat_ins, picture='static/img/cat_3.webp')


@app.route("/cat_test_4", methods=['POST', 'GET'])
def cat_4():
    if request.method == 'POST':

        constants.result = request.form.get('app')

        for key in constants.cat:
            if constants.cat[key][3] == constants.result:
                constants.cat_ins[3] += 1
                if constants.cat_ins[3] > 1:
                    constants.cat_spisok.remove(constants.last_app)
                    constants.cat_results[constants.last_app_num] -= 1
                constants.cat_results[key] += 1
                constants.last_app_num = key
                constants.cat_spisok.append(constants.result)
                constants.last_app = constants.result

        return redirect("/cat_test_5")
    return render_template("dog_test_1.html", head='Какой вы кот?', if_auto=constants.if_auto, user=constants.user_name,
                           result=constants.result,
                           title='Какая соцсеть удобнее для вас?', first='Фейсбук',
                           second='Твиттер', third='Инстаграм', fourth='ВК',
                           source='/cat_test_4',
                           id_1='Facebook', id_2='Twitter', id_3='Insta', id_4='VK',
                           value_1='Фейсбук',
                           value_2='Твиттер', value_3='Инстаграм', value_4='ВК', name='app',
                           spisok=constants.cat_spisok,
                           message='Дальше', progress='60%', count=constants.cat_ins, picture='static/img/cat_4.jpeg')


@app.route("/cat_test_5", methods=['POST', 'GET'])
def cat_5():
    if request.method == 'POST':

        constants.result = request.form.get('friends')

        for key in constants.cat:
            if constants.cat[key][4] == constants.result:
                constants.cat_ins[4] += 1
                if constants.cat_ins[4] > 1:
                    constants.cat_spisok.remove(constants.last_fri)
                    constants.cat_results[constants.last_fri_num] -= 1
                constants.cat_results[key] += 1
                constants.last_fri_num = key
                constants.cat_spisok.append(constants.result)
                constants.last_fri = constants.result

        return redirect("/cat_results")
    return render_template("dog_test_1.html", head='Какой вы кот?', if_auto=constants.if_auto, user=constants.user_name,
                           result=constants.result,
                           title='Сложно ли вам было бы без друзей?', first='Нет, я могу побыть и один',
                           second='Да, сложно', third='Иногда было бы',
                           fourth='Не испытывал', source='/cat_test_5',
                           id_1='Yes', id_2='No', id_3='Some', id_4='Know',
                           value_1='Нет',
                           value_2='Да', value_3='Иногда', value_4='Неиспытывал', name='friends',
                           spisok=constants.cat_spisok,
                           message='Завершить', progress='80%', count=constants.cat_ins, picture='static/img/cat_5.webp')


@app.route("/cat_results")
def result_cat():
    maximum = 0
    for key in constants.cat_results:
        if constants.cat_results[key] > maximum:
            maximum = constants.cat_results[key]
            constants.result = key

    new_spisok = []
    for key in constants.cat_inv:
        for item in constants.cat_spisok:
            if item in constants.cat_inv[key] and item not in new_spisok:
                new_spisok.append(item)

    db_sess = db_session.create_session()
    res = Results_Cat(
        cat_1=(constants.cat_spisok)[0],
        cat_2=(constants.cat_spisok)[1],
        cat_3=(constants.cat_spisok)[2],
        cat_4=(constants.cat_spisok)[3],
        cat_5=(constants.cat_spisok)[4],
        user_id=constants.user_id
    )
    db_sess.add(res)
    db_sess.commit()

    db_sess = db_session.create_session()
    ress = Results(
        cat=constants.result,
        user_id=constants.user_id
    )
    db_sess.add(ress)
    db_sess.commit()

    return render_template("result_dog.html", head='Какой вы кот?', title=constants.result, spis=constants.cat_spisok)


@app.route("/chin_test_1", methods=['POST', 'GET'])
def chin_1():
    if request.method == 'POST':

        constants.result = request.form.get('film')

        for key in constants.chin:
            if constants.chin[key][0] == constants.result:
                constants.chin_ins[0] += 1
                if constants.chin_ins[0] > 1:
                    constants.chin_spisok.remove(constants.last_film)
                    constants.chin_results[constants.last_film_num] -= 1
                constants.chin_results[key] += 1
                constants.last_film_num = key
                constants.chin_spisok.append(constants.result)
                constants.last_film = constants.result
        return redirect("/chin_test_2")
    return render_template("dog_test_1.html", head='Какая вы шиншилла?', if_auto=constants.if_auto, user=constants.user_name,
                           result=constants.result,
                           title='Какое кино вы бы посмотрели?', first='Комедия',
                           second='Боевик', third='Фантастика',
                           fourth='Артхаус', source='/chin_test_1',
                           id_1='Comedian', id_2='Battle', id_3='Fanta', id_4='Arthouse',
                           value_1='Комедия',
                           value_2='Боевик', value_3='Фантастика', value_4='Артхаус', name='film',
                           spisok=constants.chin_spisok, message='Дальше', progress='0%', count=constants.chin_ins,
                           picture='static/img/chin_1.webp')


@app.route("/chin_test_2", methods=['POST', 'GET'])
def chin_2():
    if request.method == 'POST':

        constants.result = request.form.get('people')

        for key in constants.chin:
            if constants.chin[key][1] == constants.result:
                constants.chin_ins[1] += 1
                if constants.chin_ins[1] > 1:
                    constants.chin_spisok.remove(constants.last_people)
                    constants.chin_results[constants.last_people_num] -= 1
                constants.chin_results[key] += 1
                constants.last_people_num = key
                constants.chin_spisok.append(constants.result)
                constants.last_people = constants.result
        return redirect("/chin_test_3")
    return render_template("dog_test_1.html", head='Какая вы шиншилла?', if_auto=constants.if_auto, user=constants.user_name,
                           result=constants.result,
                           title='С кем обычно вы проводите свое свободное время?', first='С группой друзей',
                           second='С семьей', third='С лучшим другом',
                           fourth='В одиночестве', source='/chin_test_2',
                           id_1='Group', id_2='Family', id_3='Friend', id_4='Alone',
                           value_1='Группа',
                           value_2='Семья', value_3='Друг', value_4='Один', name='people', spisok=constants.chin_spisok,
                           message='Дальше', progress='20%', count=constants.chin_ins, picture='static/img/chin_2.jpg')


@app.route("/chin_test_3", methods=['POST', 'GET'])
def chin_3():
    if request.method == 'POST':

        constants.result = request.form.get('fear')

        for key in constants.chin:
            if constants.chin[key][2] == constants.result:
                constants.chin_ins[2] += 1
                if constants.chin_ins[2] > 1:
                    constants.chin_spisok.remove(constants.last_fear)
                    constants.chin_results[constants.last_fear_num] -= 1
                constants.chin_results[key] += 1
                constants.last_fear_num = key
                constants.chin_spisok.append(constants.result)
                constants.last_fear = constants.result
        return redirect("/chin_test_4")
    return render_template("dog_test_1.html", head='Какая ты шиншилла?', if_auto=constants.if_auto, user=constants.user_name,
                           result=constants.result,
                           title='Ваш страх?', first='Одиночество',
                           second='Смерть', third='Высота', fourth='Разочарованность', source='/chin_test_3',
                           id_1='Lonely', id_2='Death', id_3='Height', id_4='Dissapoint',
                           value_1='Одиночество',
                           value_2='Смерть', value_3='Высота', value_4='Разочарованность', name='fear',
                           spisok=constants.chin_spisok,
                           message='Дальше', progress='40%', count=constants.chin_ins, picture='static/img/chin_3.jfif')


@app.route("/chin_test_4", methods=['POST', 'GET'])
def chin_4():
    if request.method == 'POST':

        constants.result = request.form.get('like')

        for key in constants.chin:
            if constants.chin[key][3] == constants.result:
                constants.chin_ins[3] += 1
                if constants.chin_ins[3] > 1:
                    constants.chin_spisok.remove(constants.last_like)
                    constants.chin_results[constants.last_like_num] -= 1
                constants.chin_results[key] += 1
                constants.last_like_num = key
                constants.chin_spisok.append(constants.result)
                constants.last_like = constants.result

        return redirect("/chin_test_5")
    return render_template("dog_test_1.html", head='Какая ты шиншилла?', if_auto=constants.if_auto, user=constants.user_name,
                           result=constants.result,
                           title='Что больше всего вас привлекает в людях?', first='Ум',
                           second='Харизма', third='Трудолюбие', fourth='Чувственность',
                           source='/chin_test_4',
                           id_1='Smart', id_2='Kharizma', id_3='Doing', id_4='Feels',
                           value_1='Ум',
                           value_2='Харизма', value_3='Трудолюбие', value_4='Чувственность', name='like',
                           spisok=constants.chin_spisok,
                           message='Дальше', progress='60%', count=constants.chin_ins, picture='static/img/chin_4.webp')


@app.route("/chin_test_5", methods=['POST', 'GET'])
def chin_5():
    if request.method == 'POST':

        constants.result = request.form.get('believe')

        for key in constants.chin:
            if constants.chin[key][4] == constants.result:
                constants.chin_ins[4] += 1
                if constants.chin_ins[4] > 1:
                    constants.chin_spisok.remove(constants.last_believe)
                    constants.chin_results[constants.last_believe_num] -= 1
                constants.chin_results[key] += 1
                constants.last_believe_num = key
                constants.chin_spisok.append(constants.result)
                constants.last_believe = constants.result

        return redirect("/chin_results")
    return render_template("dog_test_1.html", head='Какая ты шиншилла?', if_auto=constants.if_auto, user=constants.user_name,
                           result=constants.result,
                           title='Доверяете ли вы людям?', first='Скорее да, чем нет',
                           second='Скорее нет, чем да', third='Определенно',
                           fourth='Нет', source='/chin_test_5',
                           id_1='Yesno', id_2='Noyes', id_3='Yes', id_4='No',
                           value_1='Данет',
                           value_2='Нетда', value_3='Да', value_4='Нет', name='believe',
                           spisok=constants.chin_spisok,
                           message='Завершить', progress='80%', count=constants.chin_ins, picture='static/img/chin_5.jfif')


@app.route("/chin_results", )
def result_chin():
    maximum = 0
    for key in constants.chin_results:
        if constants.chin_results[key] > maximum:
            maximum = constants.chin_results[key]
            constants.result = key

    new_spisok = []
    for key in constants.chin_inv:
        for item in constants.chin_spisok:
            if item in constants.chin_inv[key] and item not in new_spisok:
                new_spisok.append(item)

    db_sess = db_session.create_session()
    res = Results_Chin(
        chin_1=(constants.chin_spisok)[0],
        chin_2=(constants.chin_spisok)[1],
        chin_3=(constants.chin_spisok)[2],
        chin_4=(constants.chin_spisok)[3],
        chin_5=(constants.chin_spisok)[4],
        user_id=constants.user_id
    )
    db_sess.add(res)
    db_sess.commit()

    db_sess = db_session.create_session()
    ress = Results(
        chinchilla=constants.result,
        user_id=constants.user_id
    )
    db_sess.add(ress)
    db_sess.commit()

    return render_template("result_dog.html", head='Какая вы шиншилла?', title=constants.result, spis=constants.chin_spisok)


@app.route('/register', methods=['GET', 'POST'])
def register():
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
        constants.if_auto = True
        constants.user_name = user.name
        constants.user_email = user.email
        constants.user_id = user.id
        return redirect("/")
    return render_template('register.html', title='Регистрация', form=form, if_auto=constants.if_auto, user=constants.user_name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            constants.if_auto = True
            constants.user_name = user.name
            constants.user_email = user.email
            constants.user_id = user.id
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль. Возможно, требуется регистрация",
                               form=form)

    return render_template('login.html', title='Авторизация', form=form, if_auto=constants.if_auto, user=constants.user_name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/personal')
def person():
    form = RequestsForm()
    return render_template("personal.html", user=constants.user_name, if_auto=constants.if_auto, email=constants.user_email, form=form)


@app.route('/statistics', methods=['GET', 'POST'])
def statistics():
    if constants.if_auto:
        main_dog_diagram()
        main_drink_diagram()
        main_cat_diagram()
        main_chin_diagram()
        return render_template('diagram.html')
    else:
        return render_template('diagram_error.html')


@app.route('/dog_more_info', methods=['GET', 'POST'])
def dog_more_info():
    for i in range(1, 6):
        eval(f'info_dog_diagram{i}()')
    return render_template('info_dog_diagram.html')


@app.route('/drink_more_info', methods=['GET', 'POST'])
def drink_more_info():
    for i in range(1, 6):
        eval(f'info_drink_diagram{i}()')
    return render_template('info_drink_diagram.html')


@app.route('/cat_more_info', methods=['GET', 'POST'])
def cat_more_info():
    for i in range(1, 6):
        eval(f'info_cat_diagram{i}()')
    return render_template('info_cat_diagram.html')


@app.route('/chin_more_info', methods=['GET', 'POST'])
def chin_more_info():
    for i in range(1, 6):
        eval(f'info_chin_diagram{i}()')
    return render_template('info_chin_diagram.html')


def main():
    db_session.global_init("db/tests.db")
    api.add_resource(ResultsResource, '/api/v2/results')
    api.add_resource(Results_DogListResource, '/api/v2/results_dog')
    api.add_resource(Results_DrinkListResource, '/api/v2/results_drink')
    api.add_resource(Results_CatListResource, '/api/v2/results_cat')
    api.add_resource(Results_ChinchillaListResource, '/api/v2/results_chinchilla')

    app.run(port=8080)


if __name__ == '__main__':
    db_session.global_init("db/tests.db")
    api.add_resource(ResultsResource, '/api/v2/results')
    api.add_resource(Results_DogListResource, '/api/v2/results_dog')
    api.add_resource(Results_DrinkListResource, '/api/v2/results_drink')
    api.add_resource(Results_CatListResource, '/api/v2/results_cat')
    api.add_resource(Results_ChinchillaListResource, '/api/v2/results_chinchilla')

    app.run(port=8080)
