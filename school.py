class School():

    def __init__(self, name=None, roster={}):
        self.name = name
        self.roster = roster

    def add_student(self, full_name, grade_level):
        if grade_level in self.roster:
            self.roster[grade_level] = self.roster[grade_level].append(full_name)
            print(self.roster)
	else:
            self.roster[grade_level] = [].append(full_name)
	    print(self.roster)
	    print(self.roster[grade_level])
