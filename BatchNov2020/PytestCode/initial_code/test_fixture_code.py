import pytest

@pytest.fixture(scope="function")
#@pytest.fixture(scope="module")
def setup():
    print("Setup Initiated")
    yield
    print("We are in tear down")



def test_fist_case(setup):
    print("this is my first test case")


def test_second_case(setup):
    print("this is my second test case")


def test_third_case(setup):
    print("this is my third test case")