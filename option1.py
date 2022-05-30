from option3 import students_list

def add_new_student():
    new_student_name = input("Введіть ПІБ студента: ")
    new_student_age = input("Введіть вік студента: ")
    new_student_course = input('Введіть курс студента: ')
    students_list.append(new_student_name)
    students_list.append(new_student_age)
    students_list.append(new_student_course)