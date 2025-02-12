from src.sample import add,sub

def test_add(a,b):
    assert add(3,4) == 7
    assert add(5,4) == 9
    assert add(2,8) == 10

def test_sub(a,b):
    assert sub(5,2) == 3
    assert add(14,6) == 8    

#just to trigger the github actions