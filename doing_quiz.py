from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

ui = uic.loadUiType('doing_question.ui')[0]


class DoingQuiz(QMainWindow, ui):
    def __init__(self, appwindow):
        super().__init__()
        self.setupUi(appwindow)

        # list of the pyqt matrix objects NOT VALUES
        self.left_matrix_values = [
            self.q1,
            self.q2,
            self.q3,
            self.q4,
            self.q5,
            self.q6,
            self.q7,
            self.q8,
            self.q9,
        ]
        self.right_matrix_values = [
            self.q10,
            self.q11,
            self.q12,
            self.q13,
            self.q14,
            self.q15,
            self.q16,
            self.q17,
            self.q18,
        ]

        self.q_single_answer.hide()
        self.load_quiz()
        self.load_question()

        self.q_next_question.clicked.connect(self.next_question_clicked)
        self.q_previous_question.clicked.connect(self.previous_question_clicked)
        self.q_check_correct.clicked.connect(self.check_question_clicked)

    def load_quiz(self):
        # load the quiz from database into here, load the questions as well
        
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()

        # get the quiz name
        quiz_id = 1  # do we want to randomly pick a quiz with rand.int for the id number or idk
        c.execute("SELECT name FROM quizzes WHERE id=?", (quiz_id,))
        quiz_name = c.fetchone()[0]

        # load the questions for the quiz
        c.execute("SELECT id, question FROM questions WHERE quiz_id=?", (quiz_id,))
        questions = c.fetchall()

        conn.close()


        
        self.quiz_name = quiz_name
        self.questions = questions
        pass

    def load_question(self):
        
        quiz_id = 1 #i still need to iterate this to get all the questions
        question_number = 1 # placeholder
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        
        # need to load the quiz name into quiz_name variable
        cursor.execute("SELECT name FROM quizzes WHERE id=?", (quiz_id,))
        quiz_name = cursor.fetchone()[0]
        
        # need to load the question number into question_number variable
        cursor.execute("SELECT question FROM questions WHERE quiz_id=? AND number=?", (quiz_id, question_number))
        question_text = cursor.fetchone()[0]
        
        # need to load the username into username variable
        cursor.execute("SELECT username FROM users WHERE id=?", (self.user_id,))
        username = cursor.fetchone()[0]
        db.close()

        # Update on the UI
        
        self.q_quiz_name.setText(quiz_name)
        self.q_question_number.setText(str(question_number))
        self.q_question_text.setText(question_text)
        self.q_by_username.setText('by ' + username)
        self.format_matrices()


    def next_question_clicked(self):
        # load the values for the next question... ill sort the front end of it. make the values a 1d array of strings
        self.question_number += 1
        self.load_question()
        
        self.format_matrices()
        pass

    def previous_question_clicked(self):
        # same here
        self.question_number -= 1
        self.load_question()
        
        self.format_matrices()
        pass

    def check_question_clicked(self):
        # here are the matrix values, as a 1d list of strings
        left_matrix_values = [i.text() for i in self.left_matrix_values]
        right_matrix_values = [i.text() for i in self.right_matrix_values]

        # do the calculations on them, may need to convert to 2d array
        # if it's a unary operation, then use the right matrix values not the left
        # return true or false for now, ill implement through to front end once done
        self.format_matrices()
        pass

    def format_matrices(self):
        # for ben to do
        pass



