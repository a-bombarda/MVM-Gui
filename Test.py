from pytestqt.qt_compat import qt_api
import pytest
import time
import threading
from PyQt5.Qt import QTimer
from _pytest.outcomes import fail
from FileToBeTested import *

def test1(qtbot):
  FileToBeTested
