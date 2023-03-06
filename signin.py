from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

ui = uic.loadUiType("signin.ui")[0]

'''
q_username

q_create_account -> QWidget {
    q_make_password -> QLineEdit
    q_repeat_password -> QLineEdit
    q_create_account_button -> QPushButton
}
q_signin -> QWidget {
    q_password -> QLineEdit
    q_signin_button -> QPushButton
    q_dont_have_account -> QPushButton
}
'''


class Signin(QMainWindow, ui):
    def __init__(self, appwindow):
        super().__init__()
        self.setupUi(appwindow)

        # hide the create account part of it unless they click don't have account
        self.q_create_account.hide()
        self.q_dont_have_account.clicked.connect(self.create_account)
        self.q_create_account_button.clicked.connect(self.create_account_clicked)
        # TODO need to add a show password button, and have by default ...... instead of password in the password field

    def create_account(self):
        self.q_signin.hide()
        self.q_create_account.show()

    def create_account_clicked(self):
        valid = True
        # TODO add account validation in here
        if valid:
            print('here')
            # TODO add account details to database
            self.q_create_account.hide()
            self.q_signin.show()



