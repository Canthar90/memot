from shutil import ExecError
import sys
import pytest
import unittest
import sys
import os


current = os.path.dirname(os.path.realpath(__file__))


parent = os.path.dirname(current)

sys.path.append(parent)

from apis import RandoCatApi

def test_random_cat():
    cats = RandoCatApi()
    assert "http" in cats.get_random_cat()

def test_random_cat_not_pased():
    cats = RandoCatApi()
    with pytest.raises(Exception):
        cats.get_random_cat("this should not be here")
