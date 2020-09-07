import pytest

@pytest.mark.parametrize("point1,point2,x3,expected",[
	((1,3), (2,6), 3, 9),
	((1,4), (2,8), 3, 12),
	((1,5), (2,10), 3, 15),
	])


def test_find_y(point1,point2, x3, expected):
	from findy import find_y
	answer = find_y(point1, point2, x3, expected)
	assert answer == expected