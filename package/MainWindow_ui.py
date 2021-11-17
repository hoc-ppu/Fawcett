# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.intro_text = QtWidgets.QLabel(self.centralwidget)
        self.intro_text.setTextFormat(QtCore.Qt.RichText)
        self.intro_text.setWordWrap(True)
        self.intro_text.setOpenExternalLinks(True)
        self.intro_text.setObjectName("intro_text")
        self.verticalLayout.addWidget(self.intro_text)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.date_label = QtWidgets.QLabel(self.frame)
        self.date_label.setWordWrap(True)
        self.date_label.setObjectName("date_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.date_label)
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.vboxlayout.setObjectName("vboxlayout")
        self.create_proof_btn = QtWidgets.QPushButton(self.frame_2)
        self.create_proof_btn.setMaximumSize(QtCore.QSize(350, 16777215))
        self.create_proof_btn.setObjectName("create_proof_btn")
        self.vboxlayout.addWidget(self.create_proof_btn)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.logBtn = QtWidgets.QPushButton(self.centralwidget)
        self.logBtn.setObjectName("logBtn")
        self.verticalLayout.addWidget(self.logBtn, 0, QtCore.Qt.AlignRight)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionInstilation_Instructions = QtWidgets.QAction(MainWindow)
        self.actionInstilation_Instructions.setObjectName("actionInstilation_Instructions")
        self.actionView_source_code = QtWidgets.QAction(MainWindow)
        self.actionView_source_code.setObjectName("actionView_source_code")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fawcett App"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#79b656;\">Fawcett App </span><span style=\" font-size:14pt; font-weight:600; color:#79b656;\">(v5)</span></p></body></html>"))
        self.intro_text.setText(_translate("MainWindow", "<html><head/><body><p>Create a quick proof of the \'Questions Tabled On\' document. First select the tableing date for the questions then press \'Create Quick Proof\'. This program will query the <a href=\"https://api.eqm.parliament.uk/\"><span style=\" text-decoration: underline; color:#419cff;\">EQM API</span></a> for the relevant questions and arrange them for you in a web browser. </p></body></html>"))
        self.date_label.setText(_translate("MainWindow", "Select tableing date"))
        self.create_proof_btn.setText(_translate("MainWindow", "Create Quick Proof"))
        self.logBtn.setText(_translate("MainWindow", "Open Log"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Usage Instructions, background and installation instructions are avaliable on <a href=\"https://hopuk.sharepoint.com/:w:/r/sites/bct-ppu/_layouts/15/Doc.aspx?sourcedoc=%7B6B4ACE86-8B55-4742-A8EC-12BE078E67A2%7D&amp;file=FawcettAppInstructions.docx&amp;action=default&amp;mobileredirect=true\"><span style=\" text-decoration: underline; color:#419cff;\">SharePoint.</span></a><br/>You can also view the source code on <a href=\"https://github.com/hoc-ppu/Fawcett\"><span style=\" text-decoration: underline; color:#419cff;\">GitHub</span></a>.</p></body></html>"))
        self.actionInstilation_Instructions.setText(_translate("MainWindow", "Instilation Instructions"))
        self.actionView_source_code.setText(_translate("MainWindow", "View source code"))
