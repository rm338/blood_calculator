import pytest

@pytest.mark.parametrize("HDL_value,expected",[
	(120, "Normal"),
	(45, "Borderline Low"),
	(10, "Low")
	])

def test_analyze_HDL_result_normal(HDL_value, expected):
	from calculator import analyze_HDL_result
	answer = analyze_HDL_result(HDL_value)
	assert answer == expected





