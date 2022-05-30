from option3 import students_list
from option3 import title
from option3 import PrettyTable

def find_student():
  found_students_list = []
  ages = input('Введіть вік студентів по яких хочете бачити інформацію:\n')
  x = [i for i, ltr in enumerate(students_list) if ltr == ages]
  
  for index in x:
      found_students_list.append(students_list[index-1])
      found_students_list.append(students_list[index])
      found_students_list.append(students_list[index+1])
  
  columns = len(title)  
  table = PrettyTable(title)  
  table_data = found_students_list[:]
  
  while table_data:
      table.add_row(table_data[:columns])
      table_data = table_data[columns:]
  print(table)
