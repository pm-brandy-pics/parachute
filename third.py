class Student:
    student_id='D021'
    student_name='Brandy'
    student_class='Btech'
    def display():
        print(f'Student ID: {Student.student_id} \n Student name: {Student.student_name} \n')
        print(f'Student class: {Studen.student_class} \n')
print('Original attributes and their values of the student class.')
try:
    Student.display()
    Student.display()
except NameError:
    print('Class name does not exist.')