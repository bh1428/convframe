# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maindialog.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from  . import maindialog_rc

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        if not MainDialog.objectName():
            MainDialog.setObjectName(u"MainDialog")
        MainDialog.resize(500, 450)
        MainDialog.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u":/images/images/python-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainDialog.setWindowIcon(icon)
        self.vl_main_dialog = QVBoxLayout(MainDialog)
        self.vl_main_dialog.setSpacing(3)
        self.vl_main_dialog.setObjectName(u"vl_main_dialog")
        self.vl_main_dialog.setContentsMargins(2, 2, 2, 2)
        self.gb_input = QGroupBox(MainDialog)
        self.gb_input.setObjectName(u"gb_input")
        self.hl_gb_input_main = QHBoxLayout(self.gb_input)
        self.hl_gb_input_main.setObjectName(u"hl_gb_input_main")
        self.hl_gb_input_main.setContentsMargins(3, 3, 3, 3)
        self.hl_gb_input = QHBoxLayout()
        self.hl_gb_input.setObjectName(u"hl_gb_input")
        self.hl_gb_input.setContentsMargins(3, 3, 3, 3)
        self.pte_input_text = QPlainTextEdit(self.gb_input)
        self.pte_input_text.setObjectName(u"pte_input_text")
        self.pte_input_text.setAcceptDrops(False)
        self.pte_input_text.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.hl_gb_input.addWidget(self.pte_input_text)

        self.vl_input_buttons = QVBoxLayout()
        self.vl_input_buttons.setObjectName(u"vl_input_buttons")
        self.pb_copy_from_clipb = QPushButton(self.gb_input)
        self.pb_copy_from_clipb.setObjectName(u"pb_copy_from_clipb")

        self.vl_input_buttons.addWidget(self.pb_copy_from_clipb)

        self.hl_imp_enc = QHBoxLayout()
        self.hl_imp_enc.setObjectName(u"hl_imp_enc")
        self.hl_imp_enc.setContentsMargins(5, -1, -1, -1)
        self.lb_imp_enc = QLabel(self.gb_input)
        self.lb_imp_enc.setObjectName(u"lb_imp_enc")

        self.hl_imp_enc.addWidget(self.lb_imp_enc)

        self.cb_imp_enc = QComboBox(self.gb_input)
        self.cb_imp_enc.setObjectName(u"cb_imp_enc")

        self.hl_imp_enc.addWidget(self.cb_imp_enc)


        self.vl_input_buttons.addLayout(self.hl_imp_enc)

        self.pb_import_from_file = QPushButton(self.gb_input)
        self.pb_import_from_file.setObjectName(u"pb_import_from_file")

        self.vl_input_buttons.addWidget(self.pb_import_from_file)

        self.vs_input_buttons = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_input_buttons.addItem(self.vs_input_buttons)

        self.pb_reset = QPushButton(self.gb_input)
        self.pb_reset.setObjectName(u"pb_reset")

        self.vl_input_buttons.addWidget(self.pb_reset)

        self.pb_convert = QPushButton(self.gb_input)
        self.pb_convert.setObjectName(u"pb_convert")

        self.vl_input_buttons.addWidget(self.pb_convert)


        self.hl_gb_input.addLayout(self.vl_input_buttons)


        self.hl_gb_input_main.addLayout(self.hl_gb_input)


        self.vl_main_dialog.addWidget(self.gb_input)

        self.gb_output = QGroupBox(MainDialog)
        self.gb_output.setObjectName(u"gb_output")
        self.hl_gb_output_main = QHBoxLayout(self.gb_output)
        self.hl_gb_output_main.setObjectName(u"hl_gb_output_main")
        self.hl_gb_output_main.setContentsMargins(3, 3, 3, 3)
        self.hl_gb_output = QHBoxLayout()
        self.hl_gb_output.setObjectName(u"hl_gb_output")
        self.hl_gb_output.setContentsMargins(3, 3, 3, 3)
        self.pte_output_text = QPlainTextEdit(self.gb_output)
        self.pte_output_text.setObjectName(u"pte_output_text")
        self.pte_output_text.setAcceptDrops(False)
        self.pte_output_text.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.pte_output_text.setReadOnly(True)

        self.hl_gb_output.addWidget(self.pte_output_text)

        self.vl_output_buttons = QVBoxLayout()
        self.vl_output_buttons.setObjectName(u"vl_output_buttons")
        self.pb_copy_to_clipb = QPushButton(self.gb_output)
        self.pb_copy_to_clipb.setObjectName(u"pb_copy_to_clipb")

        self.vl_output_buttons.addWidget(self.pb_copy_to_clipb)

        self.hl_exp_enc = QHBoxLayout()
        self.hl_exp_enc.setObjectName(u"hl_exp_enc")
        self.hl_exp_enc.setContentsMargins(5, -1, -1, -1)
        self.lb_exp_enc = QLabel(self.gb_output)
        self.lb_exp_enc.setObjectName(u"lb_exp_enc")

        self.hl_exp_enc.addWidget(self.lb_exp_enc)

        self.cb_exp_enc = QComboBox(self.gb_output)
        self.cb_exp_enc.setObjectName(u"cb_exp_enc")

        self.hl_exp_enc.addWidget(self.cb_exp_enc)


        self.vl_output_buttons.addLayout(self.hl_exp_enc)

        self.pb_export_to_file = QPushButton(self.gb_output)
        self.pb_export_to_file.setObjectName(u"pb_export_to_file")

        self.vl_output_buttons.addWidget(self.pb_export_to_file)

        self.vs_output_buttons = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_output_buttons.addItem(self.vs_output_buttons)

        self.pb_about = QPushButton(self.gb_output)
        self.pb_about.setObjectName(u"pb_about")

        self.vl_output_buttons.addWidget(self.pb_about)

        self.pb_exit = QPushButton(self.gb_output)
        self.pb_exit.setObjectName(u"pb_exit")

        self.vl_output_buttons.addWidget(self.pb_exit)


        self.hl_gb_output.addLayout(self.vl_output_buttons)


        self.hl_gb_output_main.addLayout(self.hl_gb_output)


        self.vl_main_dialog.addWidget(self.gb_output)

