# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose_option.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_optionList(object):
    def setupUi(self, optionList):
        optionList.setObjectName("optionList")
        optionList.resize(283, 178)
        self.verticalLayout = QtWidgets.QVBoxLayout(optionList)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(optionList)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.GlobalOption = QtWidgets.QCheckBox(optionList)
        self.GlobalOption.setObjectName("GlobalOption")
        self.verticalLayout.addWidget(self.GlobalOption)
        self.ControlSurfacesOption = QtWidgets.QCheckBox(optionList)
        self.ControlSurfacesOption.setObjectName("ControlSurfacesOption")
        self.verticalLayout.addWidget(self.ControlSurfacesOption)
        self.RowEffOption = QtWidgets.QCheckBox(optionList)
        self.RowEffOption.setObjectName("RowEffOption")
        self.verticalLayout.addWidget(self.RowEffOption)
        self.StageEffOption = QtWidgets.QCheckBox(optionList)
        self.StageEffOption.setObjectName("StageEffOption")
        self.verticalLayout.addWidget(self.StageEffOption)
        self.ProgrEffOption = QtWidgets.QCheckBox(optionList)
        self.ProgrEffOption.setObjectName("ProgrEffOption")
        self.verticalLayout.addWidget(self.ProgrEffOption)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.okBtn = QtWidgets.QPushButton(optionList)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout.addWidget(self.okBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(optionList)
        QtCore.QMetaObject.connectSlotsByName(optionList)

    def retranslateUi(self, optionList):
        _translate = QtCore.QCoreApplication.translate
        optionList.setWindowTitle(_translate("optionList", "Form"))
        self.label.setText(_translate("optionList", "Выберите необходимые функции:"))
        self.GlobalOption.setText(_translate("optionList", "Глобальные параметры турбомашины"))
        self.ControlSurfacesOption.setText(_translate("optionList", "Параметры на контрольных поверхностях (КП)"))
        self.RowEffOption.setText(_translate("optionList", "Анализ эффективности по венцам"))
        self.StageEffOption.setText(_translate("optionList", "Анализ эффективности по ступеням"))
        self.ProgrEffOption.setText(_translate("optionList", "Накопительные параметры эффективности"))
        self.okBtn.setText(_translate("optionList", "ОК"))

