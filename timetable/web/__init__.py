from flask import Flask
from timetable_lib import Timetable, TIMETABLE_STRING


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
