import csv
from io import StringIO
import sqlite3

TIMETABLE_STRING = '''Class ID,Unit ID,Class Name,Class Type,Day,Start,End,Location,Staff
4,CAB201,Practical - On Campus Class Weeks 1 - 13 [Internal Mode Only],PRC,Mon,02:00pm,04:00pm,GP S517,""
2,CAB240,Tutorial - On Campus Class Weeks 1 - 13 [Internal Mode Only],TUT,Mon,10:30am,12:00pm,GP S305,""
1,CAB202,Lecture Q&A Session - Online via ZOOM [Internal Mode Only],LEC,Mon,09:00am,10:00am,GP VIRTOLT08,"Feras Dayoub, Luis Mejias Alvarez"
18,CAB202,Tutorial - On Campus Class [Internal Mode Only],TUT,Fri,09:00am,11:00am,GP G216,""
5,IAB207,Tutorial - On Campus Class Weeks 2 - 13 [Internal Mode Only],TUT,Tue,10:00am,12:00pm,GP S507,""'''


def get_db():
    return sqlite3.connect("database.db")


def init_db():
    with open("timetable_lib/schema.sql", encoding="utf-8") as f:
        db = get_db()
        db.executescript(f.read())


class Timetable:
    def __init__(self, timetable_string):
        self.__timetable_string = timetable_string

    def __iter__(self):
        self.csv_reader = csv.reader(StringIO(self.__timetable_string))
        # Skip description line
        next(self.csv_reader)
        return self

    def __next__(self):
        line = next(self.csv_reader)
        return Lesson(*line)

    def get_contact_info(self, db):
        return [lesson.get_contact_info(db) for lesson in self]

    def upload_contact_info(self, db, contact_info):
        pass


class Lesson:
    def __init__(self, class_id, unit_id, class_name, class_type, day, start,
                 end, location, staff):
        self.class_id = class_id
        self.unit_id = unit_id
        self.class_name = class_name
        self.class_type = class_type
        self.day = day
        self.start = start
        self.end = end
        self.location = location
        self.staff = staff

    def __eq__(self, other):
        if isinstance(other, Lesson):
            return (self.class_id == other.class_id and
                    self.unit_id == other.unit_id and
                    self.class_name == other.class_name and
                    self.class_type == other.class_type and
                    self.day == other.day and
                    self.start == other.start and
                    self.end == other.end and
                    self.location == other.location and
                    self.staff == other.staff)
        else:
            return False

    def upload_contact_info(self, db, contact_info):
        pass

    def get_contact_info(self, db):
        # db fetch
        return self.class_name # temp
