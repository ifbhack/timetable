class StudentModel:
    def __init__(self, db):
        self.db = db

    def upload_contact_info(self, contact_info):
        pass

    def get_contact_info(self, timetable):
        return {
            'CAB201': {
                'a@a.com', # one student contact string
                'a@b.com'
            },
            'CAB202': {

            }
        }


class Student:
    def __init__(self, timetable, contact_info):
        self.timetable = timetable
        self.contact_info = contact_info
# upload
# contact
# unit -> contact

# match units WHERE class_id = ?
# return contacts

# front-end
from lib import StudentModel, Timetable

db = ?
timetable = Timetable()
studentModel = StudentModel(db)
studentModel.get_contact_info(timetable)
