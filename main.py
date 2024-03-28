from student import Student, add_student_to_list, students_list
from teacher import Teacher, add_teacher_to_list, teachers_list

# Kullanıcıdan öğrenci eklemesini sağlayan fonksiyon
def add_student():
    name = input("Öğrenci adını girin: ")
    age = int(input("Öğrenci yaşını girin: "))
    grade = input("Öğrenci sınıfını girin: ")
    add_student_to_list(name, age, grade)

# Kullanıcıdan öğretmen eklemesini sağlayan fonksiyon
def add_teacher():
    name = input("Öğretmen adını girin: ")
    age = int(input("Öğretmen yaşını girin: "))
    branch = input("Öğretmen branşını girin: ")
    add_teacher_to_list(name, age, branch)

# Kullanıcıya öğrenci veya öğretmen eklemesini isteyen döngü
while True:
    choice = input("Öğrenci eklemek için 'o', öğretmen eklemek için 't', çıkmak için 'q' tuşuna basın: ")

    if choice == 'o':
        add_student()  # add_student fonksiyonunu çağırarak öğrenci eklemesini sağlıyoruz
    elif choice == 't':
        add_teacher()  # add_teacher fonksiyonunu çağırarak öğretmen eklemesini sağlıyoruz
    elif choice == 'q':
        break  # 'q' tuşuna basarak döngüden çıkıyoruz     
    else:
        print("Geçersiz seçim. Lütfen 'o', 't' veya 'q' tuşlarından birini seçin.")

# Eklenen öğrenci ve öğretmen bilgilerini listelerini yazdırıyoruz
print("\nÖğrenciler:")
for student in students_list:
    student.student_information() # Öğrenci bilgilerini ekrana yazdırıyoruz

print("\nÖğretmenler:") 
for teacher in teachers_list:
    teacher.teacher_information() # Öğretmen bilgilerini ekrana yazdırıyoruz