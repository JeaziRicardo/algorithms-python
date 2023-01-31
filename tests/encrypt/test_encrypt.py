from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message([], 0)
    with pytest.raises(TypeError):
        encrypt_message("message", [])
