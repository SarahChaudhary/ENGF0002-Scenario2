from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

ui = uic.loadUiType('doing_question.ui')[0]


class DoingQuiz(QMainWindow, ui):
    def __init__(self, appwindow):
        super().__init__()
        self.setupUi(appwindow)

        self.q_single_answer.hide()
        self.load_quiz()

        self.q_next_question.clicked.connect(self.next_question_clicked)
        self.q_previous_question.clicked.connect(self.previous_question_clicked)
        self.q_check_correct.clicked.connect(self.check_question_clicked)


    def load_quiz(self):
        # need to load the quiz name
        quiz_name = "quiz name"
        self.q_quiz_name.setText(quiz_name)

        # need to load the question number
        question_number = "1"
        self.q_question_number.setText(question_number)

        # need to load the username
        username = "test"
        self.q_by_username.setText('by ' + username)


    def next_question_clicked(self):
        pass

    def previous_question_clicked(self):
        pass

    def check_question_clicked(self):
        pass




