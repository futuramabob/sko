import sys
import os

# Pfad zu skogit/ hinzufügen, damit file.py gefunden wird
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from file import add, subtract, multi, absolute, double

def test_add():
    assert add(2, 3) == 5
    assert add(-1, -1) == -2
    assert add(0, 5) == 5
    assert add(1.5, 2.5) == 4.0

def test_subtract():
    assert subtract(10, 3) == 7
    assert subtract(0, 5) == -5
    assert subtract(-3, -6) == 3
    assert subtract(2.5, 1.0) == 1.5

def test_multi():
    assert multi(3, 4) == 12
    assert multi(-2, 3) == -6
    assert multi(0, 10) == 0
    assert multi(2.5, 2) == 5.0

def test_absolute():
    assert absolute(5) == 5
    assert absolute(-5) == 5
    assert absolute(0) == 0
    assert absolute(-3.5) == 3.5

def test_double():
    assert double(2) == 4
    assert double(-3) == -6
    assert double(0) == 0
    assert double(1.5) == 3.0
