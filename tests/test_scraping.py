import sys
import pytest
import requests
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from scraping import Scrapping, Allegro_scrapping, XcomScraping


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
@pytest.mark.allegro_testing
@pytest.mark.parametrize("keyword,nr_of_results,flag", [
    ("kopytko", 1, False), ("kopytko", 10, False), ("kopytko", 10, True)
])    
def test_allegro_scrapping_passes_with_valid_arguments(keyword, nr_of_results, flag):
    """Test if Allegro scraping works correctly with two valid arguments passed"""
    allegro_scraping = Allegro_scrapping()
    resp = allegro_scraping.search(keyword, nr_of_results, flag)
    assert "Tytuł to" in resp and "link" in resp 
    

@pytest.mark.allegro_testing    
@pytest.mark.parametrize("keyword,nr_of_results,flag", [
    ("adweqeedasfaw", 1, False), ("kopytko", 0, False),
])
def test_allegro_scrapping_fails_nonsence_arguments(keyword, nr_of_results, flag):
    """Test if Allegro scraping fails with invalid arguments"""
    allegro_scraping = Allegro_scrapping()
    resp = allegro_scraping.search(keyword, nr_of_results, flag)
    assert "Nie było wystarczająco dużo" in resp or "Sory nie mogę znaleźć" in resp
    

@pytest.mark.allegro_testing    
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


@pytest.mark.allegro_testing
def test_allegro_scrapping_fails_to_many_arguments():
    """Test if Allegro scraping rises TypeError when to many arguments passed"""
    allegro_scraping = Allegro_scrapping()
    with pytest.raises(TypeError) as err:
        allegro_scraping.search("kopytko", 1, False, "unnesesary")
    assert "takes from 2 to 4 positional arguments" in str(err.value)
    

@pytest.mark.allegro_testing    
def test_allegro_scrapping_fails_no_args():
    """Test if Allegro scraping rises TypeError when no arguments passed"""
    allegro_scraping = Allegro_scrapping()
    with pytest.raises(TypeError) as err:
        allegro_scraping.search()
    assert "missing 1 required positional argument" in str(err.value)


# ----------------------- Test Xscraping----------------------------
@pytest.mark.xcom_test
@pytest.mark.parametrize("keyword,expected", [("rtx 3070", "Tytuł to"),
("kopytko", "There is no reasults for this phraze")])
def test_xcom_scraping_works_one_argument_passed(keyword, expected):
    """Test if Xcom_scraping works witch one argument passed"""
    xscrap = XcomScraping()
    res = xscrap.search(keyword)
    assert expected in res


@pytest.mark.xcom_test
@pytest.mark.parametrize("keyword,number,expected", [("monitor", 10, "Tytuł to"),
("monitor", 1000000, "There was not enought results"), 
("kopytko", 1, "There is no reasults for this phraze")])
def test_xcom_scraping_works_two_argument_passed(keyword, number, expected):
    """Test if Xcom scraping works witch 2 arguments passed"""
    xscrap = XcomScraping()
    res = xscrap.search(keyword, number)
    assert expected in res


    