import pytest

@pytest.mark.parametrize("point1, point2, x3, expected",[
	((1,3), (2,6), 3, 9),
	((1,4), (2,8), 3, 12),
	((1,5), (2,10), 3, 15),
	])

def test_find_y(point1, point2, x3, expected):
	from findy import find_y
	answer = find_y(point1, point2, x3)
	assert answer == expected

@pytest.mark.parametrize("point1, point2, expected",[
	((1,3), (2,6), 3),
	((1,4), (2,8), 4),
	((1,5), (2,10), 5),
	])

def test_find_slope(point1, point2, expected):
    from findy import find_slope
    answer = find_slope(point1, point2)
    assert answer == expected