import sys
import typing
from PyQt5.QtCore import QSize, Qt
from random import choice
from PyQt5.QtGui import QPixmap, QPalette, QColor, QIcon, QKeySequence
from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QCheckBox,
    QAction,
    QDialog,
    QMenu,
    QComboBox,
    QToolBar,
    QLineEdit,
    QTabWidget,
    QDateEdit,
    QStatusBar,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QSlider,
    QSpinBox,
    QLCDNumber,
    QMainWindow,
    QDialogButtonBox,
    QGridLayout,
    QProgressBar,
    QRadioButton,
    QStackedLayout,
    QSpinBox,
    QTimeEdit,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
)
# This is not a main class, its only for color layouts
class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

# window_titles = ['My App',
#                 'My App',
#                 'Still My App',
#                 'Still My App',
#                 'What on earth',
#                 'What on earth',
#                 'This is surprising',
#                 'This is surprising',
#                 'Something went wrong']

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Widgets App")

#/////////////////////////////////////////////////////////////////////////////////////////////////

    #     self.setWindowTitle("My App")

    #     self.button = QPushButton("Press Me!")
    #     self.button.clicked.connect(self.the_button_was_clicked)

    #     self.setCentralWidget(self.button)

    # def the_button_was_clicked(self):
    #     self.button.setText("You already clicked me.")
    #     self.button.setEnabled(False)

        # Also change the window title.
        # self.setWindowTitle("My Oneshot App")

 #/////////////////////////////////////////////////////////////////////////////////////////////////       

        # self.button_is_checked = False
        # self.setWindowTitle("APP")
        # self.button = QPushButton("Click here")
    #     self.button.setCheckable(True)
    #     # self.button.clicked.connect(self.button_clicked)
    #     # button.clicked.connect(self.button_toggle)
    #     self.button.released.connect(self.button_was_released)
    #     self.button.setChecked(self.button_is_checked)

    #     self.setMinimumSize(QSize(400, 300))
    #     self.setCentralWidget(self.button)

    # def button_was_released(self):
    #     self.button_checked = self.button.isChecked()
    #     print(self.button_checked)

    # def button_clicked(self):
    #     self.button.setText("button is already clicked")
    #     self.button.setEnabled(False)

    #     self.setWindowTitle("One Way Shot")
    # def button_toggle(self, checked):
    #     self.button_clicked = checked
    #     print(self.button_clicked)

#/////////////////////////////////////////////////////////////////////////////////////////////////


    #     self.n_times_clicked = 0

    #     self.setWindowTitle("My App")

    #     self.button = QPushButton("Press Me!")
    #     self.button.clicked.connect(self.the_button_was_clicked)

    #     self.windowTitleChanged.connect(self.the_window_title_changed)

    #     # Set the central widget of the Window.
    #     self.setCentralWidget(self.button)

    # def the_button_was_clicked(self):
    #     print("Clicked.")
    #     new_window_title = choice(window_titles)
    #     print("Setting title:  %s" % new_window_title)
    #     self.setWindowTitle(new_window_title)

    # def the_window_title_changed(self, window_title):
    #     print("Window title changed: %s" % window_title)

    #     if window_title == 'Something went wrong':
    #         self.button.setDisabled(True)

#/////////////////////////////////////////////////////////////////////////////////////////////////

        # self.setWindowTitle("My App")

        # self.label = QLabel()

        # self.input = QLineEdit()
        # self.input.textChanged.connect(self.label.setText)

        # layout = QVBoxLayout()
        # layout.addWidget(self.input)
        # layout.addWidget(self.label)

        # container = QWidget()
        # container.setLayout(layout)

        # # Set the central widget of the Window.
        # self.setCentralWidget(container)

#/////////////////////////////////////////////////////////////////////////////////////////////////


    #     self.label = QLabel("Cick in this windows")
    #     self.setCentralWidget(self.label)

    # def mouseMoveEvent(self, e):
    #     self.label.setText("mouseMoveEvent")

    # def mouseDoubleClickEvent(self, e):
    #     self.label.setText('mouseDoubleClickEvent')

    # def mousePressEvent(self,e) :
    #     self.label.setText("mousePressEvent")

    # def mouseReleaseEvent(self, e):
    #     self.label.setText("mouseReleaseEvent")


