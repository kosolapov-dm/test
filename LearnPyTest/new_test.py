import pytest
@pytest.mark.skip
def testLogin():
    print("Login successful")

@pytest.mark.skip
def testLogoff():
    print("Logoff successful")


@pytest.mark.skip
def testCalc():
    assert 2 + 2 == 4