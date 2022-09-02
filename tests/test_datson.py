import sys
import pytest
import os
import datetime as dt

current = os.path.dirname(os.path.realpath(__file__))

parent = os.path.dirname(current)

from datson import Garbagson


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
