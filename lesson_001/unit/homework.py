from unit.div import div
import pytest

@pytest.mark.happy
# happy是组名 自定义命名
# pytest.mark.parametrize参数化
@pytest.mark.parametrize("number1,number2,excepection", {
    (10, 2, 5),
    (10000, 1, 10000),
    (10, 3, 3.3333333333333335),
    (10.0, 5, 2.0),
    (9, -1, -9),
    (0, 1, 0),
})
def test_div_case01(number1, number2, excepection):
    assert div(number1, number2) == excepection


@pytest.mark.parametrize('num1,num2,excepection', {
    (1, 0, ZeroDivisionError),
    ('a', 'b', TypeError)
})
def test_div_case02(num1, num2, excepection):
    assert div(num1, num2) == excepection

def test_div_case03(num1,num2,excepection):
    with pytest.raises(excepection):
        div(num1,num2)