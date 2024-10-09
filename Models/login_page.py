from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page

        """
        Define selectors for the page.
        """
        """
        Initial login view
        """
        self.new_user_signup_header = page.locator('div.signup-form>h2')
        self.new_user_signup_name = page.locator('div.signup-form input[data-qa="signup-name"]')
        self.new_user_signup_email = page.locator('div.signup-form input[data-qa="signup-email"]')
        self.new_user_signup_button = page.locator('div.signup-form button[type="submit"]')

        """
        New Signup Page 2
        """
        ##Top Section
        self.signup_header = page.locator('div.login-form h2:nth-child(1)')
        self.signup_title_mr = page.locator('div.radio-inline input[value="Mr"]')
        self.signup_title_mrs = page.locator('div.radio-inline input[value="Mrs"]')
        self.signup_name = page.locator('input#name')
        self.signup_email = page.locator('input#email')
        self.signup_password = page.locator('input#password')
        self.dob_day = page.locator('select#days')
        self.dob_month = page.locator('select#months')
        self.dob_year = page.locator('select#years')
        self.signup_newsletter = page.locator('input[type="checkbox"]#newsletter')
        self.signup_offers = page.locator('input[type="checkbox"]#optin')

        ##Address Section
        self.first_name = page.locator('input#first_name')
        self.last_namme = page.locator('input#last_name')
        self.company = page.locator('input#company')
        self.add1 = page.locator('input#address1')
        self.add2 = page.locator('input#address2')
        self.country = page.locator('select#country')
        self.state = page.locator('input#state')
        self.city = page.locator('input#city')
        self.zip = page.locator('input#zipcode')
        self.phone = page.locator('input#mobile_number')

    def verify_signup_header(self, name_of_header):
        match name_of_header:
            case "new-signup-page-1":
                expect(self.new_user_signup_header, "Header for signup form was incorrect.").to_have_text("New User Signup!")
            case "new-signup-page-2":
                expect(self.signup_header, "Second page of new user signup had an incorrect header!").to_have_text("Enter Account Information")

    def configure_signup_form(self, username, email):
        self.new_user_signup_name.fill(username)
        self.new_user_signup_email.fill(email)

    f"""
    Script used to fill in the signup for new user form
    takes in a {map} of values that correlate to the fields.
    """
    def fill_signup_form(self, signup_form_data):
        #Fill in the data sequentially
        if (signup_form_data["Title"]) == "Mr.":
            self.signup_title_mr.click()
        elif (signup_form_data["Title"] == "Mrs."):
            self.signup_title_mrs.click()

        self.signup_name.fill(signup_form_data["Name"])
        expect(self.signup_email, "Email was not pre populated correctly").to_have_attribute("value", signup_form_data["Email"])
        self.signup_password.fill(signup_form_data["Password"])

        self.dob_day.select_option(value=f'{signup_form_data["DOB"][0]}')
        self.dob_month.select_option(value=f'{signup_form_data["DOB"][1]}')
        self.dob_year.select_option(value=f'{signup_form_data["DOB"][2]}')

        self.signup_newsletter.click()
        self.signup_offers.click()

        #Address section of the form
        self.first_name.fill(signup_form_data["FirstName"])
        self.last_namme.fill(signup_form_data["LastName"])
        self.company.fill(signup_form_data["Company"])
        self.add1.fill(signup_form_data["Address"]["Add1"])
        self.add2.fill(signup_form_data["Address"]["Add2"])
        self.country.select_option(value=f'{signup_form_data["Address"]["Country"]}')
        self.state.fill(signup_form_data["Address"]["State"])
        self.city.fill(signup_form_data["Address"]["City"])
        self.zip.fill(signup_form_data["Address"]["Code"])
        self.phone.fill(signup_form_data["Phone"])



        




