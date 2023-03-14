from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

ui = uic.loadUiType('determinant_calculator.ui')[0]

'''
q_history_left -> widget {h1-h9}
q_history_right -> widget {h10-h18}
q_history_matrix_ans -> widget {h19-27}
q_history_single_ans -> lineedit
q_history_operator_label -> label

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

'''


class Calculator(QMainWindow, ui):
    def __init__(self, appwindow):
        super().__init__()
        self.setupUi(appwindow)
        self.history_bivariable = True
        self.bivariable = True

        self.q_single_answer.hide()
        self.q_history_single_ans.hide()
        self.q_update.clicked.connect(self.update_clicked)
        self.q_show_history.clicked.connect(self.show_history_clicked)
        self.q_clear_history.clicked.connect(self.hide_history_clicked)
        self.q_calculate.clicked.connect(self.calculate_clicked)

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

    def calculate_clicked(self):
        operation = self.q_operator_label.text()
        self.answers = []

        # for testing perposes:
        self.answers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        if self.bivariable:
            self.left_values = [v.text() for v in self.left_matrix]
            self.right_values = [v.text() for v in self.right_matrix]

            if operation == "+":
                pass
                # call addition function
            elif operation == 'x':
                pass
                # call multiplication function
            elif operation == '-':
                pass
                # call subtraction function

        else:
            self.values = [v.text() for v in self.right_matrix]

            if operation == 'det':
                pass
                # call determinant and have it return to the answer list

            elif operation == '-1':
                pass
                # call inverse function

        self.update_history()

    def update_history(self):
        if self.bivariable:
            self.q_history_left_matrix.show()
            for i in range(9):
                self.history_left_matrix[i].setText(self.left_matrix[i].text())

        else:
            self.q_history_left_matrix.hide()

        for i in range(9):
            self.history_right_matrix[i].setText(self.right_matrix[i].text())
            self.history_matrix_ans[i].setText(str(self.answers[i]))

        self.q_history_operator_label.setText(self.q_operator_label.text())



        # update the matrix values

    def hide_history_clicked(self):
        self.q_history_left.hide()
        self.q_history_right.hide()
        self.q_history_single_ans.hide()
        self.q_history_matrix_ans.hide()

    def show_history_clicked(self):
        self.q_history_left.show()
        self.q_history_right.show()
        self.q_history_single_ans.show()
        self.q_history_matrix_ans.show()

    def update_clicked(self):
        # dictionary to take the string from the dropdown box, and convert it to the string for the operator label
        self.operator_dict = {
            "Addition": "+",
            "Subtraction": "-",
            "Multiplication": "x",
            "Inversion": "-1",
            "Determinant": "Det",
        }

        dropdown_string = self.q_operator_dropdown.currentText()
        self.q_operator_label.setText(self.operator_dict[dropdown_string])

        if dropdown_string == "Inverse":
            self.q_left_matrix.hide()

        elif dropdown_string == "Determinant":
            self.q_left_matrix.hide()

        elif (
                dropdown_string == "Multiply"
                or dropdown_string == "Subtraction"
                or dropdown_string == "Addition"
        ):
            self.q_left_matrix.show()