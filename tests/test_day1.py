import pytest
from adventofcode_2023.day1 import get_calibration_value, filter_for_numbers


@pytest.mark.parametrize("input,expected", [("1abc2", "12"), ("pqr3stu8vwx", "38")])
def test_filter_for_numbers(input, expected):
    assert filter_for_numbers(input) == expected


def test_get_calibration_value():
    example = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    assert get_calibration_value(example) == 142