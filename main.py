from flask import Flask, render_template, redirect, url_for, request, jsonify, flash, send_from_directory, abort
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from persiantools.jdatetime import JalaliDateTime
from functools import wraps
from forms import LoginForm, RegisterForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

##CREATE DB


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///GH.db'
db = SQLAlchemy()
db.init_app(app)


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))


class Sensors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Integer, nullable=False)
    humidity = db.Column(db.Integer, nullable=False)
    level1 = db.Column(db.Integer, nullable=False)
    level2 = db.Column(db.Integer, nullable=False)
    level3 = db.Column(db.Integer, nullable=False)
    level4 = db.Column(db.Integer, nullable=False)
    ph = db.Column(db.Integer, nullable=False)
    ec = db.Column(db.Integer, nullable=False)
    hour = db.Column(db.Integer, nullable=False)


class Outputs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pump1 = db.Column(db.Integer, nullable=False)
    pump1_auto = db.Column(db.Integer, nullable=False)
    pump2 = db.Column(db.Integer, nullable=False)
    pump2_auto = db.Column(db.Integer, nullable=False)
    pump3 = db.Column(db.Integer, nullable=False)
    pump3_auto = db.Column(db.Integer, nullable=False)
    pump4 = db.Column(db.Integer, nullable=False)
    pump4_auto = db.Column(db.Integer, nullable=False)
    pump5 = db.Column(db.Integer, nullable=False)
    pump5_auto = db.Column(db.Integer, nullable=False)
    pump6 = db.Column(db.Integer, nullable=False)
    pump6_auto = db.Column(db.Integer, nullable=False)
    fan1 = db.Column(db.Integer, nullable=False)
    fan1_auto = db.Column(db.Integer, nullable=False)
    fan2 = db.Column(db.Integer, nullable=False)
    fan2_auto = db.Column(db.Integer, nullable=False)
    fan3 = db.Column(db.Integer, nullable=False)
    fan3_auto = db.Column(db.Integer, nullable=False)
    fan4 = db.Column(db.Integer, nullable=False)
    fan4_auto = db.Column(db.Integer, nullable=False)
    fan5 = db.Column(db.Integer, nullable=False)
    fan5_auto = db.Column(db.Integer, nullable=False)
    fan6 = db.Column(db.Integer, nullable=False)
    fan6_auto = db.Column(db.Integer, nullable=False)





with app.app_context():
    db.create_all()


# temp = input("temp:")
# hum = input("hum:")
# ph= input("ph:")
# ec = input("ec:")
# lev1 = input("l1:")
# lev2 = input("l2:")
# lev3 = input("l3:")
# lev4 = input("l4:")
# mp1 = input("mp1:")

temp = 40
hum = 68
ph = 6
ec = 1
lev1 = 1
lev2 = 1
lev3 = 1
lev4 = 1
mp1 = 1
current_date_and_time = JalaliDateTime.now()
hour = current_date_and_time.strftime('%H')

situation = Sensors(temperature=temp,
    humidity=hum,
    level1=lev1,
    level2=lev2,
    level3=lev3,
    level4=lev4,
    ph=ph,
    ec=ec, hour=hour)


result = Outputs(
    pump1=0, pump1_auto=1,
    pump2=0, pump2_auto=1,
    pump3=0, pump3_auto=1,
    pump4=0, pump4_auto=1,
    pump5=0, pump5_auto=1,
    pump6=0, pump6_auto=1,
    fan1=1, fan1_auto=1,
    fan2=0, fan2_auto=1,
    fan3=1, fan3_auto=1,
    fan4=0, fan4_auto=1,
    fan5=1, fan5_auto=1,
    fan6=0, fan6_auto=1)


with app.app_context():
    db.session.add(situation)
    db.session.add(result)
    db.session.commit()


def pump_1():
    last_row = Sensors.query.order_by(Sensors.id.desc()).first()
    floater1 = last_row.level1
    floater2 = last_row.level2
    floater3 = last_row.level3
    floater4 = last_row.level4
    print("p1")
    if floater1 == 1:
        last_out = Outputs.query.order_by(Outputs.id.desc()).first()
        last_out.pump2 = 1
        db.session.commit()


def pump_2():
    last_row = Sensors.query.order_by(Sensors.id.desc()).first()
    floater1 = last_row.level1
    floater2 = last_row.level2
    floater3 = last_row.level3
    floater4 = last_row.level4
    print(11)
    if floater1 == 1:
        last_out = Outputs.query.order_by(Outputs.id.desc()).first()
        last_out.pump2 = 1
        db.session.commit()


