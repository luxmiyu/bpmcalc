# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(405, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(405, 300))
        MainWindow.setMaximumSize(QSize(405, 300))
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionTapT = QAction(MainWindow)
        self.actionTapT.setObjectName(u"actionTapT")
        self.actionTapZ = QAction(MainWindow)
        self.actionTapZ.setObjectName(u"actionTapZ")
        self.actionTapX = QAction(MainWindow)
        self.actionTapX.setObjectName(u"actionTapX")
        self.actionTapReset = QAction(MainWindow)
        self.actionTapReset.setObjectName(u"actionTapReset")
        self.actionGo = QAction(MainWindow)
        self.actionGo.setObjectName(u"actionGo")
        self.actionStart = QAction(MainWindow)
        self.actionStart.setObjectName(u"actionStart")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tabTap = QWidget()
        self.tabTap.setObjectName(u"tabTap")
        self.gridLayout_5 = QGridLayout(self.tabTap)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.tapButtonReset = QPushButton(self.tabTap)
        self.tapButtonReset.setObjectName(u"tapButtonReset")
        self.tapButtonReset.setMinimumSize(QSize(100, 0))
        self.tapButtonReset.setCursor(QCursor(Qt.PointingHandCursor))
        self.tapButtonReset.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_12.addWidget(self.tapButtonReset, 0, 4, 1, 1)

        self.tapSpinboxAmount = QSpinBox(self.tabTap)
        self.tapSpinboxAmount.setObjectName(u"tapSpinboxAmount")
        self.tapSpinboxAmount.setFocusPolicy(Qt.NoFocus)
        self.tapSpinboxAmount.setMaximum(10000)
        self.tapSpinboxAmount.setSingleStep(16)

        self.gridLayout_12.addWidget(self.tapSpinboxAmount, 0, 1, 1, 1)

        self.tapLabelAmount = QLabel(self.tabTap)
        self.tapLabelAmount.setObjectName(u"tapLabelAmount")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tapLabelAmount.sizePolicy().hasHeightForWidth())
        self.tapLabelAmount.setSizePolicy(sizePolicy1)

        self.gridLayout_12.addWidget(self.tapLabelAmount, 0, 0, 1, 1)

        self.tapButtonTap = QPushButton(self.tabTap)
        self.tapButtonTap.setObjectName(u"tapButtonTap")
        self.tapButtonTap.setMinimumSize(QSize(100, 0))
        self.tapButtonTap.setCursor(QCursor(Qt.PointingHandCursor))
        self.tapButtonTap.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_12.addWidget(self.tapButtonTap, 0, 3, 1, 1)

        self.tapLCD = QLCDNumber(self.tabTap)
        self.tapLCD.setObjectName(u"tapLCD")
        self.tapLCD.setMinimumSize(QSize(0, 70))
        self.tapLCD.setDigitCount(9)
        self.tapLCD.setSegmentStyle(QLCDNumber.Flat)
        self.tapLCD.setProperty("value", 0.000000000000000)

        self.gridLayout_12.addWidget(self.tapLCD, 1, 0, 1, 5)

        self.tapLabelDetails = QLabel(self.tabTap)
        self.tapLabelDetails.setObjectName(u"tapLabelDetails")
        sizePolicy1.setHeightForWidth(self.tapLabelDetails.sizePolicy().hasHeightForWidth())
        self.tapLabelDetails.setSizePolicy(sizePolicy1)
        self.tapLabelDetails.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.tapLabelDetails, 2, 0, 1, 5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.gridLayout_12.setColumnStretch(0, 1)

        self.gridLayout_5.addLayout(self.gridLayout_12, 1, 0, 1, 1)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.tapRadio2 = QRadioButton(self.tabTap)
        self.tapRadio2.setObjectName(u"tapRadio2")
        self.tapRadio2.setCursor(QCursor(Qt.PointingHandCursor))
        self.tapRadio2.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_13.addWidget(self.tapRadio2, 1, 1, 1, 1)

        self.tapRadio1 = QRadioButton(self.tabTap)
        self.tapRadio1.setObjectName(u"tapRadio1")
        self.tapRadio1.setCursor(QCursor(Qt.PointingHandCursor))
        self.tapRadio1.setFocusPolicy(Qt.NoFocus)
        self.tapRadio1.setChecked(True)

        self.gridLayout_13.addWidget(self.tapRadio1, 1, 0, 1, 1)

        self.tapLabelRhythm = QLabel(self.tabTap)
        self.tapLabelRhythm.setObjectName(u"tapLabelRhythm")
        sizePolicy1.setHeightForWidth(self.tapLabelRhythm.sizePolicy().hasHeightForWidth())
        self.tapLabelRhythm.setSizePolicy(sizePolicy1)

        self.gridLayout_13.addWidget(self.tapLabelRhythm, 0, 0, 1, 1)

        self.tapRadio3 = QRadioButton(self.tabTap)
        self.tapRadio3.setObjectName(u"tapRadio3")
        self.tapRadio3.setCursor(QCursor(Qt.PointingHandCursor))
        self.tapRadio3.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_13.addWidget(self.tapRadio3, 1, 2, 1, 1)

        self.tapRadio4 = QRadioButton(self.tabTap)
        self.tapRadio4.setObjectName(u"tapRadio4")
        self.tapRadio4.setCursor(QCursor(Qt.PointingHandCursor))
        self.tapRadio4.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_13.addWidget(self.tapRadio4, 1, 3, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_13, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabTap, "")
        self.tabCalc = QWidget()
        self.tabCalc.setObjectName(u"tabCalc")
        self.gridLayout_10 = QGridLayout(self.tabCalc)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.calcRadio2 = QRadioButton(self.tabCalc)
        self.calcRadio2.setObjectName(u"calcRadio2")
        self.calcRadio2.setCursor(QCursor(Qt.PointingHandCursor))
        self.calcRadio2.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_14.addWidget(self.calcRadio2, 1, 1, 1, 1)

        self.calcRadio4 = QRadioButton(self.tabCalc)
        self.calcRadio4.setObjectName(u"calcRadio4")
        self.calcRadio4.setCursor(QCursor(Qt.PointingHandCursor))
        self.calcRadio4.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_14.addWidget(self.calcRadio4, 1, 3, 1, 1)

        self.calcRadio3 = QRadioButton(self.tabCalc)
        self.calcRadio3.setObjectName(u"calcRadio3")
        self.calcRadio3.setCursor(QCursor(Qt.PointingHandCursor))
        self.calcRadio3.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_14.addWidget(self.calcRadio3, 1, 2, 1, 1)

        self.calcRadio1 = QRadioButton(self.tabCalc)
        self.calcRadio1.setObjectName(u"calcRadio1")
        self.calcRadio1.setCursor(QCursor(Qt.PointingHandCursor))
        self.calcRadio1.setFocusPolicy(Qt.NoFocus)
        self.calcRadio1.setChecked(True)

        self.gridLayout_14.addWidget(self.calcRadio1, 1, 0, 1, 1)

        self.calcLabelRhythm = QLabel(self.tabCalc)
        self.calcLabelRhythm.setObjectName(u"calcLabelRhythm")
        sizePolicy1.setHeightForWidth(self.calcLabelRhythm.sizePolicy().hasHeightForWidth())
        self.calcLabelRhythm.setSizePolicy(sizePolicy1)

        self.gridLayout_14.addWidget(self.calcLabelRhythm, 0, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_14, 0, 0, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.calcComboboxValue = QComboBox(self.tabCalc)
        self.calcComboboxValue.addItem("")
        self.calcComboboxValue.addItem("")
        self.calcComboboxValue.addItem("")
        self.calcComboboxValue.setObjectName(u"calcComboboxValue")
        self.calcComboboxValue.setCursor(QCursor(Qt.PointingHandCursor))
        self.calcComboboxValue.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_11.addWidget(self.calcComboboxValue, 0, 2, 1, 1)

        self.calcLabelValue = QLabel(self.tabCalc)
        self.calcLabelValue.setObjectName(u"calcLabelValue")

        self.gridLayout_11.addWidget(self.calcLabelValue, 0, 0, 1, 1)

        self.calcSpinboxValue = QDoubleSpinBox(self.tabCalc)
        self.calcSpinboxValue.setObjectName(u"calcSpinboxValue")
        self.calcSpinboxValue.setMinimum(1.000000000000000)
        self.calcSpinboxValue.setMaximum(1000.000000000000000)
        self.calcSpinboxValue.setSingleStep(6.000000000000000)
        self.calcSpinboxValue.setValue(180.000000000000000)

        self.gridLayout_11.addWidget(self.calcSpinboxValue, 0, 1, 1, 1)

        self.calcButtonGo = QPushButton(self.tabCalc)
        self.calcButtonGo.setObjectName(u"calcButtonGo")
        self.calcButtonGo.setCursor(QCursor(Qt.PointingHandCursor))
        self.calcButtonGo.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_11.addWidget(self.calcButtonGo, 0, 3, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_11, 1, 0, 1, 1)

        self.calcTextResult = QTextBrowser(self.tabCalc)
        self.calcTextResult.setObjectName(u"calcTextResult")
        self.calcTextResult.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_10.addWidget(self.calcTextResult, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tabCalc, "")
        self.tabMetro = QWidget()
        self.tabMetro.setObjectName(u"tabMetro")
        self.gridLayout_8 = QGridLayout(self.tabMetro)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.metroRadio2 = QRadioButton(self.tabMetro)
        self.metroRadio2.setObjectName(u"metroRadio2")
        self.metroRadio2.setCursor(QCursor(Qt.PointingHandCursor))
        self.metroRadio2.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_7.addWidget(self.metroRadio2, 1, 1, 1, 1)

        self.metroRadio3 = QRadioButton(self.tabMetro)
        self.metroRadio3.setObjectName(u"metroRadio3")
        self.metroRadio3.setCursor(QCursor(Qt.PointingHandCursor))
        self.metroRadio3.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_7.addWidget(self.metroRadio3, 1, 2, 1, 1)

        self.metroRadio1 = QRadioButton(self.tabMetro)
        self.metroRadio1.setObjectName(u"metroRadio1")
        self.metroRadio1.setCursor(QCursor(Qt.PointingHandCursor))
        self.metroRadio1.setFocusPolicy(Qt.NoFocus)
        self.metroRadio1.setChecked(True)

        self.gridLayout_7.addWidget(self.metroRadio1, 1, 0, 1, 1)

        self.metroLabelRhythm = QLabel(self.tabMetro)
        self.metroLabelRhythm.setObjectName(u"metroLabelRhythm")
        sizePolicy1.setHeightForWidth(self.metroLabelRhythm.sizePolicy().hasHeightForWidth())
        self.metroLabelRhythm.setSizePolicy(sizePolicy1)

        self.gridLayout_7.addWidget(self.metroLabelRhythm, 0, 0, 1, 1)

        self.metroRadio4 = QRadioButton(self.tabMetro)
        self.metroRadio4.setObjectName(u"metroRadio4")
        self.metroRadio4.setCursor(QCursor(Qt.PointingHandCursor))
        self.metroRadio4.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_7.addWidget(self.metroRadio4, 1, 3, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 0, 0, 1, 2)

        self.metroButtonStart = QPushButton(self.tabMetro)
        self.metroButtonStart.setObjectName(u"metroButtonStart")
        self.metroButtonStart.setCursor(QCursor(Qt.PointingHandCursor))
        self.metroButtonStart.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.metroButtonStart, 4, 1, 1, 1)

        self.metroProgressbar = QProgressBar(self.tabMetro)
        self.metroProgressbar.setObjectName(u"metroProgressbar")
        self.metroProgressbar.setMaximum(1000)
        self.metroProgressbar.setValue(0)
        self.metroProgressbar.setTextVisible(False)

        self.gridLayout_4.addWidget(self.metroProgressbar, 4, 0, 1, 1)

        self.metroLabelFPS = QLabel(self.tabMetro)
        self.metroLabelFPS.setObjectName(u"metroLabelFPS")
        sizePolicy1.setHeightForWidth(self.metroLabelFPS.sizePolicy().hasHeightForWidth())
        self.metroLabelFPS.setSizePolicy(sizePolicy1)
        self.metroLabelFPS.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.metroLabelFPS, 1, 1, 1, 1)

        self.metroCheckboxSimulate = QCheckBox(self.tabMetro)
        self.metroCheckboxSimulate.setObjectName(u"metroCheckboxSimulate")
        self.metroCheckboxSimulate.setCursor(QCursor(Qt.PointingHandCursor))
        self.metroCheckboxSimulate.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.metroCheckboxSimulate, 1, 0, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 3)
        self.gridLayout_4.setColumnStretch(1, 2)

        self.gridLayout_8.addLayout(self.gridLayout_4, 3, 0, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.metroLabelBPM = QLabel(self.tabMetro)
        self.metroLabelBPM.setObjectName(u"metroLabelBPM")
        sizePolicy1.setHeightForWidth(self.metroLabelBPM.sizePolicy().hasHeightForWidth())
        self.metroLabelBPM.setSizePolicy(sizePolicy1)

        self.gridLayout_9.addWidget(self.metroLabelBPM, 0, 0, 1, 1)

        self.metroLabelSignature = QLabel(self.tabMetro)
        self.metroLabelSignature.setObjectName(u"metroLabelSignature")

        self.gridLayout_9.addWidget(self.metroLabelSignature, 0, 3, 1, 1)

        self.metroSpinboxBPM = QDoubleSpinBox(self.tabMetro)
        self.metroSpinboxBPM.setObjectName(u"metroSpinboxBPM")
        self.metroSpinboxBPM.setMaximum(1000.000000000000000)
        self.metroSpinboxBPM.setSingleStep(5.000000000000000)
        self.metroSpinboxBPM.setValue(180.000000000000000)

        self.gridLayout_9.addWidget(self.metroSpinboxBPM, 0, 1, 1, 1)

        self.metroComboboxSignature = QComboBox(self.tabMetro)
        self.metroComboboxSignature.addItem("")
        self.metroComboboxSignature.addItem("")
        self.metroComboboxSignature.addItem("")
        self.metroComboboxSignature.addItem("")
        self.metroComboboxSignature.addItem("")
        self.metroComboboxSignature.addItem("")
        self.metroComboboxSignature.addItem("")
        self.metroComboboxSignature.setObjectName(u"metroComboboxSignature")
        self.metroComboboxSignature.setCursor(QCursor(Qt.PointingHandCursor))
        self.metroComboboxSignature.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_9.addWidget(self.metroComboboxSignature, 0, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 0, 2, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_9, 1, 0, 1, 1)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.metroLabelVolume = QLabel(self.tabMetro)
        self.metroLabelVolume.setObjectName(u"metroLabelVolume")
        sizePolicy1.setHeightForWidth(self.metroLabelVolume.sizePolicy().hasHeightForWidth())
        self.metroLabelVolume.setSizePolicy(sizePolicy1)

        self.gridLayout_15.addWidget(self.metroLabelVolume, 0, 0, 1, 1)

        self.metroSliderVolume = QSlider(self.tabMetro)
        self.metroSliderVolume.setObjectName(u"metroSliderVolume")
        self.metroSliderVolume.setCursor(QCursor(Qt.PointingHandCursor))
        self.metroSliderVolume.setMaximum(100)
        self.metroSliderVolume.setSingleStep(5)
        self.metroSliderVolume.setPageStep(20)
        self.metroSliderVolume.setValue(70)
        self.metroSliderVolume.setOrientation(Qt.Horizontal)

        self.gridLayout_15.addWidget(self.metroSliderVolume, 0, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_15, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tabMetro, "")
        self.tabAbout = QWidget()
        self.tabAbout.setObjectName(u"tabAbout")
        self.gridLayout_3 = QGridLayout(self.tabAbout)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.aboutLabelTitle = QLabel(self.tabAbout)
        self.aboutLabelTitle.setObjectName(u"aboutLabelTitle")
        self.aboutLabelTitle.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.aboutLabelTitle, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabAbout, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 2)

        self.gridLayout.setColumnStretch(0, 5)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 405, 26))
        self.menuMenu = QMenu(self.menuBar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuBPM_Tap = QMenu(self.menuMenu)
        self.menuBPM_Tap.setObjectName(u"menuBPM_Tap")
        self.menuBPM_Calculator = QMenu(self.menuMenu)
        self.menuBPM_Calculator.setObjectName(u"menuBPM_Calculator")
        self.menuBPM_Metronome = QMenu(self.menuMenu)
        self.menuBPM_Metronome.setObjectName(u"menuBPM_Metronome")
        MainWindow.setMenuBar(self.menuBar)
        QWidget.setTabOrder(self.tabWidget, self.tapRadio1)
        QWidget.setTabOrder(self.tapRadio1, self.tapRadio2)
        QWidget.setTabOrder(self.tapRadio2, self.tapRadio3)
        QWidget.setTabOrder(self.tapRadio3, self.tapRadio4)
        QWidget.setTabOrder(self.tapRadio4, self.tapSpinboxAmount)
        QWidget.setTabOrder(self.tapSpinboxAmount, self.calcRadio1)
        QWidget.setTabOrder(self.calcRadio1, self.calcRadio2)
        QWidget.setTabOrder(self.calcRadio2, self.calcRadio3)
        QWidget.setTabOrder(self.calcRadio3, self.calcRadio4)
        QWidget.setTabOrder(self.calcRadio4, self.calcSpinboxValue)
        QWidget.setTabOrder(self.calcSpinboxValue, self.calcComboboxValue)
        QWidget.setTabOrder(self.calcComboboxValue, self.metroRadio1)
        QWidget.setTabOrder(self.metroRadio1, self.metroRadio2)
        QWidget.setTabOrder(self.metroRadio2, self.metroRadio3)
        QWidget.setTabOrder(self.metroRadio3, self.metroRadio4)
        QWidget.setTabOrder(self.metroRadio4, self.metroSpinboxBPM)
        QWidget.setTabOrder(self.metroSpinboxBPM, self.metroComboboxSignature)
        QWidget.setTabOrder(self.metroComboboxSignature, self.metroSliderVolume)

        self.menuBar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.menuBPM_Tap.menuAction())
        self.menuMenu.addAction(self.menuBPM_Calculator.menuAction())
        self.menuMenu.addAction(self.menuBPM_Metronome.menuAction())
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit)
        self.menuBPM_Tap.addAction(self.actionTapT)
        self.menuBPM_Tap.addAction(self.actionTapZ)
        self.menuBPM_Tap.addAction(self.actionTapX)
        self.menuBPM_Tap.addAction(self.actionTapReset)
        self.menuBPM_Calculator.addAction(self.actionGo)
        self.menuBPM_Metronome.addAction(self.actionStart)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.metroComboboxSignature.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"bpmcalc by luxmiyu", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionTapT.setText(QCoreApplication.translate("MainWindow", u"Tap T", None))
