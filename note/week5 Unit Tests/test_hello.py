from hello import hello

def test_hello():
    assert hello("David")=="Hello, David"
def test_2():
    assert hello()=="Hello, world"
def test_3():
    names= ["alice","Benjiming","Carroten"]
    for name in names:
        assert hello(name) == f"Hello, {name}"