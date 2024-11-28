import pytest
def test_verify_sum():
    assert (1+1) == 2
def test_verify_sum1():
    assert (1+1) == 3
@pytest.mark.skip(reason="not completed")
def test_verify_sum2():
    assert (1+1) == 4

