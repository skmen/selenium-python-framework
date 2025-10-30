import pytest
from main.pages.LoginPage import LoginPage

@pytest.mark.usefixtures("login_page")
class TestLogin:

    def test_successful_login(self, login_page: LoginPage):
        login_page.login("student", "Password123")
        assert "Logged In Successfully" in login_page.get_success_message_text()

    def test_unsuccessful_login(self, login_page: LoginPage):
        login_page.login("incorrect_user", "incorrect_password")
        assert "Your username is invalid!" in login_page.get_error_message_text()
