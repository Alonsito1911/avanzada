from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QApplication
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
import sys
from parametros import RUTA_LOGO
import parametros
import parametros as p
from backend import logica_inicio

class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(str, str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Geometría
        self.setGeometry(600, 200, 500, 500)
        self.setWindowTitle('Ventana de Inicio')
        self.setStyleSheet("background-color: lightblue;")
        self.crear_elementos()

    def crear_elementos(self):
        # Qlabel
        self.logo = QLabel(self)

        self.logo.setGeometry(50, 70, 300, 300)
        ruta_imagen = RUTA_LOGO
        pixeles = QPixmap(ruta_imagen)
        self.logo.setPixmap(pixeles)
        self.logo.setScaledContents(True)

        # Qlineedit
        self.input = QLineEdit('', self)
        self.input.setGeometry(200, 400, 200, 20)
        # Qlabel
        self.ingresar_nombre_usuario = QLabel('Ingresa tu nombre de usuario:', self)
        self.ingresar_nombre_usuario.move(15, 400)
        # QLineEdit contraseña ocultar con setEchoMode Qlinepassword

        self.contrasena = QLineEdit('', self)
        self.contrasena.setGeometry(200, 430, 200, 20)
        self.contrasena.setEchoMode(QLineEdit.Password)
        # COMPLETAR
        # Qlabel ingresar contraseña

        self.ingresar_contrasena = QLabel('Ingresa tu contraseña:', self)
        self.ingresar_contrasena.move(15, 430)

        # Qpushbutton
        self.boton = QPushButton('Empezar juego', self)
        self.boton.resize(self.boton.sizeHint())
        self.boton.clicked.connect(self.enviar_login)
        self.boton.move(15, 460)
        self.show()

    def enviar_login(self):
        contrasena = self.contrasena.text()
        usuario = self.input.text()
        self.senal_enviar_login.emit(contrasena,  usuario)
        self.hide()
        # COMPLETAR
        pass

    def recibir_validacion(self, valid: bool, errores: set) -> None:
        # COMPLETAR
        pass
