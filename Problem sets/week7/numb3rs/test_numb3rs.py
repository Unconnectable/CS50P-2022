import pytest
from numb3rs import validate

def test_validate1(ip):
    assert validate("2.2.2.2") ==True
    assert validate("2222.2.2.2") ==False
    assert validate("225.225.225.225") ==True
    assert validate("ss") = False
    assert validate("ss_2.2.2") = False
    assert validate("ss222") = False
    assert validate("2.2.2.2.2.2.2") = False
