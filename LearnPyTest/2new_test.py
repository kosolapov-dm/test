import pytest

@pytest.fixture()
def Arrange():
    print("\nLaunch browser")
    print("Login")
    print("Find products")
    yield
    print("\n LogOff")
    print("Close browser")


def testAddItemtoCart(Arrange):
    print("Item added successfully")

def testRemoveFromCart(Arrange):
    print("Item removed successfully")



