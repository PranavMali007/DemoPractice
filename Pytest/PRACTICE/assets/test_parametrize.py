import pytest

@pytest.mark.parametrize('user,password',[('abhi','1234'),('ram',1234)])
def parametrize_marker(user,password):
    print(user +":"+ password)