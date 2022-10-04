import sys
from unittest import mock
import pytest
import os
import datetime as dt

current = os.path.dirname(os.path.realpath(__file__))

parent = os.path.dirname(current)

from datson import Garbagson, Events, CyclicEvents
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
def test_event_detection_fails_argument_passed():
    """Test if event detection fails with any atgument passed"""
    events = Events()
    with pytest.raises(TypeError) as err:
        events.event_detection("argument")
    assert "takes 1 positional argument" in str(err.value)


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


@pytest.mark.events_test
@patch.object(Events, 'save')
def test_savin_events_future_more_than_7(mock_my_method):
    """Test if Events save react correctly when user wat to add
    event located in more than 7 days in the future"""
    mock_my_method.return_value = True

    future_8 = dt.date.today() + dt.timedelta(days=8)
    future_8_days = dt.datetime.strftime(future_8, "%Y-%m-%d")
    events = Events()
    res = events.add_event(future_8_days, "event 8 days future", 3213213213)
    assert "Event added" in res


@pytest.mark.events_test
@pytest.mark.parametrize("date,title,channel,expected" ,[
    (12321321, "test_title1", 21321321321, "Bad data type for data it should be YYYY-MM-DD"),
    ("112312-312-11123", "test_title2", 21312323, "Bad data type for data it should be YYYY-MM-DD"),
    (dt.datetime.strftime(dt.date.today(), "%Y-%m-%d"), 3231231, 2321423213, "Bad data type for description you should pass text"),
    (dt.datetime.strftime(dt.date.today(), "%Y-%m-%d"), "test_title3", "string", "Bad data type for channel internal error")
])
@patch.object(Events, 'save')
def test_saving_future_bad_data_fails(mock_my_method, date, title, channel, expected):
    """Test if Events save reacts to bad data type or nonsence data"""
    mock_my_method.return_value = True

    events = Events()
    res = events.add_event(date, title, channel)
    assert expected in res
    
    
@pytest.mark.events_test
def test_saving_fails_to_many_arguments():
    """Test if saving fails with to many arguments passed"""
    events = Events()
    with pytest.raises(TypeError) as err:
        events.add_event("3000-12-12", "future event", 32142134214, "extra")
    assert "takes 4 positional arguments" in str(err.value)
        
    
# ------------------------------------ Cyclic Evnets testing-------------------------------------
@pytest.fixture
def data_for_cyclic():
    """Fixture hodling all data for all data to cyclic events class testing
    one date 4 days in the past one current date one two dates in the future
    one 4 days in the future one 16 days"""
    current_day = dt.date.today()
    current_date = dt.datetime.strftime(current_day, "%m-%d")
    past_4days = current_day - dt.timedelta(days=4)
    past_4_days_date = dt.datetime.strftime(past_4days, "%m-%d")
    future_4days = current_day + dt.timedelta(days=4)
    future_4_days_date = dt.datetime.strftime(future_4days, "%m-%d")
    future_16days = current_day + dt.timedelta(days=16)
    future_16_days_date = dt.datetime.strftime(future_16days, "%m-%d")
    
    data_frame = {"Title description current":[current_date, 3214213213213],
                  "Title description past 4":[past_4_days_date, 688787678676],
                  "Title description future 4":[future_4_days_date, 3214352321],
                  "Title description future 16": [future_16_days_date, 3124532412]}
    
    return data_frame, current_date, past_4_days_date, future_4_days_date,\
        future_16_days_date


@pytest.mark.cyclic_events_test
def test_cyclic_events_passes(data_for_cyclic):
    """Tests if cyclic events works fine with data for the future and past"""
    data_frame, current, past4, future4, future16 = data_for_cyclic
    cyclic_events = CyclicEvents()
    cyclic_events.cyclic_events = data_frame
    flag, res = cyclic_events.event_detection()
    refactored_res = []
    for key in res:
        refactored_res.append(res[key][0])
    assert current in refactored_res and past4 not in refactored_res and future4 in refactored_res \
        and future16 not in refactored_res
        
        
@pytest.mark.cyclic_events_test
def test_cyclic_events_fails_with_argument():
    """Test if cyclic events fails when any argument passed with event detection"""
    cyclic_events = CyclicEvents()
    
    with pytest.raises(TypeError) as err:
        cyclic_events.event_detection("nonsence")
    assert "takes 1 positional" in str(err.value)


@pytest.mark.cyclic_events_test
@pytest.mark.parametrize("date,title,channel,expected" ,
[(dt.datetime.strftime(dt.date.today(), "%m-%d"), "current_time_event", 32132141242,
"Cyclic event added"), (dt.datetime.strftime((dt.date.today() 
+ dt.timedelta(days=4)), "%m-%d"), "future_cyclic_event4", 321321321321, "Cyclic event added"),
(dt.datetime.strftime((dt.date.today()+dt.timedelta(days=20)) , "%m-%d"), "future_cyclic_event20",
32131232132, "Cyclic event added"), (dt.datetime.strftime((dt.date.today() - dt.timedelta(days=4)), "%m-%d"),
"past_cyclic_event4", 32132141243213, "Cyclic event added"),
(dt.datetime.strftime(dt.date.today(), "%m-%d"), 32132131, 3213214214, "Invalid description format expected string"),
("312-21321", "Nonsence data", 32213213, "Given date is invalid"),
(213213, "bad data data type", 65765765, "Invalid data format expected string"),
(dt.datetime.strftime(dt.date.today(), '%m-%d'), "correct data", "bad type", "Internal error invalid channel data type")
])
@patch.object(CyclicEvents, 'save')
def tests_saving_options(mock_my_method, date, title, channel, expected):
    """Test bad and god cases of saving cyclic events even bad arguments"""
    mock_my_method.return_value = True

    cyclic = CyclicEvents()
    res = cyclic.add_item(date, title, channel)
    assert expected in res