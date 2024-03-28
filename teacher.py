class Teacher():
  gender = ""
  subject = ""
  
  def __init__(self,name,age,branch):
    self.name = name
    self.age = age 
    self.branch = branch

  def teacher_information(self):
    print(f"Teacher name: {self.name}, age: {self.age}, branch: {self.branch}")

teachers_list = []

def add_teacher_to_list(name, age, branch):
    teacher = Teacher(name, age, branch)
    teachers_list.append(teacher)
    print(f"{name} is added to the teachers list.")