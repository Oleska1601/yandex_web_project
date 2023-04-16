from flask import Flask, render_template, request
from werkzeug.utils import redirect

from data import db_session
from data.users import User

from data import db_session
from flask import Flask, render_template, redirect
from data.users import User
from data.results_dog import Results_Dog
from data.results import Results
from data.reqq import Requests

from forms.user import RegisterForm, LoginForm, RequestsForm
from flask_login import LoginManager, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test_project'
login_manager = LoginManager()
login_manager.init_app(app)

if_auto = False
user_name = ''
user_email = ''
searching = ''
result = ''

user_id = 0

titles = ["тест 'какая ты собака?'", "тест 'какой ты напиток?'", "тест 'какая ты кошка/кот?'",
          "тест 'какая ты шиншилла?'"]

dog = {
    'бульдог': ['Сангвинник', 'Ассам', 'Кино', 'Силы', 'Желтый'],
    'пудель': ['Флегматик', 'Улун', 'Рисование', 'Богатство', 'Синий'],
    'гончая': ['Холерик', 'Фруктовый', 'Спорт', 'Бессмертие', 'Красный'],
    'бобтейл': ['Меланхолик', 'Нет', 'Книги', 'Любовь', 'Зеленый']
}

dog_inv = {
    '1': ['Сангвинник', 'Флегматик', 'Холерик', 'Меланхолик'],
    '2': ['Улун', 'Ассам', 'Фруктовый', 'Нет'],
    '3': ['Кино', 'Рисование', 'Спорт', 'Книги', 'Бессмертие'],
    '4': ['Силы', 'Богатство', 'Любовь', 'Бессмертие'],
    '5': ['Желтый', 'Синий', 'Красный', 'Зеленый']
}

dog_results = {
    'бульдог': 0,
    'пудель': 0,
    'гончая': 0,
    'бобтейл': 0
}

last_dog = ''

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

    searching = request.args['title'].lower()

    if not if_auto:
        return render_template("search_index.html", titles=titles, request=searching, if_auto=if_auto, user=user_name)

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

        return render_template("dog_test_1.html", if_auto=if_auto, user=user_name, result=result,
                               title='Какой у вас темперамент?', first='Холерик',
                               second='Флегматик', third='Сангвинник', fourth='Меланхолик', source='/dog_test_1',
                               id_1='Holeric', id_2='Flegmatic', id_3='Sangvinnic', id_4='Melanholic',
                               value_1='Холерик',
                               value_2='Флегматик', value_3='Сангвинник', value_4='Меланхолик', name='temperament',
                               spisok=dog_spisok, message='Дальше', progress='0%', count=dog_ins)


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

        return render_template("dog_test_1.html", if_auto=if_auto, user=user_name, result=result,
                               title='Ваш любимый чай?', first='Я не пью чай',
                               second='Черный чай Ассам', third='Зеленый чай Молочный Улун',
                               fourth='Черный фруктовый чай', source='/dog_test_2',
                               id_1='Not', id_2='Assam', id_3='Ulun', id_4='Fruit',
                               value_1='Нет',
                               value_2='Ассам', value_3='Улун', value_4='Фруктовый', name='tea', spisok=dog_spisok,
                               message='Дальше', progress='20%', count=dog_ins)


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

        return render_template("dog_test_1.html", if_auto=if_auto, user=user_name, result=result,
                               title='Чем вы предпочли бы заняться?', first='Просмотром фильма или сериала',
                               second='Рисованием', third='Чтением книги', fourth='Спортом', source='/dog_test_3',
                               id_1='Film', id_2='Draw', id_3='Book', id_4='Sport',
                               value_1='Кино',
                               value_2='Рисование', value_3='Книги', value_4='Спорт', name='hobbie', spisok=dog_spisok,
                               message='Дальше', progress='40%', count=dog_ins)


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

        return render_template("dog_test_1.html", if_auto=if_auto, user=user_name, result=result,
                               title='Что бы вы выбрали?', first='Богатство',
                               second='Любовь', third='Сверхъестественные силы', fourth='Бессмертие',
                               source='/dog_test_4',
                               id_1='Money', id_2='Love', id_3='Powers', id_4='Deathless',
                               value_1='Богатство',
                               value_2='Любовь', value_3='Силы', value_4='Бессмертие', name='wish', spisok=dog_spisok,
                               message='Дальше', progress='60%', count=dog_ins)


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

        return render_template("dog_test_1.html", if_auto=if_auto, user=user_name, result=result,
                               title='Ваш любимый цвет?', first='Синий',
                               second='Желтый', third='Зеленый', fourth='Красный', source='/dog_test_5',
                               id_1='Blue', id_2='Yellow', id_3='Green', id_4='Red',
                               value_1='Синий',
                               value_2='Желтый', value_3='Зеленый', value_4='Красный', name='color', spisok=dog_spisok,
                               message='Завершить', progress='80%', count=dog_ins)


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
        dog_1=sorted(dog_spisok)[0],
        dog_2=sorted(dog_spisok)[1],
        dog_3=sorted(dog_spisok)[2],
        dog_4=sorted(dog_spisok)[3],
        dog_5=sorted(dog_spisok)[4],
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

    return render_template("result.html", title=result, spis=dog_spisok)


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


def main():
    db_session.global_init("db/tests.db")

    app.run(port=8080)


if __name__ == '__main__':
    db_session.global_init("db/tests.db")

    app.run(port=8080)