from stringPrrogram_practice import reverse_str, palendrome
import pytest
@pytest.mark.regression
def test_reverse_str():
    assert reverse_str("hello") == "olleh"
    assert reverse_str("Hello") == "olleH"
    assert reverse_str("Hello78") == "87olleH"
    assert reverse_str("989898") == "898989"
    assert reverse_str("") == ""
    assert reverse_str(9898) == '8989'
    assert reverse_str("HeLLo") == 'oLLeH'

@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.flow_id12343
def test_palendrome():
    assert palendrome("malayalam") == True
    assert palendrome("MalayalaM") == True
    assert palendrome("India") == False
    assert palendrome("98989") == True

@pytest.mark.regression
def test_palendrome23():
    assert palendrome("malayalam") == True
    assert palendrome("MalayalaM") == True
    assert palendrome("India") == False
    assert palendrome("98989") == True