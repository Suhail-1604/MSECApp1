from flask import Flask
from config import DevConfig
from Models import db, Department, Hod, UserHod
from auth import bp as auth
from students import bp as students

app = Flask(__name__)

app.config.from_object(DevConfig())
db.init_app(app)
app.register_blueprint(auth)


def create_model():
    db.create_all()
    it = Department(name = 'it')
    it_hod = Hod(name = 'ayesha banu', dpt_id = 1)
    userhodit = UserHod(username = 'ayesha@hod', password = 'gymguys')
    db.session.add_all([it, it_hod, userhodit])
    db.session.commit()

if __name__ == '__main__':
    create_model()
    app.run()