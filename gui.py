import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QLineEdit,QPushButton,QVBoxLayout,QWidget,QTableWidget,QTableWidgetItem,QMessageBox
import sqlite3

from db import add_book


class LibManSys(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library Management System")
        self.setGeometry(100, 100, 800, 600)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.title_label = QLabel("Library Management System",self)
        layout.addWidget(self.title_label)

        self.book_title_input = QLineEdit(self)
        self.book_title_input.setPlaceholderText("Enter Book Title:")
        self.book_title_input.setFixedSize(150, 30)
        layout.addWidget(self.book_title_input)

        self.book_author_input = QLineEdit(self)
        self.book_author_input.setPlaceholderText("Enter Book Author:")
        layout.addWidget(self.book_author_input)

        self.book_copies_input = QLineEdit(self)
        self.book_copies_input.setPlaceholderText("Enter Number of Copies:")
        layout.addWidget(self.book_copies_input)

        self.add_book_button = QPushButton("Add Book", self)
        self.add_book_button.setFixedSize(100,40)
        self.add_book_button.clicked.connect(self.add_book)
        layout.addWidget(self.add_book_button)

        self.view_book_button = QPushButton("View Book", self)
        self.view_book_button.setFixedSize(100, 40)
        self.view_book_button.clicked.connect(self.view_books)
        layout.addWidget(self.view_book_button)

        self.books_table = QTableWidget(self)
        self.books_table.setColumnCount(3)
        self.books_table.setHorizontalHeaderLabels(["ID", "Title", "Author", "Copies"])
        layout.addWidget(self.books_table)

        main_widget = QWidget(self)
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def add_book(self):
        title = self.book_title_input.text()
        author = self.book_author_input.text()
        copies = self.book_copies_input.text()

        if title and author and copies.isdigit():
            conn = sqlite3.connect('library.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO books (title, author, copies) VALUES (?, ?, ?)', (title, author, copies))
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Success", f"Book '{title}' added!")
            self.book_title_input.clear()
            self.book_author_input.clear()
            self.book_copies_input.clear()
        else:
            QMessageBox.warning(self, "Error", "Please enter valid information for the book.")

    # View Books in the table
    def view_books(self):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
        conn.close()

        self.books_table.setRowCount(0)

        for row_number, row_data in enumerate(books):
            self.books_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.books_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LibManSys()
    window.show()
    sys.exit(app.exec_())








