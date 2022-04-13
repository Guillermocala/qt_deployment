from PySide6 import QtWidgets
import sys
"hola"
class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.principal = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout()
        self.saludo = QtWidgets.QPushButton("Click me!")
        self.saludo.clicked.connect(self.hello)
        self.label = QtWidgets.QLabel()
        self.layout.addWidget(self.saludo)
        self.layout.addWidget(self.label)
        self.principal.setLayout(self.layout)
        self.setCentralWidget(self.principal)
        self.show()

    def hello(self):
        if self.label.text():
            self.label.setText('')
        else:
            self.label.setText("Hello world!")
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    principal = MyApp()
    sys.exit(app.exec())