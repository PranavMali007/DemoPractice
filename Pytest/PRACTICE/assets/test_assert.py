import pytest
# import test_user_defined_markers

@pytest.mark.regression
def test_sample_one():
    a = 2
    b = 5
    assert a==b, 'a != b'
    print('Inside One')

@pytest.mark.regression
def test_sample_two():
    a = 2
    b = 5
    assert a < b
    print('Inside Two')
@pytest.mark.smoke
def test_sample_three():
    a = 'Pranav'
    b = 'Pranav'
    assert a.__eq__(b)
    print('Inside Three')

