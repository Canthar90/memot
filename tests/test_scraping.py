import sys
import pytest
import requests
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from scraping import Scrapping, Allegro_scrapping


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
    
    
# -----------------Test Allegro scraping-------------------------
@pytest.mark.parametrize("keyword,nr_of_results,flag", [
    ("kopytko", 1, False), ("kopytko", 10, False), ("kopytko", 10, True)
])    
def test_allegro_scrapping_passes_with_valid_arguments(keyword, nr_of_results, flag):
    """Test if Allegro scraping works correctly with two valid arguments passed"""
    allegro_scraping = Allegro_scrapping()
    resp = allegro_scraping.search(keyword, nr_of_results, flag)
    assert "Tytuł to" in resp and "link" in resp 
    
    
@pytest.mark.parametrize("keyword,nr_of_results,flag", [
    ("adweqeedasfaw", 1, False), ("kopytko", 0, False),
])
def test_allegro_scrapping_fails_nonsence_arguments(keyword, nr_of_results, flag):
    """Test if Allegro scraping fails with invalid arguments"""
    allegro_scraping = Allegro_scrapping()
    resp = allegro_scraping.search(keyword, nr_of_results, flag)
    assert "Nie było wystarczająco dużo" in resp or "Sory nie mogę znaleźć" in resp
    
    
@pytest.mark.parametrize("keyword,nr_of_results,flag", [
    ("kopytko", "string", False), ("kopytko", 10, "string"), ("kopytko", False, False),
    ("kopytko", 1, 123), (12313213214214123, 1, False),
])
def test_allegro_scrapping_fails_invalid_datatypes(keyword, nr_of_results, flag):
    """Tet if Allegro scraping rises exception when bad data types passed"""
    allegro_scraping = Allegro_scrapping()
    with pytest.raises(ValueError) as err:
        allegro_scraping.search(keyword, nr_of_results, flag)
    assert "Invalid data type" in str(err.value)
    