#/////////////////////////////////////////////////////////////////////////////////////////////////

    # def mousePressEvent(self, e):
    #     if e.button() == Qt.LeftButton:
    #         # handle the left-button press in here
    #         self.label.setText("mousePressEvent LEFT")

    #     elif e.button() == Qt.MiddleButton:
    #         # handle the middle-button press in here.
    #         self.label.setText("mousePressEvent MIDDLE")

    #     elif e.button() == Qt.RightButton:
    #         # handle the right-button press in here.
    #         self.label.setText("mousePressEvent RIGHT")

    # def mouseDoubleClickEvent(self, e):
    #     if e.button() == Qt.LeftButton:
    #         # handle the left-button press in here
    #         self.label.setText("mouseDoubleClickEvent LEFT")

    #     elif e.button() == Qt.MiddleButton:
    #         # handle the middle-button press in here.
    #         self.label.setText("mouseDoubleClickEvent MIDDLE")

    #     elif e.button() == Qt.RightButton:
    #         # handle the right-button press in here.
    #         self.label.setText("mouseDoubleClickEvent RIGHT")

    # def mouseReleaseEvent(self, e):
    #     if e.button() == Qt.LeftButton:
    #         # handle the left-button press in here
    #         self.label.setText("mouseReleaseEvent LEFT")

    #     elif e.button() == Qt.MiddleButton:
    #         # handle the middle-button press in here.
    #         self.label.setText("mouseReleaseEvent MIDDLE")

    #     elif e.button() == Qt.RightButton:
    #         # handle the right-button press in here.
    #         self.label.setText("mouseReleaseEvent RIGHT")

    # def mouseMoveEvent(self, e):
    #     if e.button() == Qt.LeftButton:
    #         # handle the left-button press in here
    #         self.label.setText("mouseMoveEvent LEFT")

    #     elif e.button() == Qt.MiddleButton:
    #         # handle the middle-button press in here.
    #         self.label.setText("mouseMoveEvent MIDDLE")

    #     elif e.button() == Qt.RightButton:
    #         # handle the right-button press in here.
    #         self.label.setText("mouseMoveEvent RIGHT")

#/////////////////////////////////////////////////////////////////////////////////////////////////

    # def contextMenuEvent(self, e):
    #     context = QMenu(self)

    #     context.addAction(QAction("test 1", self))
    #     context.addAction(QAction("test 2", self))
    #     context.addAction(QAction("test 3", self))
    #     context.exec(e.globalPos())

#/////////////////////////////////////////////////////////////////////////////////////////////////

    #     self.show()
        
    #     self.setContextMenuPolicy(Qt.CustomContextMenu)
    #     self.customContextMenuRequested.connect(self.on_context_menu)

    # def on_context_menu(self,pos):
    #     context = QMenu(self)
    #     context.addAction(QAction("test 1", self))
    #     context.addAction(QAction("test 2", self))
    #     context.addAction(QAction("test 3", self))
    #     context.exec(self.mapToGlobal(pos))

#/////////////////////////////////////////////////////////////////////////////////////////////////
        # layout = QVBoxLayout()
        # widgets = [
        #     QCheckBox,
        #     QComboBox,
        #     QDateEdit,
        #     QDateTimeEdit,
        #     QDial,
        #     QDoubleSpinBox,
        #     QFontComboBox,
        #     QLCDNumber,
        #     QLabel,
        #     QLineEdit,
        #     QProgressBar,
        #     QPushButton,
        #     QRadioButton,
        #     QSlider,
        #     QSpinBox,
        #     QTimeEdit,
        # ]

        # for w in widgets:
        #     layout.addWidget(w())

        # widget = QWidget()
        # widget.setLayout(layout)
        # self.setCentralWidget(widget)

#///////////////////////////////////////////////////////////////////////////////////////////////// QLabel()

        # widget = QLabel("100")
        # widget.setPixmap(QPixmap('Data_Analyzer.png'))
        # widget.setScaledContents(True)
        # # widget.setText("2")
        # font = widget.font()
        # font.setPointSize(30)
        # widget.setFont(font)
        # widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # self.setCentralWidget(widget)

