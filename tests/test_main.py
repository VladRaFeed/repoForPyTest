import pytest
from contextlib import nullcontext as does_not_raise
from src.main import Calculator

class TestCalculator:
    @pytest.mark.parametrize("x,y,res, expentation", [(1,2,0.5,does_not_raise()), (5,"-1",-5, pytest.raises(TypeError)),(4,0,2,pytest.raises(ZeroDivisionError))])
    def test_divide(self,x,y,res, expentation):
        with expentation:
            assert Calculator().divide(x, y) == res
        
    @pytest.mark.parametrize("x,y,res,expentation", [(1,3,4,does_not_raise()), (5,"-1",4,pytest.raises(TypeError)),(0,0,0,does_not_raise())])
    def test_add(self,x,y,res,expentation):
        with expentation:
            assert Calculator().add(x,y) == res