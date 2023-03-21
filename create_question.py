from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
import random
from database.py import *
ui = uic.loadUiType("matrix_create_question.ui")[0]

"""
q_operator_dropdown -> QComboBox
q_dimension_dropdown -> QComboBox
q_auto_generate -> QPushButton
q_check_valid -> QPushButton
q_add_question -> QPushButton
q_finish_quiz -> QPushButton
q_update -> QPushButton
q_left_matrix -> widget containing left matrix
q_operator_label -> QLabel
"""


class CreateQuestion(QMainWindow, ui):
    def __init__(self, appwindow):
        super().__init__()
        self.setupUi(appwindow)
        self.added = 0

        # this is the 9 matrix input spaces (QLineEdit) collated into a list [QLineEdit]
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

        # same as above but for the second matrix
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

        # QLine objects that make up the left matrix's brackets

        self.q_check_valid.clicked.connect(self.check_valid_pressed)
        self.q_auto_generate.clicked.connect(self.auto_generate_pressed)
        self.q_add_question.clicked.connect(self.add_question_pressed)
        self.q_finish_quiz.clicked.connect(self.finish_quiz_pressed)
        self.q_update.clicked.connect(self.update_pressed)

    # auxiliary methods for button presses
    def check_matrix_valid(self, matrix_values):
        for i in matrix_values:
            # check if it is empty and if it is a number
            # can remove debug prints
            if i.text() == "" or not i.text().isnumeric():
                print("invalid")
                return False
        print("valid")
        return True

    def auto_generate_vals(self, matrix):
        for i in matrix:
            # arbitrary, can be changed
            i.setText(str(random.randint(0, 9)))

    # these methods below will be called when the corresponding buttons are clicked

    def check_valid_pressed(self):
        # TODO: make sure that only 1 of the matrices are checked when its a binary operator (ben will add this)
        if self.check_matrix_valid(self.left_matrix_values) and self.check_matrix_valid(
            self.right_matrix_values
        ):
            return True
        return False

    # can run this on left_matrix and right_matrix separately (as parameters)
    # TODO (maybe): add button to generate specifically for left/right.
    # Otherwise there might be problems when there is only 1 matrix, such as determinant
    def auto_generate_pressed(self):
        self.auto_generate_vals(self.left_matrix_values)
        self.auto_generate_vals(self.right_matrix_values)

    def add_question_pressed(self):
        # TODO: should check that the question is valid i.e. all fields entered correctly, and then add the question to the database
        acceptable = True
        for value in self.left_matrix_values:
                if value == None or not isinstance(value, (int, float)):
                    acceptable = False
        if self.dropdown_string != "Determinant" and self.dropdown_string != "Inverse": # assumes left matrix will always be filled
            for value in self.right_matrix_values:
                if value == None or not isinstance(value, (int, float)):
                    acceptable = False

        if acceptable:
            self.user_id = get_user_id(current[0])
            self.quiz_info = get_quiz_info_by_user_id(self.user_id) #assumes only one quiz
            insert_question(0, len(self.quiz_info) + self.added , self.left_matrix_values, self.right_matrix_values, self.dropdown_string)
            self.added += 1
        else:
            raise ValueError("invalid operation or values")
        pass

    def finish_quiz_pressed(self):
        # TODO: should add the quiz to the database as long as there is a valid question entered
        insert_quiz(self.user_id, "test", "type", len(self.quiz_info) + self.added)
        # TODO (optional) maybe add date and time to the quiz, both here and ofc in the backend
        pass

    def update_pressed(self):
        # dictionary to take the string from the dropdown box, and convert it to the string for the operator label
        self.operator_dict = {
            "Addition": "+",
            "Subtraction": "-",
            "Multiply": "x",
            "Inverse": "-1",
            "Determinant": "Det",
        }

        self.dropdown_string = self.q_operator_dropdown.currentText()
        self.q_operator_label.setText(self.operator_dict[self.dropdown_string])

        if self.dropdown_string == "Inverse":
            self.q_left_matrix.hide()
            self.q_right_matrix.move(230, 190)
            self.q_operator_label.move(275, 0)

        elif self.dropdown_string == "Determinant":
            self.q_left_matrix.hide()
            self.q_right_matrix.move(230, 190)
            self.q_operator_label.move(0, 90)

        elif (
            self.dropdown_string == "Multiply"
            or self.dropdown_string == "Subtraction"
            or self.dropdown_string == "Addition"
        ):
            # x = self.q_right_matrix.x()
            # y = self.q_right_matrix.y()
            # print(x, y)
            self.q_right_matrix.move(350, 190)
            self.q_operator_label.move(0, 90)
            self.q_left_matrix.show()
            # need to show the left matrix
