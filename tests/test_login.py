from app.login import login


def test_login_ok():
    assert login("admin", "1234")


def test_login_wrong_password():
    assert not login("admin", "wrong")
