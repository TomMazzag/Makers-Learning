from lib.report_length import *

def test_report_lenth():
    length_1 = report_length("This is a test")
    length_2 = report_length("So is this")
    length_3 = report_length("")

    assert length_1 == "This string was 14 characters long."
    assert length_2 == "This string was 10 characters long."
    assert length_3 == "This string was 0 characters long."