#if QT_CONFIG(shortcut)
        self.lb_imp_enc.setBuddy(self.cb_imp_enc)
        self.lb_exp_enc.setBuddy(self.cb_exp_enc)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.pte_input_text, self.pb_copy_from_clipb)
        QWidget.setTabOrder(self.pb_copy_from_clipb, self.cb_imp_enc)
        QWidget.setTabOrder(self.cb_imp_enc, self.pb_import_from_file)
        QWidget.setTabOrder(self.pb_import_from_file, self.pb_reset)
        QWidget.setTabOrder(self.pb_reset, self.pb_convert)
        QWidget.setTabOrder(self.pb_convert, self.pb_copy_to_clipb)
        QWidget.setTabOrder(self.pb_copy_to_clipb, self.cb_exp_enc)
        QWidget.setTabOrder(self.cb_exp_enc, self.pb_export_to_file)
        QWidget.setTabOrder(self.pb_export_to_file, self.pb_about)
        QWidget.setTabOrder(self.pb_about, self.pb_exit)
        QWidget.setTabOrder(self.pb_exit, self.pte_output_text)

        self.retranslateUi(MainDialog)

        QMetaObject.connectSlotsByName(MainDialog)
    # setupUi

    def retranslateUi(self, MainDialog):
        MainDialog.setWindowTitle(QCoreApplication.translate("MainDialog", u"Dialog", None))
        self.gb_input.setTitle(QCoreApplication.translate("MainDialog", u"Input", None))
#if QT_CONFIG(tooltip)
        self.pb_copy_from_clipb.setToolTip(QCoreApplication.translate("MainDialog", u"<html><head/><body><p>Copy information on the clipboard to the input area.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_copy_from_clipb.setText(QCoreApplication.translate("MainDialog", u"Paste from Clipboard", None))
        self.lb_imp_enc.setText(QCoreApplication.translate("MainDialog", u"Enc:", None))
#if QT_CONFIG(tooltip)
        self.pb_import_from_file.setToolTip(QCoreApplication.translate("MainDialog", u"<html><head/><body><p>Import the content from a file into the input area (file encoding can be selected).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_import_from_file.setText(QCoreApplication.translate("MainDialog", u"Import from File", None))
#if QT_CONFIG(tooltip)
        self.pb_reset.setToolTip(QCoreApplication.translate("MainDialog", u"<html><head/><body><p>Remove the content of in- and output area and reset the options.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_reset.setText(QCoreApplication.translate("MainDialog", u"Reset", None))
#if QT_CONFIG(tooltip)
        self.pb_convert.setToolTip(QCoreApplication.translate("MainDialog", u"<html><head/><body><p>Perform the conversion from input to output.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_convert.setText(QCoreApplication.translate("MainDialog", u"Convert", None))
        self.gb_output.setTitle(QCoreApplication.translate("MainDialog", u"Output", None))
#if QT_CONFIG(tooltip)
        self.pb_copy_to_clipb.setToolTip(QCoreApplication.translate("MainDialog", u"<html><head/><body><p>Copy the output area as text to the clipboard.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_copy_to_clipb.setText(QCoreApplication.translate("MainDialog", u"Copy to Clipboard", None))
        self.lb_exp_enc.setText(QCoreApplication.translate("MainDialog", u"Enc.:", None))
#if QT_CONFIG(tooltip)
        self.pb_export_to_file.setToolTip(QCoreApplication.translate("MainDialog", u"<html><head/><body><p>Export the content of the output area to a file (file encoding can be selected).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_export_to_file.setText(QCoreApplication.translate("MainDialog", u"Export to File", None))
#if QT_CONFIG(tooltip)
        self.pb_about.setToolTip(QCoreApplication.translate("MainDialog", u"<html><head/><body><p>Get version information.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_about.setText(QCoreApplication.translate("MainDialog", u"About", None))
#if QT_CONFIG(tooltip)
        self.pb_exit.setToolTip(QCoreApplication.translate("MainDialog", u"<html><head/><body><p>Leave program.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_exit.setText(QCoreApplication.translate("MainDialog", u"Exit", None))
    # retranslateUi

