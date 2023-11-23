# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

# import sys


# class AnotherWindow(QWidget):
#     """
#     This "window" is a QWidget. If it has no parent, it
#     will appear as a free-floating window as we want.
#     """
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.label = QLabel("Another Window")
#         layout.addWidget(self.label)
#         self.setLayout(layout)


# class MainWindow(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.button = QPushButton("Push for Window")
#         self.button.clicked.connect(self.show_new_window)
#         self.setCentralWidget(self.button)

#     def show_new_window(self, checked):
#         self.w = AnotherWindow()
#         self.w.show()


# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# app.exec()


# ======================================================--------------------------------000000000000000000000

# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

# import sys

# from random import randint


# class AnotherWindow(QWidget):
#     """
#     This "window" is a QWidget. If it has no parent, it
#     will appear as a free-floating window as we want.
#     """
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.label = QLabel("Another Window % d" % randint(0,100))
#         layout.addWidget(self.label)
#         self.setLayout(layout)


# class MainWindow(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.w = None  # No external window yet.
#         self.button = QPushButton("Push for Window")
#         self.button.clicked.connect(self.show_new_window)
#         self.setCentralWidget(self.button)

#     # def show_new_window(self, checked):
#     #     if self.w is None:
#     #         self.w = AnotherWindow()
#     #     self.w.show()
# # ------------------------------------------------------------------------
#     # def show_new_window(self, checked):
#     #     if self.w is None:
#     #         self.w = AnotherWindow()
#     #         self.w.show()

#     #     else:
#     #         self.w = None  


# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# app.exec()

# ======================================================--------------------------------000000000000000000000

# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

# import sys

# from random import randint


# class AnotherWindow(QWidget):
#     """
#     This "window" is a QWidget. If it has no parent, it
#     will appear as a free-floating window as we want.
#     """
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.label = QLabel("Another Window % d" % randint(0,100))
#         layout.addWidget(self.label)
#         self.setLayout(layout)


# class MainWindow(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.w = None  # No external window yet.
#         self.button = QPushButton("Push for Window")
#         self.button.clicked.connect(self.show_new_window)
#         self.setCentralWidget(self.button)

#     def show_new_window(self, checked):
#         if self.w is None:
#             self.w = AnotherWindow()
#             self.w.show()

#         else:
#             self.w.close()  # Close window.
#             self.w = None  # Discard reference.


# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# app.exec()

# ===============================================================================================================

# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

# import sys

# from random import randint


# class AnotherWindow(QWidget):
#     """
#     This "window" is a QWidget. If it has no parent, it
#     will appear as a free-floating window as we want.
#     """
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.label = QLabel("Another Window % d" % randint(0,100))
#         layout.addWidget(self.label)
#         self.setLayout(layout)


# class MainWindow(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.w = AnotherWindow()
#         self.button = QPushButton("Push for Window")
#         self.button.clicked.connect(self.show_new_window)
#         self.setCentralWidget(self.button)

#     def show_new_window(self, checked):
#         self.w.show()


# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# app.exec()

# =======================  Toggle window hide and show -----------------------------------=======================================--------------------

# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

# import sys

# from random import randint


# class AnotherWindow(QWidget):
#     """
#     This "window" is a QWidget. If it has no parent, it
#     will appear as a free-floating window as we want.
#     """
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.label = QLabel("Another Window % d" % randint(0,100))
#         layout.addWidget(self.label)
#         self.setLayout(layout)


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.w = AnotherWindow()
#         self.button = QPushButton("Push for Window")
#         self.button.clicked.connect(self.toggle_window)
#         self.setCentralWidget(self.button)

#     def toggle_window(self, checked):
#         if self.w.isVisible():
#             self.w.hide()

#         else:
#             self.w.show()


# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# app.exec()

# =========== Multiple Window Show ============================================////////////////////////////////////////////////=================

# import sys
# from random import randint

# from PyQt5.QtWidgets import (
#     QApplication,
#     QLabel,
#     QMainWindow,
#     QPushButton,
#     QVBoxLayout,
#     QWidget,
# )


# class AnotherWindow(QWidget):
#     """
#     This "window" is a QWidget. If it has no parent,
#     it will appear as a free-floating window.
#     """

#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.label = QLabel("Another Window % d" % randint(0, 100))
#         layout.addWidget(self.label)
#         self.setLayout(layout)


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.window1 = AnotherWindow()
#         self.window2 = AnotherWindow()

#         l = QVBoxLayout()
#         button1 = QPushButton("Push for Window 1")
#         button1.clicked.connect(self.toggle_window1)
#         l.addWidget(button1)

#         button2 = QPushButton("Push for Window 2")
#         button2.clicked.connect(self.toggle_window2)
#         l.addWidget(button2)

#         w = QWidget()
#         w.setLayout(l)
#         self.setCentralWidget(w)

#     def toggle_window1(self, checked):
#         if self.window1.isVisible():
#             self.window1.hide()

#         else:
#             self.window1.show()

#     def toggle_window2(self, checked):
#         if self.window2.isVisible():
#             self.window2.hide()

#         else:
#             self.window2.show()


# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# app.exec()

# ++++++++++++++++++++++++++++++++= Multiple Window Function =++++++++++++++++++++++++++++++++++++++++

import sys
from random import randint

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent,
    it will appear as a free-floating window.
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window1 = AnotherWindow()
        self.window2 = AnotherWindow()

        l = QVBoxLayout()
        button1 = QPushButton("Push for Window 1")
        button1.clicked.connect(
            lambda checked: self.toggle_window(self.window1)
        )
        l.addWidget(button1)

        button2 = QPushButton("Push for Window 2")
        button2.clicked.connect(
            lambda checked: self.toggle_window(self.window2)
        )
        l.addWidget(button2)

        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()