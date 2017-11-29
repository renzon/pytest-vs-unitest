import pytest


@pytest.mark.parametrize('expected', list(range(1, 10)))
def test_plus_1(expected):
    assert 1 == expected
