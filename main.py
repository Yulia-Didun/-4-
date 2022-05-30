import option1
import option2
import option3
import option4
import option5

def menu():
    while True:
        print('\t'*6 + 'Виберіть функцію: ')
        print('0. Вихід з програми')
        print('1. Додавання нового студента (запису) в список студентів.')
        print('2. Видалення студента зі списку студентів.')
        print('3. Вивід таблиці з результатом.')
        print('4. Знайти студентів за віком.')
        print('5. Таблиця даних списку студентів групи КН.')
        print('\nВаш вибір: ')
        
        selected_option = int(input())
        if selected_option == 0:
            quit()
        elif selected_option == 1:
            option1.add_new_student()
        elif selected_option == 2:
            option2.delete_student()
        elif selected_option == 3:
            option3.print_table()
        elif selected_option == 4:
            option4.find_student()
        elif selected_option == 5:
            option5.table_data_KN()
        
        print('Ви хочете продовжити?')
        print('Якщо так, введіть: "так", "yes" або "1"')
        print('Якщо ні, введіть: "ні", "no" або "0"')
        resume = input()
        if resume == 'no' or resume == '0' or resume == 'ні':
            quit()

menu()