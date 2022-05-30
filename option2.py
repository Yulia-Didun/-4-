from option3 import students_list

def delete_student():
    del_student = input('Введіть ПІБ студента: ')
    index_del_student = students_list.index(del_student)
    students_list.pop(index_del_student)
    students_list.pop(index_del_student)
    students_list.pop(index_del_student)