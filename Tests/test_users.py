from playwright.sync_api import Page, Browser, BrowserContext
from Models.home_page import HomePage
from Models.login_page import LoginPage
import Utilities.generic_functions

def test_register_user(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    """
    Variables for this test.
    """
    username = 'Joe Shmmo'
    email = 'johhnnnathan@joe.com'
    signup_form_data = {
        "Title": "Mr.",
        "Name": username,
        "Email": email,
        "Password": "abcdefg123",
        "DOB": [8, 8, 1985],
        "FirstName": username.split(" ")[0],
        "LastName": username.split(" ")[1],
        "Company": "BigCo",
        "Address": {
            "Add1": "123 church st",
            "Add2": "Unit 123",
            "Country": "United States",
            "State": "California",
            "City": "SF",
            "Code": "99959",
        },
        "Phone": "4083993339",
    }

    page.goto("http://automationexercise.com")
    
    #Nav from home page to login page
    home_page.verify_page_loaded()
    home_page.nav_to_login_page()

    #Page 1 -> verify the signup header + start creating user
    login_page.verify_signup_header('new-signup-page-1')
    login_page.configure_signup_form(username, email)
    Utilities.generic_functions.click_button(page, "Signup")

    #Page 2 -> Verify Signup header + fill in form data (Top Form)
    login_page.verify_signup_header('new-signup-page-2')
    login_page.fill_signup_form(signup_form_data)

    #Page 2 -> Click submit
    Utilities.generic_functions.click_button(page, "Create Account")
    

    page.wait_for_timeout(4000)

