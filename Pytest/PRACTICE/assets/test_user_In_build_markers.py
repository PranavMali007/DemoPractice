import pytest

#xpassed
@pytest.mark.xfail
def test_xfail_Failed():
    assert "9<10"=="9<10"
    print('xfail=9>10')

#xfailed
@pytest.mark.xfail
def test_xfail_passed():
    assert 0>1
    print('xfail=0>1')

@pytest.mark.smoke
def test_sample_1():
    assert 9<10
    print('sample1')

@pytest.mark.smoke
def test_sample_2():
    print('sample2')

@pytest.mark.regression
def test_sample_3():
    print('sample3')

@pytest.mark.xyz
def test_sample_4():
    print('sample4')

@pytest.mark.skip
def test_sample_4():
    print('skip marker')