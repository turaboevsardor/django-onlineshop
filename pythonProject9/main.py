student = {}
c = []

def add_student(name,classrom):
    print(c)
    student[name] = classrom
    c.append(student[name])
    print(student)

def delete_student(name):
    a = student[name]
    c.remove(a)
    student.pop(name)
    print('student ismi blan {} ochirildi'.format(name))


def classroms():
    print(c)

    while True:
     admin = input('nima qilmoqchisiz')

     if admin == 'studentni qoshish':
         student_name = input('studentni ismi')
         student_classroom = int(input('qaysi sinf'))

         add_student(student_name,student_classroom)

         if admin == 'ochirish':
             del_student = input('kimmi ochiramiz')
             delete_student(del_student)

         elif admin == 'sinfning nomeri':
             classroms()