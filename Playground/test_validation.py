import pytest

"""
    :param scope:
        The scope for which this fixture is shared; one of ``"function"``
        (default), ``"class"``, ``"module"``, ``"package"`` or ``"session"``.
"""
@pytest.fixture(scope="module")
def pre_work():
    print("I setup browser")
    return 'pass'

@pytest.fixture(scope="function")
def second_work():
    print("Second fixtures")
    yield
    print('tear down fixture')

def test_initial_check(pre_work, second_work):
    print("This is first test")
    assert pre_work == 'fail'


def test_second_check(pre_work):
    print("This is second test")