import pytest

@pytest.mark.smoke
def test_print():
    a = 10
    b = 20
    assert a + b == 30

@pytest.mark.smoke
def test_divition():
    a = 10
    b = 20
    assert b//a == 2

@pytest.mark.sanity
@pytest.mark.smoke
def test_multiply():
    a = 10
    b = 20
    assert a*b == 300

@pytest.mark.sanity
def test_subs():
    a = 40
    b = 30
    assert a-b == 10

@pytest.mark.regression
def test_print1():
    a = 10
    b = 20
    assert a + b == 30

@pytest.mark.regression
def test_divition1():
    a = 10
    b = 20
    assert b//a == 2

def test_multiply1():
    a = 10
    b = 20
    assert a*b == 300

def test_subs1():
    a = 40
    b = 30
    assert a-b == 10


