# tests/test_login.py

from abstracts.ILoginPage import ILoginPage # Import the Interface

# Test uses the 'login_page' fixture, which provides the ILoginPage contract
def test_successful_login(login_page: ILoginPage):
    """
    Test case for logging in with the default correct credentials (admin/admin).
    """
    # 1. Navigate to the login page
    login_page.load()
    
    # 2. Perform the login action (Default Credentials: admin / admin)
    login_page.login("admin", "admin")
    
    # 3. Assert the expected outcome
    # Note: We removed the hardcoded URL in load() to demonstrate the flexibility 
    # of IBaseWebPage/ILoginPage, but we will use the default.
    expected_message = "System Login Demo" # Assuming this is the title of the next page
    actual_title = login_page.get_page_title() # Using the inherited IBaseWebPage method
    
    assert expected_message in actual_title, \
        f"Login failed. Expected '{expected_message}' but got page title '{actual_title}'"

# NEW TEST: Invalid Login Test
def test_invalid_login(login_page: ILoginPage):
    """
    Test case for attempting to log in with incorrect credentials.
    """
    login_page.load()
    login_page.login("bad_user", "wrong_pass")
    
    # The error message element should now be visible and contain the error text
    expected_error_message = "Invalid Credentials" # Placeholder - update after checking the site
    actual_error_message = login_page.get_error_message_text()
    
    assert expected_error_message in actual_error_message, \
        f"Invalid login test failed. Expected '{expected_error_message}' but got '{actual_error_message}'"