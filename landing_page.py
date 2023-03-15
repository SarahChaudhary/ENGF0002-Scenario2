from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

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

    def load_quiz_clicked(self):
        pass

    def delete_quiz_clicked(self):
        pass


