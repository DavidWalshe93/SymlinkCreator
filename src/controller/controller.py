"""
Author:     David Walshe
Date:       13 March 2021
"""

import logging
import os
from typing import Type
import subprocess as sub

from PyQt5.QtWidgets import QFileDialog, QApplication

from src.view.view import MainWindow

logger = logging.getLogger(__name__)


class Controller:

    def __init__(self):
        """Controller constructor"""
        self.view: MainWindow = None

    def setup(self):
        """Setup the view and add in callback functionality"""
        # Add path selectors.
        self.view.pushButtonLinkPath.clicked.connect(self.get_link_path_cb)
        self.view.pushButtonTargetPath.clicked.connect(self.get_target_path_cb)

        # Add symlink creation.
        self.view.pushButtonCreateSymlink.clicked.connect(self.create_symlink_cb)

        # Add in initial text for path.
        self.view.lineEditLinkPath.setText(os.getcwd())

    def show(self):
        """Construct and show the GUI application."""
        try:
            app = QApplication([])
            self.view = MainWindow()
            self.setup()
            self.view.show()

            app.exec_()
        except Exception as err:
            raise err

    def get_link_path_cb(self) -> None:
        """Get and set the path for the link path."""
        link_path = self.get_path_from_file_handler()
        self.view.lineEditLinkPath.setText(link_path)

    def get_target_path_cb(self) -> None:
        """Get and set the path for the target path."""
        target_path = self.get_path_from_file_handler()
        self.view.lineEditTargetPath.setText(target_path)

    @staticmethod
    def get_path_from_file_handler() -> str:
        """Return a directory path the user selects."""
        file_name = QFileDialog.getExistingDirectory(None, "Select Directory")

        if file_name:
            return file_name
        else:
            return os.getcwd()

    @property
    def link_name(self) -> str:
        return self.view.lineEditLinkName.text()

    @property
    def link(self) -> str:
        return os.path.join(self.view.lineEditLinkPath.text(), self.link_name)

    @property
    def target(self) -> str:
        return self.view.lineEditTargetPath.text()

    def create_symlink_cb(self):
        """Create a symlink on the filesystem."""
        try:
            # Call the symlink cmd function.
            proc = sub.Popen(f'mklink /D "{self.link}" "{self.target}"', shell=True, stdout=sub.PIPE, stderr=sub.PIPE)
            out, err = proc.communicate()
            # Show the output and err of the command.
            if out:
                self.view.plainTextEditLog.setPlainText(f"OUT:: {str(out, encoding='utf8')}")
            if err:
                self.view.plainTextEditLog.appendPlainText(f"\nERR:: {str(err, encoding='utf8')}")
        except sub.SubprocessError as err:
            self.view.plainTextEditLog.setPlainText(err.__str__())
        except Exception as err:
            raise err