#///////////////////////////////////////////////////////////////////////////////////////////////// QCheckBox()

    #     widget = QCheckBox()
    #     widget.setCheckState(Qt.Checked)

    #     # For tristate: widget.setCheckState(Qt.PartiallyChecked)
    #     # Or: widget.setTriState(True)
    #     widget.stateChanged.connect(self.show_state)

    #     self.setCentralWidget(widget)

    # def show_state(self, s):
    #     print(s == Qt.Checked)
        # print(s)

#///////////////////////////////////////////////////////////////////////////////////////////////// QComboBox()

    #     widget = QComboBox()
    #     widget.addItems(["One", "Two", "Three"])
    #     widget.setEditable(True)

    #     # Sends the current index (position) of the selected item.
    #     widget.currentIndexChanged.connect( self.index_changed )

    #     # There is an alternate signal to send the text.
    #     widget.currentTextChanged.connect( self.text_changed )

    #     self.setCentralWidget(widget)

    # def index_changed(self, i): # i is an int
    #     print(i)

    # def text_changed(self, s): # s is a str
    #     print(s)


#///////////////////////////////////////////////////////////////////////////////////////////////// QListWidget()

    #     widget = QListWidget()
    #     widget.addItems(["One", "Two", "Three"])

    #     widget.currentItemChanged.connect(self.index_changed)
    #     widget.currentTextChanged.connect(self.text_changed)

    #     self.setCentralWidget(widget)

    # def index_changed(self, i): # Not an index, i is a QListWidgetItem
    #     print(i.text())

    # def text_changed(self, s): # s is a str
    #     print(s)

#///////////////////////////////////////////////////////////////////////////////////////////////// QLineEdit()

    #     widget = QLineEdit()
    #     widget.setMaxLength(10)
    #     widget.setInputMask('000.000.000.000;_')
    #     widget.setPlaceholderText("Enter your text")

    #     #widget.setReadOnly(True) # uncomment this to make it read-only

    #     widget.returnPressed.connect(self.return_pressed)
    #     widget.selectionChanged.connect(self.selection_changed)
    #     widget.textChanged.connect(self.text_changed)
    #     widget.textEdited.connect(self.text_edited)

    #     self.setCentralWidget(widget)

    # def return_pressed(self):
    #     print("Return pressed!")
    #     self.centralWidget().setText("BOOM!")

    # def selection_changed(self):
    #     print("Selection changed")
    #     print(self.centralWidget().selectedText())

    # def text_changed(self, s):
    #     print("Text changed...")
    #     print(s)

    # def text_edited(self, s):
    #     print("Text edited...")
    #     print(s)

#///////////////////////////////////////////////////////////////////////////////////////////////// QSpinBox and QDoubleSpinBox()

        # widget = QSpinBox()
    #     widget = QDoubleSpinBox()

    #     # widget.setMinimum(-10)
    #     # widget.setMaximum(3)
    #     widget.setRange(-10,3)

    #     widget.setPrefix("$")
    #     widget.setSuffix("c")
    #     widget.setSingleStep(3)  # Or e.g. 0.5 for QDoubleSpinBox
    #     widget.valueChanged.connect(self.value_changed)
    #     widget.textChanged.connect(self.value_changed_str)

    #     self.setCentralWidget(widget)

    # def value_changed(self, i):
    #     print(i)

    # def value_changed_str(self, s):
    #     print(s)


#///////////////////////////////////////////////////////////////////////////////////////////////// QSlider()

    #     widget = QSlider()

    #     widget.setMinimum(-10)
    #     widget.setMaximum(3)
    #     # Or: widget.setRange(-10,3)

    #     widget.setSingleStep(3)

    #     widget.valueChanged.connect(self.value_changed)
    #     widget.sliderMoved.connect(self.slider_position)
    #     widget.sliderPressed.connect(self.slider_pressed)
    #     widget.sliderReleased.connect(self.slider_released)

    #     self.setCentralWidget(widget)

    # def value_changed(self, i):
    #     print(i)

    # def slider_position(self, p):
    #     print("position", p)

    # def slider_pressed(self):
    #     print("Pressed!")

    # def slider_released(self):
    #     print("Released")


