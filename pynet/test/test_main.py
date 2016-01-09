__author__ = 'eric'

import pytest

from pynet import main as m

def test_add():
    assert m.add(2, 3) == 5
