from dbmanager import DbManager
from Student import Student
import datetime

class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = "*****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Sınıflara Göre Dersler\n7-Çıkış(E)"
        while True:
            print(msg)
            islem = input("Seçim: ")
            if islem == '1':
                self.displayStudents()
            elif islem == '2':
                self.addStudent()
            elif islem == '3':
                self.editStudent()
            elif islem == '4':
                self.deleteStudent()
            elif islem == 'E':
                break
            else:
                print("Yanlış Seçim")


    def displayStudents(self):
        classid = int(input('Hangi sınıf: '))

        students = self.db.getStudentsByClassId(classid)
        print("Öğrenci Listesi")
        for std in students:
            print(f'{std.id}--{std.name} {std.surname}')

        return classid

    def displayClasses(self):
        classes = self.db.getClasses()
        for c in classes:
            print(f'{c.id}:' f'{c.name}')


    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input('Öğrenci id: '))

        self.db.deleteStudent(studentid)


    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input('Öğrenci id: '))

        student = self.db.getStudentById(studentid)

        student[0].name = input('name') or student[0].name
        student[0].surname = input('surname') or student[0].surname
        student[0].gender = input('cinsiyet (E/K)') or student[0].gender
        student[0].classid = input('sınıf: ') or student[0].classid

        year = input("year: ") or student[0].birthdate.year
        month = input("ay: ") or student[0].birthdate.month
        day = input("gün: ") or student[0].birthdate.day

        student[0].birthdate = datetime.date(year,month,day)
        self.db.editStudent(student[0])


    def addStudent(self):
        self.displayClasses()

        classid = int(input('Hangi sınıf: '))
        number = input('numara: ')
        name = input('ad: ')
        surname = input('soyad: ')
        year = int(input('yıl: '))
        month = int(input('ay: '))
        day = int(input('gün: '))

        birthdate = datetime.date(year,month,day)
        gender = input('Cinsiyet (E/K)')

        student = Student(None,name,surname,birthdate,gender,number,classid)
        self.db.addStudent(student)


app = App()
app.initApp()

