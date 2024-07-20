import pytest

from main import add

data = [(2, 3, 5), (5, 5, 10), (0, 10, 110)]


# テストケースをパラメータ化
@pytest.mark.parametrize("a, b, expected", data)
def test_add(a, b, expected):
    assert add(a, b) == expected
