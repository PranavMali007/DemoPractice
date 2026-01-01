def test_file_2_0(test_fixture):
    print('file_2.0')


'''even if u don't use test_fixture name in below method 
still it will work because of @pytest.fixture(autouse=True)'''

def test_file_2_1():
    print('file_2.1')

def test_file_2_2():
    print('file_2.2')