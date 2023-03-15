from PyQt5.QtWidgets import QMainWindow
from create_question import CreateQuestion
from signin import Signin
from calculator import Calculator
from landing_page import LandingPage
import database


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        database.init_db()
        self.setup_signin()
        # self.setup_landing_page()
        self.show()

    def setup_signin(self):
        self.signin_screen = Signin(self)
        self.signin_screen.q_signin_button.clicked.connect(self.move_to_landing)
        self.signin_screen.close()

    def move_to_landing(self):
        print('hello')
        print(f'{self.signin_screen.valid = }')
        if self.signin_screen.valid:
            print('valid')
            self.setup_landing_page()

    def setup_landing_page(self):
        self.landing_page = LandingPage(self)
        self.landing_page.q_signout.clicked.connect(self.setup_signin)
        self.landing_page.q_calculator.clicked.connect(self.setup_calculator)
        self.landing_page.q_practice_quiz.clicked.connect(self.setup_practice_quiz)
        self.landing_page.q_create_quiz.clicked.connect(self.create_question_screen)

    def setup_practice_quiz(self):
        pass

    def setup_calculator(self):
        self.calculator = Calculator(self)

    def setup_create_question(self):
        self.create_question_screen = CreateQuestion(self)

    # def setup_doing_quiz(self):
    #     self.setup_doing_quiz_screen = DoingQuiz(Self)



