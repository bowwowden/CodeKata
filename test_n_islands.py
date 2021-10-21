import pytest


def get_n_islands(input: list):
    output = None
    return output


def test_n_islands():
    grid: list = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    assert get_n_islands(grid) == 3
