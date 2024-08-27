import pytest
from calculator import f


def test():
    #Part1
    '''
    if f(2)!=4:
        print("f(2)!=4")
    if f(3)!=9:
        print("f(3)!=9")
    '''
    #Part2
    '''
    #new key word
    #AssertionError 断言错误
    try:
        assert f(2)==4
    except AssertionError:
        print("f(2)!=4")
    try:
        assert f(3)==9
    except AssertionError:
        print("f(2)!=4")
    '''


def test_pos():
    #Part3:
    assert f(2) == 4
    assert f(3) == 9


def test_neg():
    assert f(-3) == 9
    assert f(-2) == 4


def test_zero():
    assert f(0) == 0


def test_str():
    with pytest.raises(TypeError):
        f("note")


def test_float_convesion():
    assert f(10) == pytest.approx(100, abs=0.1)
