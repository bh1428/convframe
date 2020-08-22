#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""main dialog for converterframework

converterframework is a PyQt based framework for simple text converters
"""

import pathlib as pl

from PySide2 import QtCore, QtWidgets

from .ui_maindialog import Ui_MainDialog


class Converter(QtWidgets.QLayout):
    """A (dummy) class for the conversion"""

    def __init__(self, parent):
        # initialize UI
        super(Converter, self).__init__()
        self.parent = parent

    def get_options_dialog(self):
        """Return an (optional) dialog (type=QLayout) for converter config."""
        return None

    def reset_options(self):
        """Reset the options in the (optional) dialog."""
        pass

    def convert(self, data):
        """Perform the conversion."""
        return data


def correct_encoding(encoding):
    """Correct encoding

    UTF-8 uses an optional BOM (0xef, 0xbb, 0xbf). We always want to use that
    because it prevents errors. The codepage to use would then be UTF-8-SIG
    instead of UTF-8. However, UTF-8-SIG is an ugly name, so we just use UTF-8
    as name and correct it where required.

    Arguments:
        encoding    codepage string to be checked

    Return:
        corrected codepage as string
    """
    in_encoding = str(encoding)
    out_encoding = in_encoding

    in_encoding = in_encoding.upper().replace("-", "")
    if in_encoding.startswith("UTF8"):
        # always use UTF-8-SIG instead of UTF-8
        out_encoding = "utf-8-sig"

    return out_encoding


def get_max_width(*layouts):
    """Get the maximum width of the children of a layout."""
    max_width = 0
    for layout in layouts:
        widgets = (layout.itemAt(i) for i in range(layout.count()))
        for widget in widgets:
            width = widget.sizeHint().width()
            if width > max_width:
                max_width = width
    return max_width


class MainDialog(QtWidgets.QDialog, Ui_MainDialog):
    """Main dialog for the Converter Framework"""

    # default window title
    title = "Converter Framework"

    # default encodings to be used
    default_encodings = ("utf-8", "cp1252")

    def __init__(
        self,
        title=title,
        about_text="",
        converter=Converter,
        import_filter="",
        export_filter="",
        file_encodings=default_encodings,
    ):

        # initialize UI
        super(MainDialog, self).__init__()
        self.setupUi(self)

        # initialise attributes
        self.title = title
        self.about_text = about_text
        self.converter = converter(self)
        self.import_filter = import_filter
        self.export_filter = export_filter
        self.default_file_encodings = file_encodings
        self.default_output_fn = "output"

        # start with an undefined options dialog
        self.options = None

        # UI specific initialization
        self.initialize_ui()

        # get a handle to the clipboard
        self.clipboard = QtWidgets.QApplication.clipboard()

    def initialize_ui(self):
        """Initialise the user interface."""
        # configure title bar
        self.setWindowTitle(self.title)
        self.setWindowFlags(
            QtCore.Qt.Dialog
            | QtCore.Qt.WindowMinimizeButtonHint
            | QtCore.Qt.WindowMaximizeButtonHint
            | QtCore.Qt.WindowCloseButtonHint
        )

        # populate file encodings
        self.cb_imp_enc.addItems(self.default_file_encodings)
        self.cb_exp_enc.addItems(self.default_file_encodings)

        # make buttons areas same width
        new_width = get_max_width(self.vl_input_buttons, self.vl_output_buttons)
        self.pb_copy_from_clipb.setFixedWidth(new_width)
        self.pb_export_to_file.setFixedWidth(new_width)

        # add (optional) options from the converter object
        self.options = self.converter.get_options_dialog()
        if self.options:
            if isinstance(self.options, QtWidgets.QLayout):
                self.options_box = QtWidgets.QGroupBox("Option(s)", self)
                self.options_box.setLayout(self.options)
                self.vl_main_dialog.insertWidget(0, self.options_box)
            else:
                self.show_error(
                    "Convert dialog error",
                    "The converter should return a QLayout object from\n"
                    + "its get_options_dialog() method.\n\n"
                    + f'We got an object of type "{type(self.options)}"\n'
                    + "which is not usable as a converter configuration dialog.",
                )

        # signals and slots
        self.pb_copy_from_clipb.clicked.connect(self.on_pb_copy_from_clipb_clicked)
        self.pb_import_from_file.clicked.connect(self.on_pb_import_from_file_clicked)
        self.pb_reset.clicked.connect(self.on_pb_reset_clicked)
        self.pb_convert.clicked.connect(self.on_pb_convert_clicked)
        self.pb_copy_to_clipb.clicked.connect(self.on_pb_copy_to_clipb_clicked)
        self.pb_export_to_file.clicked.connect(self.on_pb_export_to_file_clicked)
        self.pb_about.clicked.connect(self.on_pb_about_clicked)
        self.pb_exit.clicked.connect(self.on_pb_exit_clicked)

        # make sure dialog options are set to the correct state
        self.on_pb_reset_clicked()

    def show_error(self, title, text):
        """Show a modal error information dialog."""
        QtWidgets.QMessageBox.critical(self, title, text)

    def dragEnterEvent(self, event):
        """Accept drag events only for URLs (i.e. filenames) and text."""
        mimedata = event.mimeData()
        if mimedata.hasUrls() or mimedata.hasText():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        """Handle a drop event (i.e. import file or copy normal text)."""
        mimedata = event.mimeData()
        if mimedata.hasUrls():
            filenames = []
            for url in mimedata.urls():
                path = pl.Path(url.toLocalFile())
                if path.is_file():
                    filenames.append(str(path))
            self.import_files(filenames)
        elif mimedata.hasText():
            self.pte_input_text.insertPlainText(mimedata.text())

    def import_files(self, filenames):
        """Import the content of one or more files into the input area"""
        new_input = ""
        for filename in filenames:
            try:
                encoding = correct_encoding(self.cb_imp_enc.currentText())
                with open(filename, "r", encoding=encoding) as f:
                    file_content = f.read()
                new_input = "".join([new_input, file_content])
            except (UnicodeDecodeError, UnicodeError):
                self.show_error("Import conversion error", "Codepage error: please set correct input encoding")
            except IOError:
                self.show_error("File I/O Error", f'Could not read from file:\n"{filename}"')
        self.pte_input_text.setPlainText(new_input)

    def on_pb_copy_from_clipb_clicked(self):
        """Handle click on the "Copy from Clipboard" button."""
        self.pte_input_text.setPlainText(self.clipboard.text())

    def on_pb_import_from_file_clicked(self):
        """Handle click on the "Import from File" button."""
        # get the filename(s) and read the file(s)
        filenames, dummy = QtWidgets.QFileDialog.getOpenFileNames(
            self, "Open File(s)", str(pl.Path.cwd()), self.import_filter
        )
        if filenames:
            self.import_files(filenames)

    def on_pb_reset_clicked(self):
        """Handle click on the "Reset" button."""
        # reset in- and output text areas
        self.pte_input_text.setPlainText("")
        self.pte_output_text.setPlainText("")
        self.cb_imp_enc.setCurrentIndex(0)
        self.cb_exp_enc.setCurrentIndex(0)
        if self.options:
            self.converter.reset_options()

    def on_pb_convert_clicked(self):
        """Handle click on the "Convert" button."""
        self.pte_output_text.setPlainText(self.converter.convert(str(self.pte_input_text.toPlainText())))

    def on_pb_copy_to_clipb_clicked(self):
        """Handle click on the "Copy to Clipboard" button."""
        self.clipboard.setText(self.pte_output_text.toPlainText())

    def on_pb_export_to_file_clicked(self):
        """Handle click on the "Export to File" button."""
        # write output area to a file
        directory = pl.Path.cwd() / pl.Path(self.default_output_fn)
        out_filename, dummy = QtWidgets.QFileDialog.getSaveFileName(
            parent=self, caption="Save As", dir=str(directory), filter=self.export_filter
        )
        if out_filename:
            encoding = correct_encoding(self.cb_exp_enc.currentText())
            try:
                with open(out_filename, mode="w", encoding=encoding) as f:
                    text = str(self.pte_output_text.toPlainText())
                    f.write(text)
            except IOError:
                self.show_error("File I/O Error", f'Could not write to file:\n"{out_filename}"')

    def on_pb_about_clicked(self):
        """Handle click on the "About" button."""
        QtWidgets.QMessageBox.about(self, "About", self.about_text)

    def on_pb_exit_clicked(self):
        """Handle click on the "Exit" button."""
        self.close()
