#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Example of an application using the ConverterFramework"""
# TODO: change description in above line

import convframe
from PySide2 import QtWidgets

__version__ = "2020.4.11"

#
# Name the application
#
# TODO: change name of the application and copyright
APPNAME = "Application Name"
COPYRIGHT = "(c) Copyright 2020 by Ben Hattem"

#
# file filters to be used for file import and export
#
# TODO: define wildcards for import / export of files
IMPORT_FILTER = ";;".join((convframe.ConverterApp.default_import_filter, "Text files (*.txt)"))
EXPORT_FILTER = convframe.ConverterApp.default_export_filter

#
# possible file encodings for the file export
#
# TODO: adapt file encodings when required
FILE_ENCODINGS = ["utf-8", "cp1252", "iso-8859-1", "utf-16"]

#
# text for the About popup
#
# TODO: change about text
ABOUT_TEXT = "<br>".join(
    (f"<b>{APPNAME}</b> V{__version__}", COPYRIGHT, "", "Description of the application goes here.",)
)

#
# conversion class
#
# TODO: rename converter class to something meaningful
# TODO: remove example code
class ExampleConverter(convframe.Converter):
    """TODO: describe the converter class"""

    def get_options_dialog(self):
        """Return a dialog (type=QLayout) for converter config."""
        # TODO: adept dialog, return None if no dialog is required
        # first options line
        self.cb_upper_case = QtWidgets.QCheckBox("Convert to UPPER Case")
        self.hl_line_1 = QtWidgets.QHBoxLayout()
        self.hl_line_1.addWidget(self.cb_upper_case)
        self.hl_line_1.addStretch()
        # second options line
        self.cb_title_case = QtWidgets.QCheckBox("Title Case")
        self.lb_arrow = QtWidgets.QLabel(" -> ")
        self.cb_swap_case = QtWidgets.QCheckBox("Swap Case")
        self.hl_line_2 = QtWidgets.QHBoxLayout()
        self.hl_line_2.addWidget(self.cb_title_case)
        self.hl_line_2.addWidget(self.lb_arrow)
        self.hl_line_2.addWidget(self.cb_swap_case)
        self.hl_line_2.addStretch()
        # main sizer (to be linked to parent)
        self.vl_main = QtWidgets.QVBoxLayout()
        self.vl_main.setContentsMargins(3, 3, 3, 3)
        self.vl_main.addLayout(self.hl_line_1)
        self.vl_main.addLayout(self.hl_line_2)
        # bind signals
        self.cb_upper_case.clicked.connect(self.check_upper_case)
        self.cb_title_case.clicked.connect(self.check_title_case)
        self.cb_swap_case.clicked.connect(self.check_swap_case)
        # return the main sizer
        return self.vl_main

    def reset_options(self):
        """Reset all options in the converter specific options dialog."""
        # TODO: remove or adapt
        self.cb_upper_case.setChecked(True)
        self.cb_title_case.setChecked(False)
        self.cb_swap_case.setChecked(False)

    def check_upper_case(self):
        """Do not capitalize or swapcase if uppercase is selected."""
        # TODO: remove or adapt
        self.cb_upper_case.setChecked(True)
        self.cb_title_case.setChecked(False)
        self.cb_swap_case.setChecked(False)

    def check_title_case(self):
        """Convert to title case only if uppercase is not checked."""
        # TODO: remove or adapt
        if self.cb_upper_case.isChecked() and self.cb_title_case.isChecked():
            self.cb_upper_case.setChecked(False)

    def check_swap_case(self):
        """Only swap case if uppercase is not checked."""
        # TODO: remove or adapt
        if self.cb_upper_case.isChecked() and self.cb_swap_case.isChecked():
            self.cb_upper_case.setChecked(False)

    def convert(self, data):
        """Perform the conversion operation"""
        # TODO: implement convert method (remove example code)
        work = data
        if self.cb_upper_case.isChecked():
            work = work.upper()
        if self.cb_title_case.isChecked():
            work = work.title()
        if self.cb_swap_case.isChecked():
            work = work.swapcase()
        if not work:
            self.parent.show_error("No output", "No output generated")
        return work


def main():
    """start the Converter Framework based app"""
    # TODO: adapt main application call if required"""
    convframe.ConverterApp(
        APPNAME,
        ABOUT_TEXT,
        converter=ExampleConverter,
        import_filter=IMPORT_FILTER,
        export_filter=EXPORT_FILTER,
        file_encodings=FILE_ENCODINGS,
    )


if __name__ == "__main__":
    main()
