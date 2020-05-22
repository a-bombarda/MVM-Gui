#!/usr/bin/env python3

# from pytestqt import qt_compat
from pytestqt.qt_compat import qt_api
import pytest
import time
import re
from PyQt5.QtCore import QCoreApplication
from .FileToBeTested import DataFiller


def test_expiratoryPause(qtbot):
	assert qt_api.QApplication.instance() is not None
	a = 2
	DataFiller.stampa()
	assert True

    