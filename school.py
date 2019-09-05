class School():

    def __init__(self, name=None, roster=None):
        self.name = name
        if roster is None:
            self.roster = {}
        else:
            self.roster = roster

    def add_student(self, full_name, grade_level):
        if grade_level in self.roster:
            self.roster[grade_level].append(full_name)
        else:
            self.roster[grade_level] = [full_name]