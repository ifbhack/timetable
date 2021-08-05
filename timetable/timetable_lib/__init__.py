import csv
from io import StringIO
import sqlite3


def get_db():
    return sqlite3.connect("../instance/database.db")


def init_db():
    with open("timetable_lib/schema.sql", encoding="utf-8") as f:
        db = get_db()
        db.executescript(f.read())


class Timetable:
    '''Create a wrapper around a list of sessions
    from a string supplied by the Timetable Planner'''
    def __init__(self, timetable_string):
        self.__timetable_string = timetable_string

    def __iter__(self):
        self.csv_reader = csv.reader(StringIO(self.__timetable_string))
        # Skip description line
        next(self.csv_reader)
        return self

    def __next__(self):
        line = next(self.csv_reader)
        return TimetablePlannerLesson(*line)

    def get_contact_info(self, db):
        return [lesson.get_contact_info(db) for lesson in self]

    def upload_contact_info(self, db, contact_info):
        pass


class Lesson:
    def __init__(self, lesson_id, unit_id):
        self.lession_id = lesson_id
        self.unit_id = unit_id

    def upload_contact_info(self, db, contact_info):
        pass

    def get_contact_info(self, db):
        cur = db.cursor()
        sql = """
            SELECT name, contact FROM Student s
            LEFT JOIN HaveUnit h ON h.studentID=s.studentID
            LEFT JOIN Lessons l ON l.lessonID=h.lessonID
            LEFT JOIN Unit u ON u.unitPK=l.unitPK
            WHERE u.unitID=? AND h.lessonID=?"""  # this doesn't work
        cur.execute(sql, (self.unit_id, self.lession_id))
        print(cur.fetchall())
        return cur.fetchall()


class TimetablePlannerLesson(Lesson):
    def __init__(self, class_id, unit_id, class_name, class_type, day, start,
                 end, location, staff):
        super().__init__(class_id, unit_id)
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
