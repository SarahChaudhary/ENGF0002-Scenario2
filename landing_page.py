from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from signin import current
import database


ui = uic.loadUiType('landing_page.ui')[0]
'''
q_signout -> button
q_create_quiz -> button
q_delete_quiz -> button
q_practice_quiz -> button
q_load_quiz -> button
q_calculator -> button
q_quiz_code -> lineedit
q_table -> table
'''


class LandingPage(QMainWindow, ui):
    def __init__(self, appwindow):
        super().__init__()
        self.setupUi(appwindow)

        self.q_load_quiz.clicked.connect(self.load_quiz_clicked)
        self.q_delete_quiz.clicked.connect(self.delete_quiz_clicked)
        
        self.create_table()
        self.q_table.show()
        # signin = Signin()
        # self.username = signin.get_username()
        # print(self.username)
        

    def load_quiz_clicked(self):
        pass

    def delete_quiz_clicked(self):
        pass
    
  

    # function to create table. table will contain quiz id, quiz name, quiz type, number of questions and creator id
    def create_table(self):
        self.q_table = QTableWidget()
        quiz_data = self.load_quiz_data()
        self.q_table.setColumnCount(len(quiz_data[0]))
        self.q_table.setRowCount(len(quiz_data))
        self.q_table.setHorizontalHeaderLabels(['Quiz ID', 'Creator (User) ID', 'Name', 'Type', 'Nr. Questions'])
        self.q_table.setItem(0,0, QTableWidgetItem('yo'))
        self.set_cells(self.q_table, quiz_data)



    def load_table(self):
        user_id = database.get_user_id(current[0])
        database.insert_quiz(user_id, "test", "practice1", 69)
        quiz_data = database.get_quiz_info_by_username(user_id)
        print(quiz_data)

    def load_quiz_data(self):
        user_id = int(database.get_user_id(current[0])[0])

        # functions to insert if you want to test
        # database.insert_quiz(user_id, "test", "practice1", 69)
        # database.insert_quiz(user_id, "test", "practice2", 420)
        
        quiz_data = database.get_quiz_info_by_user_id(user_id)
        return quiz_data

    def set_cells(self, table, data):
        for i in range(len(data)):
            for j in range(len(data[0])):
                print(i, j, data[i][j])
                table.setItem(i, j, QTableWidgetItem(str(data[i][j])))




