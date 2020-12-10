from unit import div
import pytest


@pytest.mark.happy
def test_div_int():
    assert div.div(10, 2) == 5
    assert div.div(10, 5) == 2
    assert div.div(10000000, 1) == 10000000.0


def test_div_float():
    assert div.div(10, 3) == 333333
    assert div.div(10.2, 0.2) == 51


def test_div_expection():
    assert div.div(10, 'a')


@pytest.mark.expection
def test_div_zero():
    assert div.div(10, 0) == None


@pytest.mark.happy
@pytest.mark.parametrize("number1,number2,excepection", {
    (10, 2, 5),
    (10, 5, 2),
    (100000000, 1, 1000000)
})
# parametrize参数化

def test_div_int_pram(number1, number2, excepection):
    assert div.div(number1, number2) == excepection
