# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/page01.ui'
#
# Created: Mon Dec 31 15:23:36 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Page01(object):
    def setupUi(self, Page01):
        Page01.setObjectName(_fromUtf8("Page01"))
        Page01.resize(730, 564)
        Page01.setMinimumSize(QtCore.QSize(730, 0))
        Page01.setMaximumSize(QtCore.QSize(730, 16777215))
        Page01.setStyleSheet(_fromUtf8(""))
        self.verticalLayout = QtGui.QVBoxLayout(Page01)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(Page01)
        self.label_2.setStyleSheet(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.nomM = QtGui.QLabel(Page01)
        self.nomM.setStyleSheet(_fromUtf8(""))
        self.nomM.setObjectName(_fromUtf8("nomM"))
        self.gridLayout.addWidget(self.nomM, 0, 0, 1, 1)
        self.codeM = QtGui.QLabel(Page01)
        self.codeM.setMinimumSize(QtCore.QSize(27, 20))
        self.codeM.setMaximumSize(QtCore.QSize(27, 20))
        self.codeM.setStyleSheet(_fromUtf8(""))
        self.codeM.setObjectName(_fromUtf8("codeM"))
        self.gridLayout.addWidget(self.codeM, 0, 1, 1, 1)
        self.M = QtGui.QRadioButton(Page01)
        self.M.setText(_fromUtf8(""))
        self.M.setObjectName(_fromUtf8("M"))
        self.gridLayout.addWidget(self.M, 0, 2, 1, 1)
        self.nomO = QtGui.QLabel(Page01)
        self.nomO.setObjectName(_fromUtf8("nomO"))
        self.gridLayout.addWidget(self.nomO, 1, 0, 1, 1)
        self.codeO = QtGui.QLabel(Page01)
        self.codeO.setMinimumSize(QtCore.QSize(27, 20))
        self.codeO.setMaximumSize(QtCore.QSize(27, 20))
        self.codeO.setStyleSheet(_fromUtf8(""))
        self.codeO.setObjectName(_fromUtf8("codeO"))
        self.gridLayout.addWidget(self.codeO, 1, 1, 1, 1)
        self.O = QtGui.QRadioButton(Page01)
        self.O.setText(_fromUtf8(""))
        self.O.setObjectName(_fromUtf8("O"))
        self.gridLayout.addWidget(self.O, 1, 2, 1, 1)
        self.nomC = QtGui.QLabel(Page01)
        self.nomC.setObjectName(_fromUtf8("nomC"))
        self.gridLayout.addWidget(self.nomC, 2, 0, 1, 1)
        self.codeC = QtGui.QLabel(Page01)
        self.codeC.setMinimumSize(QtCore.QSize(27, 20))
        self.codeC.setMaximumSize(QtCore.QSize(27, 20))
        self.codeC.setStyleSheet(_fromUtf8(""))
        self.codeC.setObjectName(_fromUtf8("codeC"))
        self.gridLayout.addWidget(self.codeC, 2, 1, 1, 1)
        self.C = QtGui.QRadioButton(Page01)
        self.C.setText(_fromUtf8(""))
        self.C.setObjectName(_fromUtf8("C"))
        self.gridLayout.addWidget(self.C, 2, 2, 1, 1)
        self.nomD = QtGui.QLabel(Page01)
        self.nomD.setObjectName(_fromUtf8("nomD"))
        self.gridLayout.addWidget(self.nomD, 3, 0, 1, 1)
        self.codeD = QtGui.QLabel(Page01)
        self.codeD.setMinimumSize(QtCore.QSize(27, 20))
        self.codeD.setMaximumSize(QtCore.QSize(27, 20))
        self.codeD.setStyleSheet(_fromUtf8(""))
        self.codeD.setObjectName(_fromUtf8("codeD"))
        self.gridLayout.addWidget(self.codeD, 3, 1, 1, 1)
        self.D = QtGui.QRadioButton(Page01)
        self.D.setText(_fromUtf8(""))
        self.D.setObjectName(_fromUtf8("D"))
        self.gridLayout.addWidget(self.D, 3, 2, 1, 1)
        self.nomV = QtGui.QLabel(Page01)
        self.nomV.setObjectName(_fromUtf8("nomV"))
        self.gridLayout.addWidget(self.nomV, 4, 0, 1, 1)
        self.codeV = QtGui.QLabel(Page01)
        self.codeV.setMinimumSize(QtCore.QSize(27, 20))
        self.codeV.setMaximumSize(QtCore.QSize(27, 20))
        self.codeV.setStyleSheet(_fromUtf8(""))
        self.codeV.setObjectName(_fromUtf8("codeV"))
        self.gridLayout.addWidget(self.codeV, 4, 1, 1, 1)
        self.V = QtGui.QRadioButton(Page01)
        self.V.setText(_fromUtf8(""))
        self.V.setObjectName(_fromUtf8("V"))
        self.gridLayout.addWidget(self.V, 4, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_3 = QtGui.QLabel(Page01)
        self.label_3.setStyleSheet(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.nomM_2 = QtGui.QLabel(Page01)
        self.nomM_2.setStyleSheet(_fromUtf8(""))
        self.nomM_2.setObjectName(_fromUtf8("nomM_2"))
        self.gridLayout_2.addWidget(self.nomM_2, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.codeM_2 = QtGui.QLabel(Page01)
        self.codeM_2.setMinimumSize(QtCore.QSize(27, 20))
        self.codeM_2.setMaximumSize(QtCore.QSize(27, 20))
        self.codeM_2.setStyleSheet(_fromUtf8(""))
        self.codeM_2.setObjectName(_fromUtf8("codeM_2"))
        self.gridLayout_2.addWidget(self.codeM_2, 0, 2, 1, 1)
        self.nbF = QtGui.QSpinBox(Page01)
        self.nbF.setEnabled(True)
        self.nbF.setMinimumSize(QtCore.QSize(30, 20))
        self.nbF.setMaximumSize(QtCore.QSize(30, 20))
        self.nbF.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.nbF.setWrapping(False)
        self.nbF.setFrame(True)
        self.nbF.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nbF.setReadOnly(True)
        self.nbF.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.nbF.setAccelerated(False)
        self.nbF.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.nbF.setKeyboardTracking(True)
        self.nbF.setSuffix(_fromUtf8(""))
        self.nbF.setPrefix(_fromUtf8(""))
        self.nbF.setMinimum(0)
        self.nbF.setMaximum(9)
        self.nbF.setSingleStep(1)
        self.nbF.setProperty("value", 0)
        self.nbF.setObjectName(_fromUtf8("nbF"))
        self.gridLayout_2.addWidget(self.nbF, 0, 3, 1, 1)
        self.nomO_2 = QtGui.QLabel(Page01)
        self.nomO_2.setObjectName(_fromUtf8("nomO_2"))
        self.gridLayout_2.addWidget(self.nomO_2, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 1)
        self.codeO_2 = QtGui.QLabel(Page01)
        self.codeO_2.setMinimumSize(QtCore.QSize(27, 20))
        self.codeO_2.setMaximumSize(QtCore.QSize(27, 20))
        self.codeO_2.setStyleSheet(_fromUtf8(""))
        self.codeO_2.setObjectName(_fromUtf8("codeO_2"))
        self.gridLayout_2.addWidget(self.codeO_2, 1, 2, 1, 1)
        self.nbG = QtGui.QSpinBox(Page01)
        self.nbG.setEnabled(True)
        self.nbG.setMinimumSize(QtCore.QSize(30, 20))
        self.nbG.setMaximumSize(QtCore.QSize(30, 20))
        self.nbG.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.nbG.setWrapping(False)
        self.nbG.setFrame(True)
        self.nbG.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nbG.setReadOnly(True)
        self.nbG.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.nbG.setAccelerated(False)
        self.nbG.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.nbG.setKeyboardTracking(True)
        self.nbG.setSuffix(_fromUtf8(""))
        self.nbG.setPrefix(_fromUtf8(""))
        self.nbG.setMinimum(0)
        self.nbG.setMaximum(9)
        self.nbG.setSingleStep(1)
        self.nbG.setProperty("value", 0)
        self.nbG.setObjectName(_fromUtf8("nbG"))
        self.gridLayout_2.addWidget(self.nbG, 1, 3, 1, 1)
        self.nomC_2 = QtGui.QLabel(Page01)
        self.nomC_2.setObjectName(_fromUtf8("nomC_2"))
        self.gridLayout_2.addWidget(self.nomC_2, 2, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 1)
        self.codeC_2 = QtGui.QLabel(Page01)
        self.codeC_2.setMinimumSize(QtCore.QSize(27, 20))
        self.codeC_2.setMaximumSize(QtCore.QSize(27, 20))
        self.codeC_2.setStyleSheet(_fromUtf8(""))
        self.codeC_2.setObjectName(_fromUtf8("codeC_2"))
        self.gridLayout_2.addWidget(self.codeC_2, 2, 2, 1, 1)
        self.nbH = QtGui.QSpinBox(Page01)
        self.nbH.setEnabled(True)
        self.nbH.setMinimumSize(QtCore.QSize(30, 20))
        self.nbH.setMaximumSize(QtCore.QSize(30, 20))
        self.nbH.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.nbH.setWrapping(False)
        self.nbH.setFrame(True)
        self.nbH.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nbH.setReadOnly(True)
        self.nbH.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.nbH.setAccelerated(False)
        self.nbH.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.nbH.setKeyboardTracking(True)
        self.nbH.setSuffix(_fromUtf8(""))
        self.nbH.setPrefix(_fromUtf8(""))
        self.nbH.setMinimum(0)
        self.nbH.setMaximum(9)
        self.nbH.setSingleStep(1)
        self.nbH.setProperty("value", 0)
        self.nbH.setObjectName(_fromUtf8("nbH"))
        self.gridLayout_2.addWidget(self.nbH, 2, 3, 1, 1)
        self.nomD_2 = QtGui.QLabel(Page01)
        self.nomD_2.setObjectName(_fromUtf8("nomD_2"))
        self.gridLayout_2.addWidget(self.nomD_2, 3, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 3, 1, 1, 1)
        self.codeD_2 = QtGui.QLabel(Page01)
        self.codeD_2.setMinimumSize(QtCore.QSize(27, 20))
        self.codeD_2.setMaximumSize(QtCore.QSize(27, 20))
        self.codeD_2.setStyleSheet(_fromUtf8(""))
        self.codeD_2.setObjectName(_fromUtf8("codeD_2"))
        self.gridLayout_2.addWidget(self.codeD_2, 3, 2, 1, 1)
        self.nbI = QtGui.QSpinBox(Page01)
        self.nbI.setEnabled(True)
        self.nbI.setMinimumSize(QtCore.QSize(30, 20))
        self.nbI.setMaximumSize(QtCore.QSize(30, 20))
        self.nbI.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.nbI.setWrapping(False)
        self.nbI.setFrame(True)
        self.nbI.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nbI.setReadOnly(True)
        self.nbI.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.nbI.setAccelerated(False)
        self.nbI.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.nbI.setKeyboardTracking(True)
        self.nbI.setSuffix(_fromUtf8(""))
        self.nbI.setPrefix(_fromUtf8(""))
        self.nbI.setMinimum(0)
        self.nbI.setMaximum(9)
        self.nbI.setSingleStep(1)
        self.nbI.setProperty("value", 0)
        self.nbI.setObjectName(_fromUtf8("nbI"))
        self.gridLayout_2.addWidget(self.nbI, 3, 3, 1, 1)
        self.nomV_2 = QtGui.QLabel(Page01)
        self.nomV_2.setObjectName(_fromUtf8("nomV_2"))
        self.gridLayout_2.addWidget(self.nomV_2, 4, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 4, 1, 1, 1)
        self.codeV_2 = QtGui.QLabel(Page01)
        self.codeV_2.setMinimumSize(QtCore.QSize(27, 20))
        self.codeV_2.setMaximumSize(QtCore.QSize(27, 20))
        self.codeV_2.setStyleSheet(_fromUtf8(""))
        self.codeV_2.setObjectName(_fromUtf8("codeV_2"))
        self.gridLayout_2.addWidget(self.codeV_2, 4, 2, 1, 1)
        self.nbR = QtGui.QSpinBox(Page01)
        self.nbR.setEnabled(True)
        self.nbR.setMinimumSize(QtCore.QSize(30, 20))
        self.nbR.setMaximumSize(QtCore.QSize(30, 20))
        self.nbR.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.nbR.setWrapping(False)
        self.nbR.setFrame(True)
        self.nbR.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nbR.setReadOnly(True)
        self.nbR.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.nbR.setAccelerated(False)
        self.nbR.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.nbR.setKeyboardTracking(True)
        self.nbR.setSuffix(_fromUtf8(""))
        self.nbR.setPrefix(_fromUtf8(""))
        self.nbR.setMinimum(0)
        self.nbR.setMaximum(9)
        self.nbR.setSingleStep(1)
        self.nbR.setProperty("value", 0)
        self.nbR.setObjectName(_fromUtf8("nbR"))
        self.gridLayout_2.addWidget(self.nbR, 4, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.label_4 = QtGui.QLabel(Page01)
        self.label_4.setStyleSheet(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.nomM_3 = QtGui.QLabel(Page01)
        self.nomM_3.setStyleSheet(_fromUtf8(""))
        self.nomM_3.setObjectName(_fromUtf8("nomM_3"))
        self.gridLayout_3.addWidget(self.nomM_3, 0, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 1, 1, 1)
        self.codeM_3 = QtGui.QLabel(Page01)
        self.codeM_3.setMinimumSize(QtCore.QSize(27, 20))
        self.codeM_3.setMaximumSize(QtCore.QSize(27, 20))
        self.codeM_3.setStyleSheet(_fromUtf8(""))
        self.codeM_3.setObjectName(_fromUtf8("codeM_3"))
        self.gridLayout_3.addWidget(self.codeM_3, 0, 2, 1, 1)
        self.nbJ = QtGui.QSpinBox(Page01)
        self.nbJ.setEnabled(True)
        self.nbJ.setMinimumSize(QtCore.QSize(30, 20))
        self.nbJ.setMaximumSize(QtCore.QSize(30, 20))
        self.nbJ.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.nbJ.setWrapping(False)
        self.nbJ.setFrame(True)
        self.nbJ.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nbJ.setReadOnly(True)
        self.nbJ.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.nbJ.setAccelerated(False)
        self.nbJ.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.nbJ.setKeyboardTracking(True)
        self.nbJ.setSuffix(_fromUtf8(""))
        self.nbJ.setPrefix(_fromUtf8(""))
        self.nbJ.setMinimum(0)
        self.nbJ.setMaximum(9)
        self.nbJ.setSingleStep(1)
        self.nbJ.setProperty("value", 0)
        self.nbJ.setObjectName(_fromUtf8("nbJ"))
        self.gridLayout_3.addWidget(self.nbJ, 0, 3, 1, 1)
        self.nomO_3 = QtGui.QLabel(Page01)
        self.nomO_3.setObjectName(_fromUtf8("nomO_3"))
        self.gridLayout_3.addWidget(self.nomO_3, 1, 0, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 1, 1, 1, 1)
        self.codeO_3 = QtGui.QLabel(Page01)
        self.codeO_3.setMinimumSize(QtCore.QSize(27, 20))
        self.codeO_3.setMaximumSize(QtCore.QSize(27, 20))
        self.codeO_3.setStyleSheet(_fromUtf8(""))
        self.codeO_3.setObjectName(_fromUtf8("codeO_3"))
        self.gridLayout_3.addWidget(self.codeO_3, 1, 2, 1, 1)
        self.nbN = QtGui.QSpinBox(Page01)
        self.nbN.setEnabled(True)
        self.nbN.setMinimumSize(QtCore.QSize(30, 20))
        self.nbN.setMaximumSize(QtCore.QSize(30, 20))
        self.nbN.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.nbN.setWrapping(False)
        self.nbN.setFrame(True)
        self.nbN.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nbN.setReadOnly(True)
        self.nbN.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.nbN.setAccelerated(False)
        self.nbN.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.nbN.setKeyboardTracking(True)
        self.nbN.setSuffix(_fromUtf8(""))
        self.nbN.setPrefix(_fromUtf8(""))
        self.nbN.setMinimum(0)
        self.nbN.setMaximum(9)
        self.nbN.setSingleStep(1)
        self.nbN.setProperty("value", 0)
        self.nbN.setObjectName(_fromUtf8("nbN"))
        self.gridLayout_3.addWidget(self.nbN, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        spacerItem8 = QtGui.QSpacerItem(20, 38, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)

        self.retranslateUi(Page01)
        QtCore.QMetaObject.connectSlotsByName(Page01)

    def retranslateUi(self, Page01):
        Page01.setWindowTitle(QtGui.QApplication.translate("Page01", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Page01", "A| ETAT CIVIL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setProperty("class", QtGui.QApplication.translate("Page01", "titreA", None, QtGui.QApplication.UnicodeUTF8))
        self.nomM.setText(QtGui.QApplication.translate("Page01", "Mariés", None, QtGui.QApplication.UnicodeUTF8))
        self.nomM.setProperty("class", QtGui.QApplication.translate("Page01", "texte01", None, QtGui.QApplication.UnicodeUTF8))
        self.codeM.setText(QtGui.QApplication.translate("Page01", "M", None, QtGui.QApplication.UnicodeUTF8))
        self.codeM.setProperty("class", QtGui.QApplication.translate("Page01", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.nomO.setText(QtGui.QApplication.translate("Page01", "Pacsés", None, QtGui.QApplication.UnicodeUTF8))
        self.nomO.setProperty("class", QtGui.QApplication.translate("Page01", "texte01", None, QtGui.QApplication.UnicodeUTF8))
        self.codeO.setText(QtGui.QApplication.translate("Page01", "O", None, QtGui.QApplication.UnicodeUTF8))
        self.codeO.setProperty("class", QtGui.QApplication.translate("Page01", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.nomC.setText(QtGui.QApplication.translate("Page01", "Célibataire", None, QtGui.QApplication.UnicodeUTF8))
        self.nomC.setProperty("class", QtGui.QApplication.translate("Page01", "texte01", None, QtGui.QApplication.UnicodeUTF8))
        self.codeC.setText(QtGui.QApplication.translate("Page01", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.codeC.setProperty("class", QtGui.QApplication.translate("Page01", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.nomD.setText(QtGui.QApplication.translate("Page01", "Divorcé", None, QtGui.QApplication.UnicodeUTF8))
        self.nomD.setProperty("class", QtGui.QApplication.translate("Page01", "texte01", None, QtGui.QApplication.UnicodeUTF8))
        self.codeD.setText(QtGui.QApplication.translate("Page01", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.codeD.setProperty("class", QtGui.QApplication.translate("Page01", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.nomV.setText(QtGui.QApplication.translate("Page01", "Veuf", None, QtGui.QApplication.UnicodeUTF8))
        self.nomV.setProperty("class", QtGui.QApplication.translate("Page01", "texte01", None, QtGui.QApplication.UnicodeUTF8))
        self.codeV.setText(QtGui.QApplication.translate("Page01", "V", None, QtGui.QApplication.UnicodeUTF8))
        self.codeV.setProperty("class", QtGui.QApplication.translate("Page01", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Page01", "C| PERSONNES A CHARGE en 2010", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setProperty("class", QtGui.QApplication.translate("Page01", "titreA", None, QtGui.QApplication.UnicodeUTF8))
        self.nomM_2.setText(QtGui.QApplication.translate("Page01", "Nombre d\'enfants non mariés de moins de 18 ans au 1er janvier 2010, ou nés en 2010, ou handicapés quel que soit leur âge", None, QtGui.QApplication.UnicodeUTF8))
        self.nomM_2.setProperty("class", QtGui.QApplication.translate("Page01", "texte01", None, QtGui.QApplication.UnicodeUTF8))
        self.codeM_2.setText(QtGui.QApplication.translate("Page01", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.codeM_2.setProperty("class", QtGui.QApplication.translate("Page01", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.nomO_2.setText(QtGui.QApplication.translate("Page01", "Dont enfants titulaires de la carte d\'invalidité ", None, QtGui.QApplication.UnicodeUTF8))
        self.nomO_2.setProperty("class", QtGui.QApplication.translate("Page01", "texte01", None, QtGui.QApplication.UnicodeUTF8))
        self.codeO_2.setText(QtGui.QApplication.translate("Page01", "G", None, QtGui.QApplication.UnicodeUTF8))
        self.codeO_2.setProperty("class", QtGui.QApplication.translate("Page01", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.nomC_2.setText(QtGui.QApplication.translate("Page01", "Nombre d\'enfants non mariés en résidence alternée de moins de 18 ans au 1er janvier 2010 ou nés en 2010\n"
"ou handicapés quel que soit l\'âge", None, QtGui.QApplication.UnicodeUTF8))
        self.nomC_2.setProperty("class", QtGui.QApplication.translate("Page01", "texte01", None, QtGui.QApplication.UnicodeUTF8))
        self.codeC_2.setText(QtGui.QApplication.translate("Page01", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.codeC_2.setProperty("class", QtGui.QApplication.translate("Page01", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.nomD_2.setText(QtGui.QApplication.translate("Page01", "dont enfants en résidence alternée titulaires de la carte d\'invalidité", None, QtGui.QApplication.UnicodeUTF8))
        self.nomD_2.setProperty("class", QtGui.QApplication.translate("Page01", "texte01", None, QtGui.QApplication.UnicodeUTF8))
        self.codeD_2.setText(QtGui.QApplication.translate("Page01", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.codeD_2.setProperty("class", QtGui.QApplication.translate("Page01", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.nomV_2.setText(QtGui.QApplication.translate("Page01", "Nombre de personnes (autres que vos enfants) vivant sous votre toit et titulaires de la carte d\'invalidité d\'au moins 80 % ", None, QtGui.QApplication.UnicodeUTF8))
        self.nomV_2.setProperty("class", QtGui.QApplication.translate("Page01", "texte01", None, QtGui.QApplication.UnicodeUTF8))
        self.codeV_2.setText(QtGui.QApplication.translate("Page01", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.codeV_2.setProperty("class", QtGui.QApplication.translate("Page01", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Page01", "D| RATTACHEMENT D\'ENFANTS MAJEURS OU MARIÉ EN 2010", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setProperty("class", QtGui.QApplication.translate("Page01", "titreA", None, QtGui.QApplication.UnicodeUTF8))
        self.nomM_3.setText(QtGui.QApplication.translate("Page01", "Nombre d\'enfants majeurs célibataires (ou veufs ou divorcés) sans enfant qui demandent leur rattachement", None, QtGui.QApplication.UnicodeUTF8))
        self.nomM_3.setProperty("class", QtGui.QApplication.translate("Page01", "texte01", None, QtGui.QApplication.UnicodeUTF8))
        self.codeM_3.setText(QtGui.QApplication.translate("Page01", "J", None, QtGui.QApplication.UnicodeUTF8))
        self.codeM_3.setProperty("class", QtGui.QApplication.translate("Page01", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.nomO_3.setText(QtGui.QApplication.translate("Page01", "Nombre d\'enfants mariés (ou non mariés chargés de famille) qui demandent leur rattachement (y compris conjoint et enfants)", None, QtGui.QApplication.UnicodeUTF8))
        self.nomO_3.setProperty("class", QtGui.QApplication.translate("Page01", "texte01", None, QtGui.QApplication.UnicodeUTF8))
        self.codeO_3.setText(QtGui.QApplication.translate("Page01", "N", None, QtGui.QApplication.UnicodeUTF8))
        self.codeO_3.setProperty("class", QtGui.QApplication.translate("Page01", "code", None, QtGui.QApplication.UnicodeUTF8))

