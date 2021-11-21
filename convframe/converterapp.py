#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""main entry point for converterframework

converterapp is a PyQt based framework for simple text converters
"""
import sys

from PySide6 import QtWidgets

from .common import __version__
from .maindialog import MainDialog, Converter


class ConverterApp:
    """Base class for a Converter Framework based application"""

    default_about_text = "<br>".join(
        (
            f"<b>ConverterFrameWork</b> V{__version__}",
            "(c) Copyright 2006-2021 by Ben Hattem (benghattem@gmail.com)",
            "",
        )
    )
    default_import_filter = "All files (*.*)"
    default_export_filter = "Text files (*.txt);;All files (*.*)"
    default_file_encodings = ("utf-8", "cp1252", "iso-8859-1", "utf-16")

    def __init__(
        self,
        app_name,
        about_text="",
        converter=Converter,
        import_filter=default_import_filter,
        export_filter=default_export_filter,
        file_encodings=default_file_encodings,
    ):

        # attributes
        self.app_name = app_name
        self.about_text = ConverterApp.default_about_text
        if len(about_text) > 0:
            self.about_text = "<br>".join((self.about_text, about_text))
        self.converter = converter
        self.import_filter = import_filter
        self.export_filter = export_filter
        self.file_encodings = file_encodings

        # initialize and start the application
        self.app = QtWidgets.QApplication(sys.argv)
        self.dialog = MainDialog(
            self.app_name,
            self.about_text,
            self.converter,
            self.import_filter,
            self.export_filter,
            self.file_encodings,
        )
        self.dialog.show()
        sys.exit(self.app.exec_())
