from src.utils import number_format, date_format, get_data, get_sorted_list, get_filtered_data
import json
from config import ROOT_DIR
import os
def test_number_format():
    assert number_format("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert number_format("Счет 35383033474447895560") == "Счет **5560"

def test_date_format():
    assert date_format("2018-06-30") == "30.06.2018"

def test_get_data():
    path = os.path.join(ROOT_DIR, "tests", "test_operation.json")
    assert get_data(path) == [1, 2, 3]

def test_get_sorted_list():
    data = ["2018-03-23", "2019-08-26", "2019-07-03", "2020-07-03", "2014-07-03"]
    assert get_sorted_list(data) == ["2020-07-03", "2019-08-26", "2019-07-03", "2018-03-23", "2014-07-03"]