#///////////////////////////////////////////////////////////////////////////////////////////////// QDial() Error in this  code

    #     widget = QDial()
    #     widget.setRange(-10, 100)
    #     widget.setSingleStep(0.9)

    #     widget.valueChanged.connect(self.value_changed)
    #     widget.sliderMoved.connect(self.slider_position)
    #     widget.sliderPressed.connect(self.slider_pressed)
    #     widget.sliderReleased.connect(self.slider_released)

    #     self.setCentralWidget(widget)

    # def value_changed(self, i):
    #     print(i)

    # def slider_position(self, p):
    #     print("position", p)

    # def slider_pressed(self):
    #     print("Pressed!")

    # def slider_released(self):
    #     print("Released")

#///////////////////////////////////////////////////////////////////////////////////////////////// Layout()

        # widget = Color('red')
        # self.setCentralWidget(widget)

        # layout = QVBoxLayout()

        # layout.addWidget(Color('red'))

        # widget = QWidget()
        # widget.setLayout(layout)
        # self.setCentralWidget(widget)

        # layout = QHBoxLayout()
        # # layout = QVBoxLayout()
        # layout.addWidget(Color('orange'))
        # layout.addWidget(Color('white'))
        # layout.addWidget(Color('green'))

        # widget = QWidget()
        # widget.setLayout(layout)
        # self.setCentralWidget(widget)

#///////////////////////////////////////////////////////////////////////////////////////////////// Nesting layouts()

        # layout1 = QHBoxLayout()
        # layout2 = QVBoxLayout()
        # layout3 = QVBoxLayout()

        # layout1.setContentsMargins(0,0,0,0)
        # layout1.setSpacing(0)

        # layout2.addWidget(Color('orenge'))
        # layout2.addWidget(Color('white'))
        # layout2.addWidget(Color('green'))

        # layout1.addLayout( layout2 )

        # layout1.addWidget(Color('blue'))

        # layout3.addWidget(Color('black'))
        # layout3.addWidget(Color('purple'))

        # layout1.addLayout( layout3 )

        # widget = QWidget()
        # widget.setLayout(layout1)
        # self.setCentralWidget(widget)

#///////////////////////////////////////////////////////////////////////////////////////////////// GridLayout()

        # layout = QGridLayout()
        # layout.addWidget(Color('red'), 0, 0)
        # layout.addWidget(Color('green'), 1, 0)
        # layout.addWidget(Color('blue'), 1, 1)
        # layout.addWidget(Color('purple'), 2, 1)

        # widget = QWidget()
        # widget.setLayout(layout)
        # self.setCentralWidget(widget)

#///////////////////////////////////////////////////////////////////////////////////////////////// QStackedLayout()

        # layout = QStackedLayout()

        # layout.addWidget(Color("red"))
        # layout.addWidget(Color("green"))
        # layout.addWidget(Color("blue"))
        # layout.addWidget(Color("yellow"))

        # layout.setCurrentIndex(3)

        # widget = QWidget()
        # widget.setLayout(layout)
        # self.setCentralWidget(widget)

#///////////////////////////////////////////////////////////////////////////////////////////////// click Color change

    #     pagelayout = QVBoxLayout()
    #     button_layout = QHBoxLayout()
    #     self.stacklayout = QStackedLayout()

    #     pagelayout.addLayout(button_layout)
    #     pagelayout.addLayout(self.stacklayout)

    #     btn = QPushButton("red")
    #     btn.pressed.connect(self.activate_tab_1)
    #     button_layout.addWidget(btn)
    #     self.stacklayout.addWidget(Color("red"))

    #     btn = QPushButton("green")
    #     btn.pressed.connect(self.activate_tab_2)
    #     button_layout.addWidget(btn)
    #     self.stacklayout.addWidget(Color("green"))

    #     btn = QPushButton("yellow")
    #     btn.pressed.connect(self.activate_tab_3)
    #     button_layout.addWidget(btn)
    #     self.stacklayout.addWidget(Color("yellow"))

    #     widget = QWidget()
    #     widget.setLayout(pagelayout)
    #     self.setCentralWidget(widget)

    # def activate_tab_1(self):
    #     self.stacklayout.setCurrentIndex(0)

    # def activate_tab_2(self):
    #     self.stacklayout.setCurrentIndex(1)

    # def activate_tab_3(self):
    #     self.stacklayout.setCurrentIndex(2)

