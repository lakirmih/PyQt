# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(322, 102)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.loginEdit = QtWidgets.QLineEdit(Form)
        self.loginEdit.setObjectName("loginEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.loginEdit)
        self.passwordEdit = QtWidgets.QLineEdit(Form)
        self.passwordEdit.setObjectName("passwordEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.okBtn = QtWidgets.QPushButton(Form)
        self.okBtn.setObjectName("okBtn")
        self.verticalLayout.addWidget(self.okBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Password"))
        self.label.setText(_translate("Form", "Login"))
        self.okBtn.setText(_translate("Form", "OK"))

