import pytest
@pytest.fixture(scope="function", autouse=True)
def Arrange():
    print("\nLaunch browser")
    print("Login")
    print("Find products")
    yield
    print("\n LogOff")
    print("Close browser")