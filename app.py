from PyQt5.QtWidgets import QMainWindow
from create_question import CreateQuestion
from signin import Signin
import database


# TODO: (ben) need to add swapping between page functionality
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        database.init_db()
        # self.setup_create_question()
        self.setup_signin()
        self.show()

    def setup_create_question(self):
        self.setup_create_question_screen = CreateQuestion(self)

    # def setup_doing_quiz(self):
    #     self.setup_doing_quiz_screen = DoingQuiz(Self)

    def setup_signin(self):
        self.setup_signin_screen = Signin(self)

