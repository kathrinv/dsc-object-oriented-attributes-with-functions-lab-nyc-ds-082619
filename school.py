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
            
    def grade(self, grade_num):
        if grade_num in self.roster:
            return self.roster[grade_num]
        else:
            print("No data for this grade")
    
    def sort_roster(self):
        self.roster = {x:sorted(self.roster[x]) for x in self.roster.keys()}
        #for grade in self.roster:
        #    self.roster[grade] = sorted(self.roster[grade])
        return self.roster