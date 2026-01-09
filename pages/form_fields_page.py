from .base_page import BasePage

class FormFieldsPage(BasePage):
    # Локаторы формы EASY
    EASY_USERNAME = "#username"
    EASY_EMAIL = "#email"
    EASY_PASSWORD = "#password"
    EASY_REGISTER = "#submitBtn"
    EASY_COUNTRY = "#country"
    EASY_TERMS = '#terms'
    EASY_RESULT = '#formResult'

    # Локаторы формы MEDIUM
    VAL_USERNAME = "#val-username"
    VAL_EMAIL = "#val-email"
    VAL_PASSWORD = "#val-password"
    VAL_CONFIRM_PASSWORD = '#val-confirm-password'
    VAL_SUBMIT = '#valSubmitBtn'
    VAL_VALID_RESULT = '#valFormResult'

    # Локаторы формы HARD
    DYNAMIC_USERNAME = "#dyn-name"
    DYNAMIC_EMAIL = '#emailFields input'
    DYNAMIC_PHONE = "#phoneFields input"
    DYNAMIC_SUBMIT = '#dynSubmitBtn'
    DYNAMIC_BTN_ADD_EMAIL = "#addEmailBtn"
    DYNAMIC_BTN_ADD_PHONE = "#addPhoneBtn"
    DYNAMIC_BTN_DELETE = "button[onclick*='removeEmailField(this)']"
    DYNAMIC_RESULT = '#dynFormResult'

    def fill_easy_form(self,username: str, email: str, password: str,country: str, expected_result: str):
        self.fill_input(self.EASY_USERNAME, username)
        self.fill_input(self.EASY_EMAIL, email)
        self.fill_input(self.EASY_PASSWORD, password)
        self.select_text_in_dropdown(self.EASY_COUNTRY, country)
        self.click_on_element_btn(self.EASY_TERMS)
        self.click_on_element_btn(self.EASY_REGISTER)
        self.check_found_text(self.EASY_RESULT,expected_result)

    def fill_medium_form(self, username: str,email: str, password: str, confirm_password: str,expected_result: str):
        self.fill_input(self.VAL_USERNAME, username)
        self.fill_input(self.VAL_EMAIL, email)
        self.fill_input(self.VAL_PASSWORD, password)
        self.fill_input(self.VAL_CONFIRM_PASSWORD, confirm_password)
        self.click_on_element_btn(self.VAL_SUBMIT)
        self.check_found_text(self.VAL_VALID_RESULT, expected_result)

    def fill_hard_form(self, username: str,email: str, phone_number: str):
        self.fill_input(self.DYNAMIC_USERNAME, username)
        self.fill_input(self.DYNAMIC_EMAIL, email)
        self.fill_input(self.DYNAMIC_PHONE, phone_number)
        self.click_on_element_btn(self.DYNAMIC_SUBMIT)


