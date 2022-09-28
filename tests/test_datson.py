import sys
from unittest import mock
import pytest
import os
import datetime as dt

current = os.path.dirname(os.path.realpath(__file__))

parent = os.path.dirname(current)

from datson import Garbagson, Events
from unittest.mock import Mock, patch


# -------------Test Garbage Class------------------
@pytest.fixture
def garbage_data_all():
    current_day = dt.date.today()
    future_4_days = current_day + dt.timedelta(days=4)
    future_8_days = current_day + dt.timedelta(days=8)
    past_4_days = current_day - dt.timedelta(days=4)
    ref_curr = current_day.strftime('%d/%m/%Y')
    ref_futur_4 = future_4_days.strftime('%d/%m/%Y')
    ref_futur_8 = future_8_days.strftime('%d/%m/%Y')
    ref_past_4 = past_4_days.strftime('%d/%m/%Y')
    data = {
        "Unexpected": ["bad/True/Data", ref_curr, ref_futur_4, ref_futur_8, ref_past_4 ],
        "Plastiki": ["bad/True/Data", ref_curr, ref_futur_4, ref_futur_8, ref_past_4],
        "Mieszane": ["bad/True/Data", ref_curr, ref_futur_4, ref_futur_8, ref_past_4],
        "Bio": ["bad/True/Data", ref_curr, ref_futur_4, ref_futur_8, ref_past_4],
        "Gabaryty": ["bad/True/Data", ref_curr, ref_futur_4, ref_futur_8, ref_past_4],
        "Szklo": ["bad/True/Data", ref_curr, ref_futur_4, ref_futur_8, ref_past_4],
        "Popioly": ["bad/True/Data", ref_curr, ref_futur_4, ref_futur_8, ref_past_4]
    }
    return data, ref_curr, ref_futur_4, ref_futur_8,\
         ref_past_4, "bad/True/Data"


@pytest.mark.garbage_test
def test_garbagson_works_fine(garbage_data_all):
    """Test if garbage checking class works fine"""
    data, ref_curr, ref_futur4, ref_futur_8, ref_past_4, bad = garbage_data_all
    garbages = Garbagson()
    garbages.garbage_dict = data
    res = garbages.trash_time()
    assert (ref_curr.replace("/", "-") not in res) and (ref_futur4.replace("/", "-") in res)\
         and (ref_futur_8.replace("/", "-") not in res) and (ref_past_4.replace("/", "-")\
         not in res) and (bad not in res)


@pytest.mark.garbage_test
def test_garbagson_fails_argument_passed():
    """Test if garbage chceckign rises TypeError when argument pased"""
    garbages = Garbagson()
    with pytest.raises(TypeError) as err:
        garbages.trash_time("invalid arg")
    assert "takes 1 positional argument" in str(err.value)


# ------------------Events testing-----------------
@pytest.fixture
def current_day():
    current = dt.date.today()
    ref_current = {"Descriprion1": [current.strftime('%Y-%m-%d'), " " ]}
    out_current = current.strftime('%Y-%m-%d')
    return ref_current


@pytest.fixture
def future_4_days():
    current = dt.date.today()
    future = current + dt.timedelta(days=4)
    ref_future = {"Description2": [future.strftime('%Y-%m-%d'), ' ']}
    out_future = future.strftime('%Y-%m-%d')
    return ref_future


@pytest.fixture
def future_8_days():
    current = dt.date.today()
    future8 = current + dt.timedelta(days=8)
    ref_future8 = {"Description3": [future8.strftime('%Y-%m-%d'), ' ']}
    out_future8 = future8.strftime("%Y-%m-%d")
    return ref_future8


@pytest.fixture
def past_4_days():
    current = dt.date.today()
    past4 = current - dt.timedelta(days=4)
    ref_past4 = {"Description4": [past4.strftime('%Y-%m-%d'), ' ']}
    out_past4 = past4.strftime('%Y-%m-%d')
    return ref_past4


@pytest.mark.events_test
def test_current_date_checking_works(current_day):
    """Test if Event checking works with one parameter passed"""
    data = current_day
    events = Events()
    events.events_dict = data
    res = events.event_detection()
    assert data in res


@pytest.mark.events_test
def test_future_4_days_date_works(future_4_days):
    """Test if Event checking works with date + 4 days from now"""
    data = future_4_days
    events = Events()
    events.events_dict = data
    res = events.event_detection()
    assert data in res


@pytest.mark.events_test
def test_future_8_days_not_passed(future_8_days):
    """Test if Event from future +7 days is not returned"""
    data = future_8_days
    events = Events()
    events.events_dict = data
    res = events.event_detection()
    assert data not in res


@pytest.mark.events_test
def test_past_4_days_not_passed(past_4_days):
    """Test if Event from the past -4 days is not returned"""
    data = past_4_days
    events = Events()
    events.events_dict = data
    res = events.event_detection()
    assert data not in res


@pytest.fixture
def all_dates():
    current = dt.date.today()
    currentday = {"Descriprion1": [current.strftime('%Y-%m-%d'), " " ]}
    future = current + dt.timedelta(days=4)
    future4_days = {"Description2": [future.strftime('%Y-%m-%d'), ' ']}
    future8 = current + dt.timedelta(days=8)
    future8_days = {"Description3": [future8.strftime('%Y-%m-%d'), ' ']}
    past4 = current - dt.timedelta(days=4)
    past4_days = {"Description4": [past4.strftime('%Y-%m-%d'), ' ']}
    all_data = {
        "Descriprion1": [current.strftime('%Y-%m-%d'), " " ],
        "Description2": [future.strftime('%Y-%m-%d'), ' '],
        "Description3": [future8.strftime('%Y-%m-%d'), ' '],
        "Description4": [past4.strftime('%Y-%m-%d'), ' ']
    }
    return all_data, currentday, future4_days, future8_days, past4_days


@pytest.mark.events_test
def test_all_dates_passed(all_dates):
    """Test if all dates future past and current are displayed
    properly in response"""
    data, current, future4, future8, past4 = all_dates
    events = Events()
    events.events_dict = data
    resflag, res = events.event_detection()
    assert (next(iter(current)) in res) and (next(iter(future4)) in res) and\
         (next(iter(future8)) not in res) and (next(iter(past4)) not in res)


@pytest.mark.events_test
@patch.object(Events, 'save')
def test_saving_events_current_passes(mock_my_method):
    """Test if saving date passes witrh correct input"""
    mock_my_method.return_value = True
    current = dt.date.today()
    current_day = dt.datetime.strftime(current, "%Y-%m-%d")
    events = Events()
    res = events.add_event(current_day, "event1", 213213442)
    assert "Event added" in res


@pytest.mark.events_test
@patch.object(Events, 'save')
def test_saving_events_future(mock_my_method):
    """Test if Events saves correctly events from the future"""
    mock_my_method.return_value = True
    future_4 = dt.date.today() + dt.timedelta(days=4)
    future_4_days = dt.datetime.strftime(future_4, "%Y-%m-%d")
    events = Events()
    res = events.add_event(future_4_days, "event2", 23123213213)
    assert "Event added" in res
    
    
@pytest.mark.events_test
@patch.object(Events, 'save')
def test_saving_events_past_reaction(mock_my_method):
    """Test if Events react correctly when user want to add event
     with date from the past"""
    mock_my_method.return_value = True

    past_4 = dt.date.today() - dt.timedelta(days=4)
    past_4_days = dt.datetime.strftime(past_4, "%Y-%m-%d")
    events = Events()
    res = events.add_event(past_4_days, "event past 4 days", 312321321321)
    assert "Given event date is in the past" in res 