#if QT_CONFIG(shortcut)
        self.actionTapT.setShortcut(QCoreApplication.translate("MainWindow", u"T", None))
#endif // QT_CONFIG(shortcut)
        self.actionTapZ.setText(QCoreApplication.translate("MainWindow", u"Tap Z", None))
#if QT_CONFIG(shortcut)
        self.actionTapZ.setShortcut(QCoreApplication.translate("MainWindow", u"Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionTapX.setText(QCoreApplication.translate("MainWindow", u"Tap X", None))
#if QT_CONFIG(shortcut)
        self.actionTapX.setShortcut(QCoreApplication.translate("MainWindow", u"X", None))
#endif // QT_CONFIG(shortcut)
        self.actionTapReset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
#if QT_CONFIG(shortcut)
        self.actionTapReset.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
#endif // QT_CONFIG(shortcut)
        self.actionGo.setText(QCoreApplication.translate("MainWindow", u"Go", None))
#if QT_CONFIG(shortcut)
        self.actionGo.setShortcut(QCoreApplication.translate("MainWindow", u"G", None))
#endif // QT_CONFIG(shortcut)
        self.actionStart.setText(QCoreApplication.translate("MainWindow", u"Start / Stop", None))
#if QT_CONFIG(shortcut)
        self.actionStart.setShortcut(QCoreApplication.translate("MainWindow", u"P", None))
#endif // QT_CONFIG(shortcut)
        self.tapButtonReset.setText(QCoreApplication.translate("MainWindow", u"Reset [R]", None))
        self.tapLabelAmount.setText(QCoreApplication.translate("MainWindow", u"# taps:", None))
        self.tapButtonTap.setText(QCoreApplication.translate("MainWindow", u"Tap [T, Z, X]", None))
        self.tapLabelDetails.setText(QCoreApplication.translate("MainWindow", u"Waiting for taps...", None))
        self.tapRadio2.setText(QCoreApplication.translate("MainWindow", u"1/2", None))
        self.tapRadio1.setText(QCoreApplication.translate("MainWindow", u"1/1", None))
        self.tapLabelRhythm.setText(QCoreApplication.translate("MainWindow", u"Tap Rhythm:", None))
        self.tapRadio3.setText(QCoreApplication.translate("MainWindow", u"1/3", None))
        self.tapRadio4.setText(QCoreApplication.translate("MainWindow", u"1/4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTap), QCoreApplication.translate("MainWindow", u"BPM Tap", None))
        self.calcRadio2.setText(QCoreApplication.translate("MainWindow", u"1/2", None))
        self.calcRadio4.setText(QCoreApplication.translate("MainWindow", u"1/4", None))
        self.calcRadio3.setText(QCoreApplication.translate("MainWindow", u"1/3", None))
        self.calcRadio1.setText(QCoreApplication.translate("MainWindow", u"1/1", None))
        self.calcLabelRhythm.setText(QCoreApplication.translate("MainWindow", u"Tap Rhythm:", None))
        self.calcComboboxValue.setItemText(0, QCoreApplication.translate("MainWindow", u"BPM", None))
        self.calcComboboxValue.setItemText(1, QCoreApplication.translate("MainWindow", u"ms/tap", None))
        self.calcComboboxValue.setItemText(2, QCoreApplication.translate("MainWindow", u"taps/s", None))

        self.calcLabelValue.setText(QCoreApplication.translate("MainWindow", u"Base Value", None))
        self.calcButtonGo.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.calcTextResult.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCalc), QCoreApplication.translate("MainWindow", u"BPM Calculator", None))
        self.metroRadio2.setText(QCoreApplication.translate("MainWindow", u"1/2", None))
        self.metroRadio3.setText(QCoreApplication.translate("MainWindow", u"1/3", None))
        self.metroRadio1.setText(QCoreApplication.translate("MainWindow", u"1/1", None))
        self.metroLabelRhythm.setText(QCoreApplication.translate("MainWindow", u"Tap Rhythm:", None))
        self.metroRadio4.setText(QCoreApplication.translate("MainWindow", u"1/4", None))
        self.metroButtonStart.setText(QCoreApplication.translate("MainWindow", u"Start / Stop [P]", None))
        self.metroLabelFPS.setText(QCoreApplication.translate("MainWindow", u"0 ms/t, 0 tps", None))
        self.metroCheckboxSimulate.setText(QCoreApplication.translate("MainWindow", u"Simulate BPM Tap", None))
        self.metroLabelBPM.setText(QCoreApplication.translate("MainWindow", u"BPM:", None))
        self.metroLabelSignature.setText(QCoreApplication.translate("MainWindow", u"Time Signature:", None))
        self.metroComboboxSignature.setItemText(0, QCoreApplication.translate("MainWindow", u"3/4", None))
        self.metroComboboxSignature.setItemText(1, QCoreApplication.translate("MainWindow", u"4/4", None))
        self.metroComboboxSignature.setItemText(2, QCoreApplication.translate("MainWindow", u"5/4", None))
        self.metroComboboxSignature.setItemText(3, QCoreApplication.translate("MainWindow", u"6/4", None))
        self.metroComboboxSignature.setItemText(4, QCoreApplication.translate("MainWindow", u"7/4", None))
        self.metroComboboxSignature.setItemText(5, QCoreApplication.translate("MainWindow", u"8/4", None))
        self.metroComboboxSignature.setItemText(6, QCoreApplication.translate("MainWindow", u"9/4", None))

        self.metroComboboxSignature.setCurrentText(QCoreApplication.translate("MainWindow", u"4/4", None))
        self.metroLabelVolume.setText(QCoreApplication.translate("MainWindow", u"Volume:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMetro), QCoreApplication.translate("MainWindow", u"BPM Metronome", None))
        self.aboutLabelTitle.setText(QCoreApplication.translate("MainWindow", u"BPM Calculator by luxmiyu v1.0.727", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAbout), QCoreApplication.translate("MainWindow", u"About", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuBPM_Tap.setTitle(QCoreApplication.translate("MainWindow", u"BPM Tap", None))
        self.menuBPM_Calculator.setTitle(QCoreApplication.translate("MainWindow", u"BPM Calculator", None))
        self.menuBPM_Metronome.setTitle(QCoreApplication.translate("MainWindow", u"BPM Metronome", None))
    # retranslateUi

