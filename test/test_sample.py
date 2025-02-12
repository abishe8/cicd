from src.sample import add, sub

def test_add():
    assert add(3, 4) == 7
    assert add(5, 4) == 9
    assert add(2, 8) == 10

def test_sub():
    assert sub(5, 2) == 3
    assert sub(14, 6) == 8  # Fixed the function call from 'add' to 'sub'

#just to trigger the github actions