import pytest


@pytest.mark.parametrize("num1, num2, output", [(2, 20, 40), (3, 10, 30), (4, 5, 21), (5, 20, 100)])
def test_param(num1, num2, output):
    mul = num1*num2
    assert mul == output


@pytest.mark.skip
@pytest.mark.smoke
def test_newcase():
    a = [4, 6, 7, 8, 9]
    for i in a:
        print(i**2)


@pytest.mark.xfail
def test_new_cases2():
    list1 = [4, 6, 7]
    assert  5 in list1
