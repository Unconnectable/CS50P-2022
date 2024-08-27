from seasons import validate
from datetime import date

def test_validate():
    assert validate("1999-01-01", "2003-01-01") == 525600
    assert validate("2001-01-01", "2003-01-01") == 1051200
    assert validate("1995-01-01", "2000-01-01") == 2629440
    assert validate("2020-06-01", "2032-01-01") == 6092640

# Call the test function
test_validate()
