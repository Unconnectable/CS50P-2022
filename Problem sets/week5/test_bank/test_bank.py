from bank import value

def test_value():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("Hey") == 20
    assert value("FUCK YOU") == 100
    assert value("hello OBY") == 0
