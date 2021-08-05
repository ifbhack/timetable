from flask import Flask
from timetable_lib import Timetable

TIMETABLE_STRING = '''Class ID,Unit ID,Class Name,Class Type,Day,Start,End,Location,Staff
4,CAB201,Practical - On Campus Class Weeks 1 - 13 [Internal Mode Only],PRC,Mon,02:00pm,04:00pm,GP S517,""
2,CAB240,Tutorial - On Campus Class Weeks 1 - 13 [Internal Mode Only],TUT,Mon,10:30am,12:00pm,GP S305,""
1,CAB202,Lecture Q&A Session - Online via ZOOM [Internal Mode Only],LEC,Mon,09:00am,10:00am,GP VIRTOLT08,"Feras Dayoub, Luis Mejias Alvarez"
18,CAB202,Tutorial - On Campus Class [Internal Mode Only],TUT,Fri,09:00am,11:00am,GP G216,""
5,IAB207,Tutorial - On Campus Class Weeks 2 - 13 [Internal Mode Only],TUT,Tue,10:00am,12:00pm,GP S507,""'''


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    from . import db
    db.init_app(app)

    @app.route('/get')
    def get_contact_info():
        db_ = db.get_db()
        timetable = Timetable(TIMETABLE_STRING)
        contact_info = timetable.get_contact_info(db_)
        print(contact_info)
        return "test"

    @app.route('/upload')
    def upload_contact_info():
        db_ = db.get_db()
        timetable = Timetable(TIMETABLE_STRING)
        timetable.upload_contact_info(db_, "test@test.com")
        return 'test'

    return app
