import pytest as pytest

from utils import arrs


def test_get_1():
    assert arrs.get([1, 2, 3], 2, default="test") == 3


def test_get_2():
    with pytest.raises(IndexError):
        assert arrs.get([], 0, default="test") == "test"


def test_slice_1():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]


def test_slice_2():
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
