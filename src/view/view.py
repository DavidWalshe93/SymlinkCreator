"""
Author:     David Walshe
Date:       13 March 2021
"""

import logging

from PyQt5.QtWidgets import QMainWindow

from src.view.core.main_view import Ui_MainWindow

logger = logging.getLogger(__name__)


class MainWindow(Ui_MainWindow, QMainWindow):

    def __init__(self, *args, **kwargs):
        """View Constructor"""
        super().__init__(*args, **kwargs)
        self.setupUi(self)