#///////////////////////////////////////////////////////////////////////////////////////////////// TabWidget()


        # tabs = QTabWidget()
        # tabs.setTabPosition(QTabWidget.West)
        # tabs.setMovable(True)

        # for n, color in enumerate(["red", "green", "blue", "yellow"]):
        #     tabs.addTab(Color(color), color)

        # self.setCentralWidget(tabs)

#///////////////////////////////////////////////////////////////////////////////////////////////// Tool Bar menu


    #     label = QLabel("Hello!")
    #     label.setAlignment(Qt.AlignCenter)

    #     self.setCentralWidget(label)

    #     toolbar = QToolBar("My main toolbar")   
    #     self.addToolBar(toolbar)
    #     button_action = QAction("Your button", self)
    #     button_action.setStatusTip("This is your button")
    #     button_action.triggered.connect(self.onMyToolBarButtonClick)
    #     toolbar.addAction(button_action)

    #     self.setStatusBar(QStatusBar(self))


    # def onMyToolBarButtonClick(self, s):
    #     print("click", s)

#///////////////////////////////////////////////////////////////////////////////////////////////// Tougle menu button

    #     label = QLabel("Hello!")
    #     label.setAlignment(Qt.AlignCenter)

    #     self.setCentralWidget(label)

    #     toolbar = QToolBar("My main toolbar")
    #     self.addToolBar(toolbar)

    #     button_action = QAction("Your button", self)
    #     button_action.setStatusTip("This is your button")
    #     button_action.triggered.connect(self.onMyToolBarButtonClick)
    #     button_action.setCheckable(True)
    #     toolbar.addAction(button_action)

    #     self.setStatusBar(QStatusBar(self))

    # def onMyToolBarButtonClick(self, s):
    #     print("click", s)


#///////////////////////////////////////////////////////////////////////////////////////////////// Tougle menu button with logo

    #     label = QLabel("Hello!")
    #     label.setAlignment(Qt.AlignCenter)

    #     self.setCentralWidget(label)

    #     toolbar = QToolBar("My main toolbar")
    #     toolbar.setIconSize(QSize(16,16))
    #     self.addToolBar(toolbar)

    #     button_action = QAction(QIcon("Data_Analyzer.png"), "Your button", self)
    #     button_action.setStatusTip("This is your button")
    #     button_action.triggered.connect(self.onMyToolBarButtonClick)
    #     button_action.setCheckable(True)
    #     toolbar.addAction(button_action)

    #     self.setStatusBar(QStatusBar(self))


    # def onMyToolBarButtonClick(self, s):
    #     print("click", s)

#///////////////////////////////////////////////////////////////////////////////////////////////// 2 button with check point

    #     label = QLabel("Hello!")
    #     label.setAlignment(Qt.AlignCenter)

    #     self.setCentralWidget(label)

    #     toolbar = QToolBar("My main toolbar")
    #     toolbar.setIconSize(QSize(16, 16))
    #     self.addToolBar(toolbar)

    #     button_action = QAction(QIcon("bug.png"), "&Your button", self)
    #     button_action.setStatusTip("This is your button")
    #     button_action.triggered.connect(self.onMyToolBarButtonClick)
    #     button_action.setCheckable(True)
    #     toolbar.addAction(button_action)

    #     toolbar.addSeparator()

    #     button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
    #     button_action2.setStatusTip("This is your button2")
    #     button_action2.triggered.connect(self.onMyToolBarButtonClick)
    #     button_action2.setCheckable(True)
    #     toolbar.addAction(button_action2)

    #     toolbar.addWidget(QLabel("Hello"))
    #     toolbar.addWidget(QCheckBox())

    #     self.setStatusBar(QStatusBar(self))

    # def onMyToolBarButtonClick(self, s):
    #     print("click", s)

