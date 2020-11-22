"""
QLineEdit控件与回显模式
基本功能：输入单行的文本
4种回显模式EchoMode
1、Normal
2、NoEcho
3、Password
4、PasswordEchoOnEdit
"""

from PyQt5.QtWidgets import *
import sys


class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')

        formLayout = QFormLayout()

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        formLayout.addRow('NormalEdit', normalLineEdit)
        formLayout.addRow('NoEchoEdit', noEchoLineEdit)
        formLayout.addRow('PasswordEdit', passwordLineEdit)
        formLayout.addRow('PasswordEchoOnEdit', passwordEchoOnEditLineEdit)

        # placeholdertext
        normalLineEdit.setPlaceholderText('Normal')
        noEchoLineEdit.setPlaceholderText('NoEcho')
        passwordLineEdit.setPlaceholderText('NoEcho')
        passwordEchoOnEditLineEdit.setPlaceholderText('PasswordEchoOnEdit')

        # 设置模式
        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditEchoMode()
    main.show()
    sys.exit(app.exec_())

