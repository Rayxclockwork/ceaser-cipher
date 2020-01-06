import pytest
from ceaser_cipher import encrypt, decrypt

def test_encrypt():
    string = 'This is a test string. My name is Raven.'
    assert encrypt(string, 5) == 'ymnx nx f yjxy xywnsl. rd sfrj nx wfajs.'

def test_decrypt():
    string = 'ymnx nx f yjxy xywnsl. rd sfrj nx wfajs.'
    assert decrypt(string, -5) == 'This is a test string. My name is Raven.'
