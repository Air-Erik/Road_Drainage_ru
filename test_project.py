import flet as ft
from project import y_coef, check

def test_y_coef_1():
    assert round(y_coef(1.0, 0.02), 7) == 20.2368316


def test_y_coef_2():
    assert round(y_coef(1.0, 0.03), 7) == 19.2897752


def test_y_coef_3():
    assert round(y_coef(1.0, 0.04), 7) == 18.2848596

def test_check_1():
    txt = ft.TextField(value='1.0')
    assert check(txt, 0.1, 2.0) == 1.0

def test_check_2():
    txt = ft.TextField()
    assert check(txt, 0.1, 2.0) == None
