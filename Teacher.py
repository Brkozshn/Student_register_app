class Teacher:
    def __init__(self,branch,name,surname,birthdate,gender,studentno,classid):
        if studentno is None:
            self.studentno = 0
        else:
            self.studentno = studentno
        self.branch = branch
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
