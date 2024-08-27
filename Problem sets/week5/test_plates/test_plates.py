from plates import is_valid
def test_is_valid():
    assert is_valid("PI3.14") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("h") == False
    assert is_valid("21213") == False
    assert is_valid("CS50") == True
    assert is_valid("ECTO88") == True
    assert is_valid("NRVOUS") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P2") == False