def pump_3():
    last_row = Sensors.query.order_by(Sensors.id.desc()).first()
    floater1 = last_row.level1
    floater2 = last_row.level2
    floater3 = last_row.level3
    floater4 = last_row.level4
    print(11)
    if floater1 == 1:
        last_out = Outputs.query.order_by(Outputs.id.desc()).first()
        last_out.pump2 = 1
        db.session.commit()


def pump_4():
    last_row = Sensors.query.order_by(Sensors.id.desc()).first()
    floater1 = last_row.level1
    floater2 = last_row.level2
    floater3 = last_row.level3
    floater4 = last_row.level4
    print(11)
    if floater1 == 1:
        last_out = Outputs.query.order_by(Outputs.id.desc()).first()
        last_out.pump2 = 1
        db.session.commit()


def pump_5():
    last_row = Sensors.query.order_by(Sensors.id.desc()).first()
    floater1 = last_row.level1
    floater2 = last_row.level2
    floater3 = last_row.level3
    floater4 = last_row.level4
    print(11)
    if floater1 == 1:
        last_out = Outputs.query.order_by(Outputs.id.desc()).first()
        last_out.pump2 = 1
        db.session.commit()


def pump_6():
    last_row = Sensors.query.order_by(Sensors.id.desc()).first()
    floater1 = last_row.level1
    floater2 = last_row.level2
    floater3 = last_row.level3
    floater4 = last_row.level4
    print(11)
    if floater1 == 1:
        last_out = Outputs.query.order_by(Outputs.id.desc()).first()
        last_out.pump2 = 1
        db.session.commit()


def fan_1():
    last_row = Sensors.query.order_by(Sensors.id.desc()).first()
    floater1 = last_row.level1
    floater2 = last_row.level2
    floater3 = last_row.level3
    floater4 = last_row.level4
    print("f1")
    if floater1 == 1:
        last_out = Outputs.query.order_by(Outputs.id.desc()).first()
        last_out.pump2 = 1
        db.session.commit()


def fan_2():
    last_row = Sensors.query.order_by(Sensors.id.desc()).first()
    floater1 = last_row.level1
    floater2 = last_row.level2
    floater3 = last_row.level3
    floater4 = last_row.level4
    print(11)
    if floater1 == 1:
        last_out = Outputs.query.order_by(Outputs.id.desc()).first()
        last_out.pump2 = 1
        db.session.commit()


def fan_3():
    last_row = Sensors.query.order_by(Sensors.id.desc()).first()
    floater1 = last_row.level1
    floater2 = last_row.level2
    floater3 = last_row.level3
    floater4 = last_row.level4
    print(11)
    if floater1 == 1:
        last_out = Outputs.query.order_by(Outputs.id.desc()).first()
        last_out.pump2 = 1
        db.session.commit()


def fan_4():
    last_row = Sensors.query.order_by(Sensors.id.desc()).first()
    floater1 = last_row.level1
    floater2 = last_row.level2
    floater3 = last_row.level3
    floater4 = last_row.level4
    print(11)
    if floater1 == 1:
        last_out = Outputs.query.order_by(Outputs.id.desc()).first()
        last_out.pump2 = 1
        db.session.commit()


def fan_5():
    last_row = Sensors.query.order_by(Sensors.id.desc()).first()
    floater1 = last_row.level1
    floater2 = last_row.level2
    floater3 = last_row.level3
    floater4 = last_row.level4
    print(11)
    if floater1 == 1:
        last_out = Outputs.query.order_by(Outputs.id.desc()).first()
        last_out.pump2 = 1
        db.session.commit()


