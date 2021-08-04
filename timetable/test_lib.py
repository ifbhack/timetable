import unittest
from timetable_lib import Timetable, Session


class TestTimetable(unittest.TestCase):
    TIMETABLE_STRING = '''Class ID,Unit ID,Class Name,Class Type,Day,Start,End,Location,Staff
4,CAB201,Practical - On Campus Class Weeks 1 - 13 [Internal Mode Only],PRC,Mon,02:00pm,04:00pm,GP S517,""
2,CAB240,Tutorial - On Campus Class Weeks 1 - 13 [Internal Mode Only],TUT,Mon,10:30am,12:00pm,GP S305,""
1,CAB202,Lecture Q&A Session - Online via ZOOM [Internal Mode Only],LEC,Mon,09:00am,10:00am,GP VIRTOLT08,"Feras Dayoub, Luis Mejias Alvarez"
18,CAB202,Tutorial - On Campus Class [Internal Mode Only],TUT,Fri,09:00am,11:00am,GP G216,""
5,IAB207,Tutorial - On Campus Class Weeks 2 - 13 [Internal Mode Only],TUT,Tue,10:00am,12:00pm,GP S507,""'''

    def test_parse(self):
        sessions = list(Timetable(self.TIMETABLE_STRING))
        expected_sessions = [
            Session(4, "CAB201", "Practical - On Campus Class Weeks 1 - 13 [Internal Mode Only]", "PRC", "Mon", "02:00pm", "04:00pm", "GP S517", ""),
            Session(2, "CAB240", "Tutorial - On Campus Class Weeks 1 - 13 [Internal Mode Only]", "TUT", "Mon", "10:30am", "12:00pm", "GP S305", ""),
            Session(1, "CAB202", "Lecture Q&A Session - Online via ZOOM [Internal Mode Only]", "LEC", "Mon", "09:00am", "10:00am", "GP VIRTOLT08", "Feras Dayoub, Luis Mejias Alvarez"),
            Session(18, "CAB202", "Tutorial - On Campus Class [Internal Mode Only]", "TUT", "Fri", "09:00am", "11:00am", "GP G216", ""),
            Session(5, "IAB207", "Tutorial - On Campus Class Weeks 2 - 13 [Internal Mode Only]", "TUT", "Tue", "10:00am", "12:00pm", "GP S507", "")
        ]
        self.assertEqual(sessions, expected_sessions)

    def test_get_contact_info(self):
        pass

    def test_upload_contact_info(self):
        pass
