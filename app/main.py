import os
from PyQt5 import QtWidgets
from controller.mainWindow import Main

def detect_display_server():
    # Verifica se a variável de ambiente XDG_SESSION_TYPE está definida
    if 'XDG_SESSION_TYPE' in os.environ:
        # Obtém o valor da variável de ambiente XDG_SESSION_TYPE
        session_type = os.environ['XDG_SESSION_TYPE']
        # Verifica se o servidor de exibição é Wayland
        if session_type == 'wayland':
            return 'wayland'
    # Se não detectar Wayland, assume-se que está usando Xorg
    return 'xorg'

def configure_qt_platform():
    display_server = detect_display_server()
    if display_server == 'wayland':
        # Define a variável de ambiente QT_QPA_PLATFORM como wayland
        os.environ['QT_QPA_PLATFORM'] = 'wayland'
    else:
        # Define a variável de ambiente QT_QPA_PLATFORM como xcb para usar Xorg
        os.environ['QT_QPA_PLATFORM'] = 'xcb'

# Chama a função para configurar a plataforma Qt de acordo com o servidor de exibição
configure_qt_platform()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Main()
    sys.exit(app.exec_())
