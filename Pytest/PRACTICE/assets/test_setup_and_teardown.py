import pytest
@pytest.fixture
def test_setup_and_teardown():
    print('Welcome to world\n')
    print('Initialize setup\n')
    yield
    print('OK Nice to meet you\n')
    print('Ended setup')

@pytest.mark.smoke
def test_login_with_valide_credentials(test_setup_and_teardown):
    print('login_with_valide_credentials\n')


def test_logout(test_setup_and_teardown):
    print('LOGOUT\n')

''' 1.How to run smoke marker
     >>>pytest - rA - m smoke.\test_setup_and_teardown.py
     
    2.How to run fixture(test_setup_and_teardown)
     >>>pytest -rA .\test_setup_and_teardown.py
'''