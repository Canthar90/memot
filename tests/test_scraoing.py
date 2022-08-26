import sys
import pytest
import requests
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from scraping import Scrapping


# ---------------Test Scrapping-------------------
def test_pancerni_scrapping_passes():
    """Test if Scraping of pancerniaki works correctly"""
    scraping = Scrapping()
    assert "Najbliższe odcinki 4" in scraping.pancernioki() 


def test_pancerni_scrapping_fails():
    """Test if Scraping of pancerniaki rises TypeError when unexpected argument passed"""
    scrapping = Scrapping()
    with pytest.raises(TypeError) as err:
        scrapping.pancernioki("any argument")
    assert "takes 1 positional argument" in str(err.value)