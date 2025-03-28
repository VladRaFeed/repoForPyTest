import pytest

from src.main import Calculator

@pytest.mark.parametrize("x,y,res", [(1,2,0.5), (5,-1,-5),(4,2,2)])
def test_divide(x,y,res):
    assert Calculator().divide(x, y) == res
    
@pytest.mark.parametrize("x,y,res", [(1,3,4), (5,-1,4),(0,0,0)])
def test_add(x,y,res):
    assert Calculator().add(x,y) == res