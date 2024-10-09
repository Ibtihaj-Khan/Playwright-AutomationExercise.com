from playwright.sync_api import expect
import re

class HomePage:
    def __init__(self, page):
        self.page = page

        """
        Selectors
        """
        self.active_carousel_header = page.locator('div.active h1')

        """
        Top Nav Bar
        """
        self.nav_login_button = page.locator('.header-middle ul.nav a[href="/login"]')

        """
        Featured Shop section
        """
        self.first_product_text = page.locator('div.features_items .productinfo p').nth(0)
        self.first_product_link = page.locator('div.features_items .product-image-wrapper ul a').nth(0)


    def verify_page_loaded(self):
        expect(self.active_carousel_header).to_have_text("AutomationExercise")

    def nav_to_login_page(self):
        self.nav_login_button.click()

    def visit_first_product(self):
        self.first_product_link.click()


