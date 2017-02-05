# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose_option.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(283, 178)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.GlobalOption = QtWidgets.QCheckBox(Form)
        self.GlobalOption.setObjectName("GlobalOption")
        self.verticalLayout.addWidget(self.GlobalOption)
        self.ControlSurfacesOption = QtWidgets.QCheckBox(Form)
        self.ControlSurfacesOption.setObjectName("ControlSurfacesOption")
        self.verticalLayout.addWidget(self.ControlSurfacesOption)
        self.RowEffOption = QtWidgets.QCheckBox(Form)
        self.RowEffOption.setObjectName("RowEffOption")
        self.verticalLayout.addWidget(self.RowEffOption)
        self.StageEffOption = QtWidgets.QCheckBox(Form)
        self.StageEffOption.setObjectName("StageEffOption")
        self.verticalLayout.addWidget(self.StageEffOption)
        self.ProgrEffOption = QtWidgets.QCheckBox(Form)
        self.ProgrEffOption.setObjectName("ProgrEffOption")
        self.verticalLayout.addWidget(self.ProgrEffOption)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.okBtn = QtWidgets.QPushButton(Form)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout.addWidget(self.okBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Выберите необходимые функции:"))
        self.GlobalOption.setText(_translate("Form", "Глобальные параметры турбомашины"))
        self.ControlSurfacesOption.setText(_translate("Form", "Параметры на контрольных поверхностях (КП)"))
        self.RowEffOption.setText(_translate("Form", "Анализ эффективности по венцам"))
        self.StageEffOption.setText(_translate("Form", "Анализ эффективности по ступеням"))
        self.ProgrEffOption.setText(_translate("Form", "Накопительные параметры эффективности"))
        self.okBtn.setText(_translate("Form", "ОК"))

