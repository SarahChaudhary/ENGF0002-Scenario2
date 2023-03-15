from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
import numpy as np
from matrix import matrix_subtraction, matrix_addition, matrix_determinant, matrix_dot_product ,matrix_dot_product, matrix_inverse, matrix_multiplication

ui = uic.loadUiType('determinant_calculator.ui')[0]

'''
q_history_left -> widget {h1-h9}
q_history_right -> widget {h10-h18}
q_history_matrix_ans -> widget {h19-27}
q_history_single_ans -> lineedit
q_history_operator_label -> label
q_history_equals_label -> label

q_operator -> combobox
q_left_matrix -> widget {q1-q9}
q_right_matrix -> widget {q10-q18}
q_answer_matrix -> widget {q19-q27}
q_single_answer -> lineedit
q_operator_label -> label

q_update -> button
q_clear_history -> button
q_show_history -> button
q_calculate -> button
q_clear_matrices -> button

'''


class Calculator(QMainWindow, ui):
    def __init__(self, appwindow):
        super().__init__()
        self.setupUi(appwindow)

        self.q_update.clicked.connect(self.update_clicked)
        self.q_show_history.clicked.connect(self.show_history_clicked)
        self.q_clear_history.clicked.connect(self.hide_history_clicked)
        self.q_calculate.clicked.connect(self.calculate_clicked)
        self.q_clear_matrices.clicked.connect(self.clear_matrices)

        self.left_matrix = [
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
        self.right_matrix = [
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

        self.answer_matrix = [self.q19,
                              self.q20,
                              self.q21,
                              self.q22,
                              self.q23,
                              self.q24,
                              self.q25,
                              self.q26,
                              self.q27]

        self.history_left_matrix = [self.h1,
                                    self.h2,
                                    self.h3,
                                    self.h4,
                                    self.h5,
                                    self.h6,
                                    self.h7,
                                    self.h8,
                                    self.h9]

        self.history_right_matrix = [self.h10,
                                     self.h11,
                                     self.h12,
                                     self.h13,
                                     self.h14,
                                     self.h15,
                                     self.h16,
                                     self.h17,
                                     self.h18]

        self.history_matrix_ans = [self.h19,
                                   self.h20,
                                   self.h21,
                                   self.h22,
                                   self.h23,
                                   self.h24,
                                   self.h25,
                                   self.h26,
                                   self.h27]

        self.initialise_status()

    def initialise_status(self):
        self.history_bivariable = True
        self.bivariable = True

        self.q_single_answer.hide()
        self.q_history_single_ans.hide()

        for i in range(9):
            self.answer_matrix[i].setReadOnly(True)
            self.history_matrix_ans[i].setReadOnly(True)
            self.history_right_matrix[i].setReadOnly(True)
            self.history_left_matrix[i].setReadOnly(True)

    def clear_matrices(self):
        for i in range(9):
            self.left_matrix[i].setText("")
            self.right_matrix[i].setText("")
            self.answer_matrix[i].setText("")

    def calculate_clicked(self):
        self.update_clicked()
        operation = self.q_operator_label.text()
        self.answers = []

        # for testing perposes:
        self.answers = [1]

        if self.bivariable:
            self.left_values = [float(v.text()) for v in self.left_matrix]
            self.right_values = [float(v.text()) for v in self.right_matrix]

            if operation == "+":
                self.answers = matrix_addition(np.array(self.left_values.copy()).reshape(3,3), np.array(self.right_values.copy()).reshape(3,3))
            
                # call addition function
            elif operation == 'x':
                self.answers = matrix_multiplication(np.array(self.left_values.copy()).reshape(3,3), np.array(self.right_values.copy()).reshape(3,3))
            
                # call multiplication function
            elif operation == '-':
                self.answers = matrix_subtraction(np.array(self.left_values.copy()).reshape(3,3), np.array(self.right_values.copy()).reshape(3,3))
            
                # call subtraction function

        else:
            self.values = [float(v.text()) for v in self.right_matrix]

            if operation == 'Det':
                self.answers = matrix_determinant(np.array(self.values.copy()).reshape(3,3))
            
                # call determinant and have it return to the answer list

            elif operation == 'Inverse':
                self.answers = matrix_inverse(np.array(self.values.copy()).reshape(3,3))
                
                # call inverse function

        self.update_matrices()

    def update_matrices(self):
        single = True if len(self.answers) == 1 else False

        if self.bivariable:
            self.q_history_left_matrix.show()
            for i in range(9):
                self.history_left_matrix[i].setText(self.left_matrix[i].text())

        else:
            self.q_history_left_matrix.hide()

        for i in range(9):
            self.history_right_matrix[i].setText(self.right_matrix[i].text())

        # handle the 2 cases where there is either 1 answers or a matrix answer
        if not single:
            for i in range(9):
                self.history_matrix_ans[i].setText(str(self.answers[i]))
                self.answer_matrix[i].setText(str(self.answers[i]))
                self.q_history_single_ans.hide()
                self.q_single_answer.hide()
                self.q_answer_matrix.show()
                self.q_history_matrix_ans.show()

        if single:
            self.q_history_single_ans.setText(str(self.answers[0]))
            self.q_single_answer.setText(str(self.answers[0]))
            self.q_history_single_ans.show()
            self.q_single_answer.show()
            self.q_answer_matrix.hide()
            self.q_history_matrix_ans.hide()

        self.q_history_operator_label.setText(self.q_operator_label.text())

        # update the matrix values

    def hide_history_clicked(self):
        self.q_history_left_matrix.hide()
        self.q_history_right_matrix.hide()
        self.q_history_single_ans.hide()
        self.q_history_matrix_ans.hide()
        self.q_history_operator_label.hide()
        self.q_history_equals_label.hide()

    def show_history_clicked(self):
        # TODO: need to make it so only the elements needed to be shown are shown
        self.q_history_left_matrix.show()
        self.q_history_right_matrix.show()
        self.q_history_single_ans.show()
        self.q_history_matrix_ans.show()
        self.q_history_operator_label.show()
        self.q_history_equals_label.show()

    def update_clicked(self):
        # dictionary to take the string from the dropdown box, and convert it to the string for the operator label
        self.operator_dict = {
            "Addition": "+",
            "Subtraction": "-",
            "Multiplication": "x",
            "Inversion": "Inverse",
            "Determinant": "Det",
        }

        dropdown_string = self.q_operator_dropdown.currentText()
        self.q_operator_label.setText(self.operator_dict[dropdown_string])

        if dropdown_string == "Inversion":
            self.bivariable = False
            self.q_left_matrix.hide()

        elif dropdown_string == "Determinant":
            self.bivariable = False
            self.q_left_matrix.hide()

        elif (
                dropdown_string == "Multiplication"
                or dropdown_string == "Subtraction"
                or dropdown_string == "Addition"
        ):
            self.q_left_matrix.show()
            self.bivariable = True
