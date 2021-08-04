class Timetable:
    def __init__(self, timetable_string):
        self.__timetable_string = timetable_string

    def __iter__(self):
        # Create iterator that loops for each line
        self.timetable_iter = iter(self.__timetable_string.split('\n'))
        # Remove first line containing column infomation
        next(self.timetable_iter)
        return self

    def __next__(self):
        return next(self.timetable_iter)

    def get_contact_info(self):
        for session in self:
            pass

    def upload_contact_info(self):
        for session in self:
            pass


class Session:
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
        if isinstance(other, Session):
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

    def get_contact_info():
        pass

    def upload_contact_info(contact_info):
        pass