#///////////////////////////////////////////////////////////////////////////////////////////////// size adjust

    #     label = QLabel("Hello!")
    #     label.setAlignment(Qt.AlignCenter)

    #     self.setCentralWidget(label)

    #     toolbar = QToolBar("My main toolbar")
    #     toolbar.setIconSize(QSize(16, 16))
    #     self.addToolBar(toolbar)

    #     button_action = QAction(QIcon("bug.png"), "&Your button", self)
    #     button_action.setStatusTip("This is your button")
    #     button_action.triggered.connect(self.onMyToolBarButtonClick)
    #     button_action.setCheckable(True)
    #     toolbar.addAction(button_action)

    #     toolbar.addSeparator()

    #     button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
    #     button_action2.setStatusTip("This is your button2")
    #     button_action2.triggered.connect(self.onMyToolBarButtonClick)
    #     button_action2.setCheckable(True)
    #     toolbar.addAction(button_action2)

    #     toolbar.addWidget(QLabel("Hello"))
    #     toolbar.addWidget(QCheckBox())

    #     self.setStatusBar(QStatusBar(self))

    #     menu = self.menuBar()

    #     file_menu = menu.addMenu("&File")
    #     file_menu.addAction(button_action)

    # def onMyToolBarButtonClick(self, s):
    #     print("click", s)

#///////////////////////////////////////////////////////////////////////////////////////////////// menu option

    #     label = QLabel("Hello!")
    #     label.setAlignment(Qt.AlignCenter)

    #     self.setCentralWidget(label)

    #     toolbar = QToolBar("My main toolbar")
    #     toolbar.setIconSize(QSize(16, 16))
    #     self.addToolBar(toolbar)

    #     button_action = QAction(QIcon("bug.png"), "&Your button", self)
    #     button_action.setStatusTip("This is your button")
    #     button_action.triggered.connect(self.onMyToolBarButtonClick)
    #     button_action.setCheckable(True)
    #     toolbar.addAction(button_action)

    #     toolbar.addSeparator()

    #     button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
    #     button_action2.setStatusTip("This is your button2")
    #     button_action2.triggered.connect(self.onMyToolBarButtonClick)
    #     button_action2.setCheckable(True)
    #     toolbar.addAction(button_action2)

    #     toolbar.addWidget(QLabel("Hello"))
    #     toolbar.addWidget(QCheckBox())

    #     self.setStatusBar(QStatusBar(self))

    #     menu = self.menuBar()

    #     file_menu = menu.addMenu("&File")
    #     file_menu.addAction(button_action)
    #     file_menu.addSeparator()

    #     file_submenu = file_menu.addMenu("Submenu")
    #     file_submenu.addAction(button_action2)

    # def onMyToolBarButtonClick(self, s):
    #     print("click", s)

 #///////////////////////////////////////////////////////////////////////////////////////////////// menu option


    #     label = QLabel("Hello!")

    #     # The `Qt` namespace has a lot of attributes to customize
    #     # widgets. See: http://doc.qt.io/qt-5/qt.html
    #     label.setAlignment(Qt.AlignCenter)

    #     # Set the central widget of the Window. Widget will expand
    #     # to take up all the space in the window by default.
    #     self.setCentralWidget(label)

    #     toolbar = QToolBar("My main toolbar")
    #     toolbar.setIconSize(QSize(16, 16))
    #     self.addToolBar(toolbar)

    #     button_action = QAction(QIcon("bug.png"), "&Your button", self)
    #     button_action.setStatusTip("This is your button")
    #     button_action.triggered.connect(self.onMyToolBarButtonClick)
    #     button_action.setCheckable(True)
    #     # You can enter keyboard shortcuts using key names (e.g. Ctrl+p)
    #     # Qt.namespace identifiers (e.g. Qt.CTRL + Qt.Key_P)
    #     # or system agnostic identifiers (e.g. QKeySequence.Print)
    #     button_action.setShortcut(QKeySequence("Ctrl+p"))
    #     toolbar.addAction(button_action)

    #     toolbar.addSeparator()

    #     button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
    #     button_action2.setStatusTip("This is your button2")
    #     button_action2.triggered.connect(self.onMyToolBarButtonClick)
    #     button_action2.setCheckable(True)
    #     toolbar.addAction(button_action)

    #     toolbar.addWidget(QLabel("Hello"))
    #     toolbar.addWidget(QCheckBox())

    #     self.setStatusBar(QStatusBar(self))

    #     menu = self.menuBar()

    #     file_menu = menu.addMenu("&File")
    #     file_menu.addAction(button_action)

    #     file_menu.addSeparator()

    #     file_submenu = file_menu.addMenu("Submenu")

    #     file_submenu.addAction(button_action2)

    # def onMyToolBarButtonClick(self, s):
    #     print("click", s)   

 #///////////////////////////////////////////////////////////////////////////////////////////////// open new dialog box

    #     button = QPushButton("Press me for a dialog!")
    #     button.clicked.connect(self.button_clicked)
    #     self.setCentralWidget(button)

    # def button_clicked(self, s):
    #     print("click", s)

    #     dlg = QDialog(self)
    #     dlg.setWindowTitle("HELLO!")
    #     dlg.exec()

 #///////////////////////////////////////////////////////////////////////////////////////////////// Ok || Cancel Button

        # QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        # self.buttonBox = QDialogButtonBox(QBtn)
        # self.buttonBox.accepted.connect(self.accept)
        # self.buttonBox.rejected.connect(self.reject)

        # self.layout = QVBoxLayout()
        # message = QLabel("Something happened, is that OK?")
        # self.layout.addWidget(message)
        # self.layout.addWidget(self.buttonBox)
        # self.setLayout(self.layout)

 #///////////////////////////////////////////////////////////////////////////////////////////////// We can modify our CustomDialog class to accept a parent parameter.



