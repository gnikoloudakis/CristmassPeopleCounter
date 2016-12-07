import platform
import time
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy


from GPIO_counter.counter import Motion

# from models import People as people

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'hose.cuervo@gmail.com'
app.config['MAIL_PASSWORD'] = 'spacegr@@'
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['SECRET_KEY'] = 'qwertyuiop[];lkjhgfdsazxcvbnm,../'

if platform.system() == 'Linux':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/pi/dbs//peopleCount.db'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/yannisnikoloudakis/dbs/peopleCount.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

mail = Mail(app)
db = SQLAlchemy(app)
socketio = SocketIO(app)
sched1 = BackgroundScheduler()

# People = people()
motion = Motion()
counter = 0


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    people = db.Column(db.Integer)

    def __init__(self, count):
        self.count = count

    def __repr__(self):
        return '<People Count is: %r>' % self.count


# def check_people():
#     # print(motion.start_sensing())
#     # while True:
#     if motion.start_sensing():
#         # global counter
#         # counter += 1
#         # socketio.emit('more_people', {'people_count': counter})
#         # print(counter)
#         print (True)
#     else:
#         # print(False)
#         pass
#     # time.sleep(0.5)


# sched1.add_job(check_people, 'interval', seconds=0.2, id='count_people', replace_existing=True)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/create_db')
def create():
    db.create_all()
    return 'created Database'


@app.route('/init_db')
def initdb():
    people = People.query.all()
    if people:
        pass
    else:
        count = People(0)
        db.session.add(count)
        db.session.commit()
    return 'db initiated'


@app.route('/set_counter', methods=['POST'])
def set_counter():
    data = request.form
    people = People.query.first()
    people.people = data['counter']
    db.session.commit()
    print data['counter']

    return 'counter was set'


@app.route('/reset_db')
def reset():
    people = People.query.first()
    people.count = 0
    db.session.commit()
    return 'counter was reset'


@app.route('/start_counting')
def resume_counting():
    sched1.start()
    print ('Counting Started')
    return 'Counting Started'


@app.route('/stop_counting')
def pause_counting():
    sched1.shutdown(wait=False)
    print ('Counting Stopped')
    return 'Counting Stopped'


@app.route('/send_mail', methods=['POST'])
def send_mail():
    data = request.form
    print (data['name'])
    msg = Message(data['message'],  # message body
                  sender=(data['name'] + ' ' + data['phone'], data['email']))  # Sender
    # msg = Message(subject="Hello", body="dfghj", recipients=["hose.cuervo@gmail.com"], sender="giannis.nikoloudakis@gmail.com")
    mail.send(msg)
    return 'ok'


@app.route('/test_motion')
def test_motion():
    pass


if __name__ == '__main__':
    # sched1.start()
    socketio.run(app, host='0.0.0.0', port=5000)
