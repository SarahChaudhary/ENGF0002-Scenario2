import sys
from PyQt5.QtWidgets import QApplication
from app import App


# print errors into command line
def my_exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    # sys.exit(1)


sys.excepthook = my_exception_hook


def main():
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

# TODO: add a file for all the different matrix operations. make it a class so it can be imported,
# TODO: basically wrap the numpy functions but make it return normal arrays and have the parameters being normal arrays

# TODO: (ben) add a page where the user can either make a quiz, do a quiz or enter calculator
# TODO: (ben) need to have another file to hold temp user data like name and id