# class CustomDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#         self.setWindowTitle("HELLO!")

#         QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

#         self.buttonBox = QDialogButtonBox(QBtn)
#         self.buttonBox.accepted.connect(self.accept)
#         self.buttonBox.rejected.connect(self.reject)

#         self.layout = QVBoxLayout()
#         message = QLabel("Something happened, is that OK?")
#         self.layout.addWidget(message)
#         self.layout.addWidget(self.buttonBox)
#         self.setLayout(self.layout)

# app = QApplication(sys.argv)
# win = CustomDialog()
# win.show()
# app.exec()

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec()

# Dialog Box and massage Box -------------------------------------------------------------------------------------------------------

# import sys

# from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QPushButton


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")

#         button = QPushButton("Press me for a dialog!")
#         button.clicked.connect(self.button_clicked)
#         self.setCentralWidget(button)
# # ------------------------------------------------------------------------------ single option only
#     # def button_clicked(self, s):
#     #     dlg = QMessageBox(self)
#     #     dlg.setWindowTitle("I have a question!")
#     #     dlg.setText("This is a simple dialog")
#     #     button = dlg.exec()

#     #     if button == QMessageBox.Ok:
#     #         print("OK!")

# # ------------------------------------------------------------------------------ Both option 

#     # def button_clicked(self, s):
#     #     dlg = QMessageBox(self)
#     #     dlg.setWindowTitle("I have a question!")
#     #     dlg.setText("This is a question dialog")
#     #     dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
#     #     dlg.setIcon(QMessageBox.Question)
#     #     button = dlg.exec()

#     #     if button == QMessageBox.Yes:
#     #         print("Yes!")
#     #     else:
#     #         print("No!")

# # ------------------------------------------------------------------------------ three option

#     # def button_clicked(self, s):

#     #     button = QMessageBox.critical(
#     #         self,
#     #         "Oh dear!",
#     #         "Something went very wrong.",
#     #         buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
#     #         defaultButton=QMessageBox.Discard,
#     #     )

#     #     if button == QMessageBox.Discard:
#     #         print("Discard!")
#     #     elif button == QMessageBox.NoToAll:
#     #         print("No to all!")
#     #     else:
#     #         print("Ignore!")

    

# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec()

