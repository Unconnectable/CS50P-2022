from fuel import convert
from fuel import  gauge

def test_convet():
    with pytest.raises(ValueError):
        convert("x/y")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        conver("1.5/3")

    assert convert("1/4") == 25
    assert convert("99/100") == 99


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(2) == "2%"
    assert gauge(40) == "40%"
    assert gauge(98) == "98%"
