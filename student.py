class Student():
  gender = ""
  schoolNo = ""
  
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade

  def student_information(self):
    print(f"Student name: {self.name}, age: {self.age}, grade: {self.grade}")
  
students_list = []

def add_student_to_list(name, age, grade):
    student = Student(name, age, grade)
    students_list.append(student)
    print(f"{name} is added to the students list.")