import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class


class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self,id):
        sql = "Select * From students where id = %s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error: ',err)

    def deleteStudent(self,studentid):
        sql = "Delete From students where id=%s"
        value = (studentid,)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt silindi.')
        except mysql.connector.Error as err:
            print('Hata :', err)


    def getClasses(self):
        sql = "Select * From class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print('Error: ', err)




    def getStudentsByClassId(self, classid):
        sql = "Select * From students where ClassId = %s"
        value = (classid,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error: ', err)

    def addStudent(self, student: Student):
        sql = "INSERT INTO students(id,Name,Surname,Birthdate,Gender,ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (student.id, student.name, student.surname, student.birthdate, student.gender,student.classid)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('Hata :', err)

    def editStudent(self,student: Student):
        sql = "update students set id=%s, Name=%s, Surname=%s, Birthdate=%s, Gender=%s, ClassId=%s Where Studentno=%s"
        value = (student.id, student.name, student.surname, student.birthdate, student.gender, student.classid,student.studentno)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi.')
        except mysql.connector.Error as err:
            print('Hata :', err)

    def addTeacher(self,teacher: Teacher):
        pass

    def editTeacher(self,teacher: Teacher):
        pass

    def __del__(self):
        self.connection.close()
        print('Db silindi.')



db = DbManager()

student = db.getStudentById(8)

student[0].name = "Mehmet"
#student[0].surname = "Yılmaz"
#student[0].id = "14"

#db.addStudent(student[0])
db.editStudent(student[0])


#students = db.getStudentsByClassId(1)
#print(students[0].name)
#print(students[4].name)
