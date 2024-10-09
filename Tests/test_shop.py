from playwright.sync_api import Page, Browser, BrowserContext
from Models.home_page import HomePage
from Models.shop_page import ShopPage

def test_verify_product_quantity_in_cart(page):
    home_page = HomePage(page)
    shop_page = ShopPage(page)

    #Launch browser, navigate, verify home page is visible
    page.goto("http://automationexercise.com")
    home_page.verify_page_loaded()

    #Get First Product Name -> Click View Product on the home page -> Verify we loaded the right product.
    first_product_name = home_page.first_product_text.inner_text()

    home_page.visit_first_product()
    shop_page.verify_product_name(first_product_name)

    #Increase quantity to 4 -> add to cart
    shop_page.increment_product_quantity(4)
    shop_page.add_to_cart()

    #View cart -> Verify quantity is correct
    shop_page.modal_view_cart.click()
    shop_page.verify_cart(first_product_name,"4")
    shop_page.cleanup_cart()
    page.wait_for_timeout(3000)