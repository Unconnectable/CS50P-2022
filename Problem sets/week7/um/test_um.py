import pytest
from um import count

def test_count():
    assert count("um") == 1
    assert count("asdasdasd,asasd,um") == 1
    assert count("unsdasd") == 0
    assert count("UM") == 1

    assert count("hello,world") == 0
    assert count("Um, thanks for the album.") == 1
