from data import db_session
from flask import Flask, render_template, redirect
from data.users import User
from forms.user import RegisterForm, LoginForm
from flask_login import LoginManager, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test_project'
login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('base.html', title='Авторизация')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/main_window')
def main_window():
    return 'Главное окно'


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
        return redirect('/main_window')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            return redirect("/main_window")
        return render_template('login.html',
                               message="Неправильный логин или пароль. Возможно, требуется регистрация",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


def main():
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='0.0.0.0')


if __name__ == '__main__':
    main()