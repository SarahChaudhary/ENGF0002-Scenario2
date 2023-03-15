from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5 import uic
import database
import hashlib

ui = uic.loadUiType("signin.ui")[0]

'''
q_title -> QLabel
q_username -> QLineEdit
q_show_password -> QRadioButton

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
# for some reason current_user is not being updated, so use list instead (kinda dirty but works)
# current_user = ""
# current = []
current = ["test1"] #TODO: HARDCODED, remove once validation is turned on

class Signin(QMainWindow, ui):
    def __init__(self, appwindow):
        super().__init__()
        self.setupUi(appwindow)

        self.hide_passwords()

        self.q_create_account.hide()
        self.q_dont_have_account.clicked.connect(self.create_account)
        self.q_create_account_button.clicked.connect(self.create_account_clicked)
        self.q_show_password.pressed.connect(self.show_password_pressed)
        self.q_show_password.released.connect(self.show_password_released)
        self.q_signin_button.clicked.connect(self.signin_button_clicked)

    def show_password_pressed(self):
        print('here')
        self.q_password.setEchoMode(QLineEdit.Normal)
        self.q_make_password.setEchoMode(QLineEdit.Normal)
        self.q_repeat_password.setEchoMode(QLineEdit.Normal)

    def show_password_released(self):
        print('here')
        self.hide_passwords()

    def hide_passwords(self):
        self.q_password.setEchoMode(QLineEdit.Password)
        self.q_make_password.setEchoMode(QLineEdit.Password)
        self.q_repeat_password.setEchoMode(QLineEdit.Password)

    def create_account(self):
        self.q_signin.hide()
        self.q_create_account.show()
        self.q_title.setText('Create Account')

    def validate_signin(self, usr, p1, p2):
        if database.is_user_in_db(usr):
            return False
        if usr == '' or p1 == '':
            return False
        if p1 != p2:
            return False
        if len(p1) < 3: # TODO: change this to 8 once testing is done (or never lol, they won't know)
            return False
        # if p1 == p1.casefold() or p1 == p1.upper():
        #     return False
        # # check if it contains a special character (!, @, #, $, %, *, &, ?)
        # if not any(char in p1 for char in ['!', '@', '#', '$', '%', '*', '&', '?']):
        #     return False

        return True
    
    def create_account_clicked(self):
        print('hi')
        username = self.q_username.text()
        password1 = self.q_make_password.text()
        password2 = self.q_repeat_password.text()

        if self.validate_signin(username, password1, password2):
            hashed_password = hashlib.sha256(password1.encode()).hexdigest()
            database.insert_user(username, hashed_password)
            print("inserted")
            self.q_create_account.hide()
            self.q_signin.show()
            self.q_title.setText('Sign In')


    def signin_button_clicked(self):
        self.valid = False
        password = self.q_password.text()
        print(password)
        username = self.q_username.text()
        if database.is_user_in_db(username):
            db_pass = database.get_pass(username)
            print(db_pass)
            print(hash(password))
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if db_pass == hashed_password:
                self.valid = True
                current.append(username)
                # current_user = username
                print('correct')
            else:
                self.valid = False
                print('incorrect')

        # for testing purposes
        self.valid = True
        
    def get_username(self):
        return self.q_username.text()

        # TODO (ben) ill add an error popup later once the above feature is implemented

