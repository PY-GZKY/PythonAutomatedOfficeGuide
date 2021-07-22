除了运行脚本，有时候我们更希望能有一个界面，实现一个类似于`客户端`的操作。

`Python` 的 `GUI` 库中，`Qt` 和 `Tk` 占据了半边天，它们都实现了一些有趣的交互。

```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowTitle("Pywinauto")
        Dialog.resize(505, 292)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(100, 40, 121, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 230, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(100, 100, 41, 16))
        self.radioButton.setObjectName("radioButton")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(100, 190, 121, 16))
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 50, 54, 12))
        self.label.setObjectName("label")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(170, 100, 41, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 140, 61, 21))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(100, 140, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setEditable(True)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(260, 40, 211, 221))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Dialog)
        self.comboBox.setCurrentIndex(-1)

        self.pushButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        value = [['张三', '20'], ['李四', '25']]
        for k in value:
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            rownumber = self.tableWidget.rowCount()
            for i in range(2):
                newItem = QtWidgets.QTableWidgetItem(k[i])
                self.tableWidget.setItem(rownumber - 1, i, newItem)




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Pywinauto"))
        self.pushButton.setText(_translate("Dialog", "关闭"))
        self.radioButton.setText(_translate("Dialog", "男"))
        self.checkBox.setText(_translate("Dialog", "我已阅读有关事项"))
        self.label.setText(_translate("Dialog", "姓名"))
        self.radioButton_2.setText(_translate("Dialog", "女"))
        self.label_2.setText(_translate("Dialog", "性别"))
        self.label_3.setText(_translate("Dialog", "注册事项"))
        self.label_4.setText(_translate("Dialog", "所在地"))
        self.comboBox.setItemText(0, _translate("Dialog", "广东省"))
        self.comboBox.setItemText(1, _translate("Dialog", "浙江省"))
        self.comboBox.setItemText(2, _translate("Dialog", "湖南省"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
```