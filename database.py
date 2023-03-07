import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


def init_db():
    # TODO: pls format all the sql nicely lol
    # NOTE: no need to insert id's, they will autoincrement
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Users (id INTEGER NOT NULL UNIQUE, username TEXT NOT NULL, \
            password TEXT NOT NULL, PRIMARY KEY(id AUTOINCREMENT));"
    )

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Quizzes (id INTEGER NOT NULL UNIQUE, user_id INTEGER NOT NULL UNIQUE, \
            quiz_name TEXT NOT NULL, quiz_type TEXT NOT NULL, nr_questions INTEGER NOT NULL, \
                PRIMARY KEY(id AUTOINCREMENT), FOREIGN KEY (user_id) REFERENCES Users (id));"
    )

    # values stored as text, just use matrix.values when inserting
    # also can't name field values because it's a reserved keyword, so used vals
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Matrices (\
        id INTEGER NOT NULL UNIQUE,\
        size INTEGER NOT NULL,\
        vals TEXT NOT NULL,\
        PRIMARY KEY(id AUTOINCREMENT));"
    )

    # matrix2 can be null, eg for determinant
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Questions (id INTEGER NOT NULL UNIQUE, \
            quiz_id INTEGER NOT NULL UNIQUE, question_number INTEGER NOT NULL UNIQUE, matrix1_id INTEGER NOT NULL UNIQUE, \
                matrix2_id INTEGER UNIQUE, operator TEXT NOT NULL, \
                    PRIMARY KEY(id AUTOINCREMENT), FOREIGN KEY (quiz_id) REFERENCES Quizzes (id), \
                        FOREIGN KEY (matrix1_id) REFERENCES Matrices (id), FOREIGN KEY (matrix2_id) REFERENCES Matrices (id));"
    )


def insert_user(username, password):
    cursor.execute(
        "INSERT INTO Users (username, password) VALUES (?, ?)", (username, password)
    )


def insert_quiz(user_id, quiz_name, quiz_type, nr_questions):
    cursor.execute(
        "INSERT INTO Quizzes (user_id, quiz_name, quiz_type, nr_questions) VALUES (?, ?, ?, ?)",
        (user_id, quiz_name, quiz_type, nr_questions),
    )


def insert_matrix(size, vals):
    cursor.execute("INSERT INTO Matrices (size, vals) VALUES (?, ?)", (size, vals))


def insert_question(quiz_id, question_number, matrix1_id, matrix2_id, operator):
    cursor.execute(
        "INSERT INTO Questions (quiz_id, question_number, matrix1_id, matrix2_id, operator) VALUES (?, ?, ?, ?, ?)",
        (quiz_id, question_number, matrix1_id, matrix2_id, operator),
    )


def close_db():
    conn.commit()
    conn.close()
