from playwright.sync_api import expect

class ShopPage:
    def __init__(self, page):
        self.page = page
        
        """
        Shop page selectors
        """
        """
        Single product view
        """
        self.product_view_name = page.locator('div.product-information h2')
        self.product_view_quantity = page.locator('//label[text()="Quantity:"]/following-sibling::input[@name="quantity"]')
        self.product_add_to_cart = page.locator('//button[contains(@class, "cart")]')

        """
        Added to cart modal
        """
        self.modal_view_cart = page.locator('//u[text()="View Cart"]/..')

        """
        Cart Page
        """
        self.cart_product_name = page.locator('td.cart_description h4 a')
        self.cart_quantity = page.locator('td.cart_quantity button')
        self.cart_delete = page.locator('.cart_quantity_delete')

    f"""
    Script used to verify the product name on the single product view
    @Param {str} name is the name of the product expected.
    """
    def verify_product_name(self, name):
        expect(self.product_view_name, f"Product name was not {name}.").to_have_text(name)

    f"""
    Script used to increase the product quantity by pressing up arrow.
    @Param {int} count is the total number you want to increase by.
    """
    def increment_product_quantity(self, count):
        #Subtract desired count by 1 since it starts at 1
        count -=1
        
        for i in range(count):
            self.product_view_quantity.press("ArrowUp")

    def add_to_cart(self):
        self.product_add_to_cart.click()

    def verify_cart(self, name, quantity):
        expect(self.cart_product_name).to_have_text(name)
        expect(self.cart_quantity).to_have_text(quantity)

    """
    Script will clean up the cart
    """
    def cleanup_cart(self):
        cart_items = self.cart_delete.count()

        for i in range(cart_items):
            self.cart_delete.nth(i).click()




