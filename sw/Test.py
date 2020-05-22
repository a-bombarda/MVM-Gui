#!/usr/bin/env python3

from pytestqt.qt_compat import qt_api
import pytest
import time
import threading
from PyQt5.Qt import QTimer
from _pytest.outcomes import fail
from FileToBeTested import DataFiller

def test_test1(qtbot):
  assert qt_api.QApplication.instance() is not None
  DataFiller.stampa()
  assert True
