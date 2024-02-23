
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CRUD:
  
  def save(self):
      ses = db.session
      ses.add(self)
      ses.commit()
  
  def delete(self):
    ses = db.session
    ses.delete(self)
    ses.commit()
    ...
  



 
class Hod(db.Model, CRUD):
  id = db.Column(db.Integer(), primary_key = True)
  name = db.Column(db.String())
  password = db.Column(db.String(), nullable = False)
  dpt_id = db.Column(db.Integer(), db.ForeignKey('department.id'))



class Student(db.Model, CRUD):
  ...
  id = db.Column(db.Integer(), primary_key = True)
  name = (db.Column(db.String(), nullable = False))
  dpt_id = db.Column(db.Integer(), db.ForeignKey('department.id'))
  class_id = db.Column(db.Integer(), db.ForeignKey('class.id'))

class Subject(db.Model,CRUD):
  id = db.Column(db.Integer(), primary_key = True)
  name = db.Column(db.String(), nullable = False)
  class_id = db.Column(db.Integer(), db.ForeignKey('class.id'))
  

class Subject_Notes(db.Model,CRUD):
  id = db.Column(db.Integer(), primary_key = True)
  name = db.Column(db.String(), nullable = False)
  link = db.Column(db.String(),nullable = False)
  subject_id = db.Column(db.Integer(), db.ForeignKey('subject.id'))


class Class(db.Model, CRUD):
  id = db.Column(db.Integer, primary_key = True)
  dpt_id = db.Column(db.Integer, db.ForeignKey('department.id'))
  sem = db.Column(db.Integer(), nullable = False)
  year = db.Column(db.Integer(), nullable = False)
  subjects = db.relationship(Subject)
  students = db.relationship(Student)





  

class Department (db.Model, CRUD):
  id = db.Column(db.Integer(), primary_key = True)
  name = db.Column(db.String(), unique = True)
  hod = db.relationship(Hod)
  classes = db.relationship(Class)






  