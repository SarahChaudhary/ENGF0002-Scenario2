from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

ui = uic.loadUiType('matrix_create_question.ui')[0]

'''
q_operator_dropdown -> QComboBox
q_dimension_dropdown -> QComboBox
q_auto_generate -> QPushButton
q_check_valid -> QPushButton
q_add_question -> QPushButton
q_finish_quiz -> QPushButton
q_update -> QPushButton
q_left_matrix -> list(QLineEdit)
q_right_matrix -> list(QLineEdit)
q_operator_label -> QLabel
'''


class CreateQuestion(QMainWindow, ui):
    def __init__(self, appwindow):
        super().__init__()
        self.setupUi(appwindow)

        # this is the 9 matrix input spaces (QLineEdit) collated into a list [QLineEdit]
        self.q_left_matrix = [self.q1,
                              self.q2,
                              self.q3,
                              self.q4,
                              self.q5,
                              self.q6,
                              self.q7,
                              self.q8,
                              self.q9]

        # same as above but for the second matrix
        self.q_right_matrix = [self.q10,
                               self.q11,
                               self.q12,
                               self.q13,
                               self.q14,
                               self.q15,
                               self.q16,
                               self.q17,
                               self.q18]

        self.q_check_valid.clicked.connect(self.check_valid_pressed)
        self.q_auto_generate.clicked.connect(self.auto_generate_pressed)
        self.q_add_question.clicked.connect(self.add_question_pressed)
        self.q_finish_quiz.clicked.connect(self.finish_quiz_pressed)
        self.q_update.clicked.connect(self.update_pressed)

    def check_valid_pressed(self):
        pass

    def auto_generate_pressed(self):
        pass

    def add_question_pressed(self):
        pass

    def finish_quiz_pressed(self):
        pass

    def update_pressed(self):
        # dictionary to take the string from the dropdown box, and convert it to the string for the operator label
        self.operator_dict = {'Addition': '+',
                              'Subtraction': '-',
                              'Multiply': 'X',
                              'Inverse': '-1',
                              'Determinant': 'Det'}

        dropdown_string = self.q_operator_dropdown.currentText()
        # inverse and determinant will require the box to be moved
        if dropdown_string == 'Inverse':
            self.change_ui_to_inverse()

        elif dropdown_string == 'Determinant':
            # need to hide the right matrix
            self.change_ui_to_determinant()

        elif dropdown_string == 'Multiply' or dropdown_string == 'Subtraction' or dropdown_string == 'Addition':
            self.q_operator_label.setText(self.operator_dict[dropdown_string])
            # need to show the left matrix

    def change_ui_to_inverse(self):
        pass

    def change_ui_to_determinant(self):
        pass
