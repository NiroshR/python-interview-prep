import pytest
import src.business_logic as sut


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (-1, -2),
        (0, 0),
        (1, 2),
    ],
)
def test_multiply_by_two(input, expected_output):
    # GIVEN

    # WHEN
    actual = sut.multiply_by_two(input)

    # THEN
    assert actual == expected_output
