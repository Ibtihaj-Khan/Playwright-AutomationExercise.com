def click_button(page, button_text):
    page.locator(f'//button[text()="{button_text}"]').click()