import pytest


@pytest.fixture(autouse=True,scope='session')

def test_fixture():
    print('\n!!!!!SETUP FIXTURE!!!!!')
    yield
    print('<<<<TEARDOWN FIXTURE>>>>>')