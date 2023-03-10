from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

ui = uic.loadUiType('doing_question.ui')[0]


class DoingQuiz(QMainWindow, ui):
    def __init__(self, appwindow):
        super().__init__()
        self.setupUi(appwindow)

    # TODO (ben) once the quizzes in the database have been written, i can make a page for this. need the db to be done first