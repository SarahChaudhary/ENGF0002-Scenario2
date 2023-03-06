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
q_left_matrix -> widget containing left matrix
q_operator_label -> QLabel
'''


class CreateQuestion(QMainWindow, ui):
    def __init__(self, appwindow):
        super().__init__()
        self.setupUi(appwindow)

        # this is the 9 matrix input spaces (QLineEdit) collated into a list [QLineEdit]
        self.left_matrix_values = [self.q1,
                                   self.q2,
                                   self.q3,
                                   self.q4,
                                   self.q5,
                                   self.q6,
                                   self.q7,
                                   self.q8,
                                   self.q9]

        # same as above but for the second matrix
        self.right_matrix_values = [self.q10,
                                    self.q11,
                                    self.q12,
                                    self.q13,
                                    self.q14,
                                    self.q15,
                                    self.q16,
                                    self.q17,
                                    self.q18]

        # QLine objects that make up the left matrix's brackets

        self.q_check_valid.clicked.connect(self.check_valid_pressed)
        self.q_auto_generate.clicked.connect(self.auto_generate_pressed)
        self.q_add_question.clicked.connect(self.add_question_pressed)
        self.q_finish_quiz.clicked.connect(self.finish_quiz_pressed)
        self.q_update.clicked.connect(self.update_pressed)

    # these methods below will be called when the corresponding buttons are clicked
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
                              'Multiply': 'x',
                              'Inverse': '-1',
                              'Determinant': 'Det'}

        dropdown_string = self.q_operator_dropdown.currentText()
        self.q_operator_label.setText(self.operator_dict[dropdown_string])

        if dropdown_string == 'Inverse':
            self.q_left_matrix.hide()
            self.q_right_matrix.move(230, 190)
            self.q_operator_label.move(275, 0)


        elif dropdown_string == 'Determinant':
            self.q_left_matrix.hide()
            self.q_right_matrix.move(230, 190)
            self.q_operator_label.move(0, 90)

        elif dropdown_string == 'Multiply' or dropdown_string == 'Subtraction' or dropdown_string == 'Addition':
            # x = self.q_right_matrix.x()
            # y = self.q_right_matrix.y()
            # print(x, y)
            self.q_right_matrix.move(350, 190)
            self.q_operator_label.move(0, 90)
            self.q_left_matrix.show()
            # need to show the left matrix
