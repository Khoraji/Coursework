import pytest
import uuid
from booking import addbooking

def test_addbooking():
    # Test with valid input
    new_uuid = addbooking()
    assert isinstance(new_uuid, str) # Check that the function returns a string
    assert len(new_uuid) == 8 # Check that the UUID is 8 characters long

    # Test with invalid input
    with pytest.raises(Exception):
        # Test with empty surname
        input_values = ["", "Forename", "Film", "Monday"]
        monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
        addbooking()

        # Test with empty forename
        input_values = ["Surname", "", "Film", "Monday"]
        monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
        addbooking()

        # Test with empty film
        input_values = ["Surname", "Forename", "", "Monday"]
        monkeypatch.setattr
