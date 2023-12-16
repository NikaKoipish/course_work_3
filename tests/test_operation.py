from src.utils import number_format, date_format

def test_number_format():
    assert number_format("Maestro 1596837868705199") == "Maestro  1596 83** **** 5199"
    assert number_format("Счет 35383033474447895560") == "Счет **5560"

def test_date_format():
    assert date_format("2018-06-30") == "30.06.2018"
