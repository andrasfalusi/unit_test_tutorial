import pytest

@pytest.fixture()
def fixture01():
    print("\nIn fixture01()...")

@pytest.mark.usefixtures('fixture01')
def test_case01(fixture01):
    print("\nIn tst_case01()...")

