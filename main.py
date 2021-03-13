"""
Author:     David Walshe
Date:       13 March 2021
"""

import logging

from src.view.view import MainWindow
from src.controller.controller import Controller

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    """Run the GUI application"""
    Controller().show()
