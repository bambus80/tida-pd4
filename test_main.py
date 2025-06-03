from main import *


def test_zad1():
    data = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    result = zad1(data)
    expected = [10, 22, 33, 50, 60, 80]
    assert result == expected


def test_zad1_blank_input():
    data = []
    result = zad1(data)
    expected = []
    assert result == expected


def test_zad2():
    data = [2, -4, 6, 8, -10, 100, -6, 5]
    result = zad2(data)
    expected = [6, 8, -10, 100]
    assert result == expected


def test_zad2_blank_input():
    data = []
    result = zad2(data)
    expected = []
    assert result == expected


def test_zad3():
    data = 5
    result = zad3(data)
    expected = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 2],
        [1, 1, 3],
        [1, 2, 2],
        [1, 4],
        [2, 3],
        [5]
    ]
    assert result == expected


def test_zad3_n_zero():
    deta = 0
    result = zad3(deta)
    expected = [0]
    assert result == expected


def test_zad4():
    data = 3
    result = zad4(data)
    expected = [
        "abc",
        "acb",
        "bac",
        "bca",
        "cab",
        "cba",
    ]
    assert result == expected


def test_zad4_n_zero():
    data = 0
    result = zad4(data)
    expected = []
    assert result == expected