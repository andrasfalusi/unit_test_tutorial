import pytest

@pytest.fixture()
def fixture01(request):
    print("\nIn fixture...")
    print(f"Fixture scope: {str(request.scope)}")
    print(f"Function name: {str(request.function.__name__)}")
    print(f"Class name: {str(request.cls)}")
    print(f"Module name: {str(request.module.__name__)}")
    print(f"File path: {str(request.fspath)}")

@pytest.mark.usefixtures('fixture01')
def test_case01():
    print("\nI'm the test_case01")