def fan_6():
    last_row = Sensors.query.order_by(Sensors.id.desc()).first()
    floater1 = last_row.level1
    floater2 = last_row.level2
    floater3 = last_row.level3
    floater4 = last_row.level4
    print(11)
    if floater1 == 1:
        last_out = Outputs.query.order_by(Outputs.id.desc()).first()
        last_out.pump2 = 1
        db.session.commit()


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
@login_required
def home():
    current = JalaliDateTime.now()
    date = current.strftime('%Y/%m/%d')
    last_rows = Sensors.query.order_by(Sensors.id.desc()).limit(5).all()
    last_five_temps = [row.temperature for row in last_rows]
    last_five_hums = [row.humidity for row in last_rows]
    last_five_ph = [row.ph for row in last_rows]
    last_five_ec = [row.ec for row in last_rows]
    last_five_times = [row.hour for row in last_rows]
    last_row = Sensors.query.order_by(Sensors.id.desc()).first()
    return render_template("dashboard.html", date=date,
                           last_temps=last_five_temps, last_hums=last_five_hums, last_ph=last_five_ph,
                           last_ec=last_five_ec, last_times=last_five_times)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('home'))
    return render_template("login.html", form=form, current_user=current_user)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        if User.query.filter_by(email=form.email.data).first():
            print(User.query.filter_by(email=form.email.data).first())
            #User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password=hash_and_salted_password,
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("home"))

    return render_template("register.html", form=form, current_user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/bastar1", methods=['get', 'post'])
def bed1():
    return render_template("bastar1.html")


@app.route("/bastar2", methods=['get', 'post'])
def bed2():
    return render_template("bastar2.html")


@app.route("/bastar3", methods=['get', 'post'])
def bed3():
    return render_template("bastar3.html")


@app.route("/pumps", methods=['get', 'post'])
@login_required
def pumps():
    last_out = Outputs.query.order_by(Outputs.id.desc()).first()
    if request.method == "POST":
        name = request.form["state"]
        num = int(name[0])
        column_name = f'pump{num}_auto'
        wanted = getattr(last_out, column_name)
        print(wanted)
        print(f'last_out.pump{num}_auto')
        if name[-1] == "o":
            exec(f"last_out.pump{num}_auto = 1")
            db.session.commit()
            globals()[f"pump_{num}"]()
        elif name[-1] == "l":
            exec(f"last_out.pump{num}_auto = 0")
            db.session.commit()
        elif name[-1] == "f" and wanted == 0:
            exec(f"last_out.pump{num} = 0")
            db.session.commit()
        elif name[-1] == "n" and wanted == 0:
            print('works')
            exec(f"last_out.pump{num} = 1")
            db.session.commit()
    p1 = last_out.pump1
    p2 = last_out.pump2
    p3 = last_out.pump3
    p4 = last_out.pump4
    p5 = last_out.pump5
    p6 = last_out.pump6
    pa1 = last_out.pump1_auto
    pa2 = last_out.pump2_auto
    pa3 = last_out.pump3_auto
    pa4 = last_out.pump4_auto
    pa5 = last_out.pump5_auto
    pa6 = last_out.pump6_auto
    print(p2)
    return render_template("pumps.html", p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, pa1=pa1, pa2=pa2, pa3=pa3, pa4=pa4, pa5=pa5, pa6=pa6)


@app.route("/fans", methods=['get', 'post'])
@login_required
def fans():
    last_out_fan = Outputs.query.order_by(Outputs.id.desc()).first()
    if request.method == "POST":
        name = request.form["state"]
        num = int(name[0])
        column_name = f'fan{num}_auto'
        wanted = getattr(last_out_fan, column_name)
        print(wanted)
        print(f'last_out_fan.fan{num}_auto')
        if name[-1] == "o":
            exec(f"last_out_fan.fan{num}_auto = 1")
            db.session.commit()
            globals()[f"fan_{num}"]()
        elif name[-1] == "l":
            exec(f"last_out_fan.fan{num}_auto = 0")
            db.session.commit()
        elif name[-1] == "f" and wanted == 0:
            exec(f"last_out_fan.fan{num} = 0")
            db.session.commit()
        elif name[-1] == "n" and wanted == 0:
            print('works')
            exec(f"last_out_fan.fan{num} = 1")
            db.session.commit()
    f1 = last_out_fan.fan1
    f2 = last_out_fan.fan2
    f3 = last_out_fan.fan3
    f4 = last_out_fan.fan4
    f5 = last_out_fan.fan5
    f6 = last_out_fan.fan6
    fa1 = last_out_fan.fan1_auto
    fa2 = last_out_fan.fan2_auto
    fa3 = last_out_fan.fan3_auto
    fa4 = last_out_fan.fan4_auto
    fa5 = last_out_fan.fan5_auto
    fa6 = last_out_fan.fan6_auto
    return render_template("fans.html", f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, fa1=fa1, fa2=fa2, fa3=fa3, fa4=fa4,
                           fa5=fa5, fa6=fa6)


if __name__ == '__main__':
    app.run(debug=True)