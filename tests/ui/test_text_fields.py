# ==========================================
# POSITIVE SCENARIOS
# ==========================================
def test_easy_success_registration(open_main_page,form_page):
    form_page.fill_easy_form('Витя', 'test@4.com','11111111','Germany','Форма успешно отправлена!')

def test_medium_success_registration(open_main_page,form_page):
    form_page.fill_medium_form('Виктор','test@4.com','11111111a','11111111a','Все проверки пройдены! Форма валидна.')

def test_hard_success_registration(open_main_page,form_page):
    form_page.fill_hard_form('Виктор', 'test@4.com', '73453453465')
    form_page.check_found_text(form_page.DYNAMIC_RESULT,'Форма успешно отправлена!')
    form_page.check_found_text(form_page.DYNAMIC_RESULT,'Виктор')
    form_page.check_found_text(form_page.DYNAMIC_RESULT,'test@4.com')
    form_page.check_found_text(form_page.DYNAMIC_RESULT, '73453453465')

def test_hard_should_add_new_email_field(open_main_page,form_page):
    form_page.click_on_element_btn(form_page.DYNAMIC_BTN_ADD_EMAIL)
    form_page.check_the_number_of_entries(form_page.DYNAMIC_EMAIL,2)

def test_hard_should_remove_new_email_field(open_main_page,form_page):
    form_page.click_on_element_btn(form_page.DYNAMIC_BTN_ADD_EMAIL)
    form_page.check_the_number_of_entries(form_page.DYNAMIC_EMAIL, 2)
    form_page.click_on_element_btn(form_page.DYNAMIC_BTN_DELETE + " >> nth=1")
    form_page.check_the_number_of_entries(form_page.DYNAMIC_EMAIL, 1)

def test_hard_should_add_new_phone_field(open_main_page,form_page):
    form_page.click_on_element_btn(form_page.DYNAMIC_BTN_ADD_PHONE)
    form_page.check_the_number_of_entries(form_page.DYNAMIC_PHONE,2)

def test_hard_should_remove_new_phone_field(open_main_page,form_page):
    form_page.click_on_element_btn(form_page.DYNAMIC_BTN_ADD_PHONE)
    form_page.check_the_number_of_entries(form_page.DYNAMIC_PHONE,2)
    form_page.click_on_element_btn(form_page.DYNAMIC_BTN_DELETE)
    form_page.check_the_number_of_entries(form_page.DYNAMIC_EMAIL, 1)
# ==========================================
# NEGATIVE SCENARIOS
# ==========================================
def test_easy_empty_username_registration(open_main_page,form_page):
    form_page.fill_input(form_page.EASY_EMAIL,'test@4.com')
    form_page.fill_input(form_page.EASY_PASSWORD,'11111111')
    form_page.select_text_in_dropdown(form_page.EASY_COUNTRY,'Germany')
    form_page.click_on_element_btn(form_page.EASY_TERMS)
    form_page.click_on_element_btn(form_page.EASY_REGISTER)
    form_page.check_field_validation_error(form_page.EASY_USERNAME)

def test_easy_empty_email_registration(open_main_page,form_page):
    form_page.fill_input(form_page.EASY_USERNAME,'Витя')
    form_page.fill_input(form_page.EASY_PASSWORD,'11111111')
    form_page.select_text_in_dropdown(form_page.EASY_COUNTRY,'Germany')
    form_page.click_on_element_btn(form_page.EASY_TERMS)
    form_page.click_on_element_btn(form_page.EASY_REGISTER)
    form_page.check_field_validation_error(form_page.EASY_EMAIL)

def test_easy_empty_password_registration(open_main_page,form_page):
    form_page.fill_input(form_page.EASY_USERNAME,'Витя')
    form_page.fill_input(form_page.EASY_EMAIL, 'test@4.com')
    form_page.select_text_in_dropdown(form_page.EASY_COUNTRY,'Germany')
    form_page.click_on_element_btn(form_page.EASY_TERMS)
    form_page.click_on_element_btn(form_page.EASY_REGISTER)
    form_page.check_field_validation_error(form_page.EASY_PASSWORD)

def test_easy_empty_country_registration(open_main_page,form_page):
    form_page.fill_input(form_page.EASY_USERNAME,'Витя')
    form_page.fill_input(form_page.EASY_EMAIL, 'test@4.com')
    form_page.fill_input(form_page.EASY_PASSWORD, '11111111')
    form_page.click_on_element_btn(form_page.EASY_TERMS)
    form_page.click_on_element_btn(form_page.EASY_REGISTER)
    form_page.check_field_validation_error(form_page.EASY_COUNTRY)

def test_easy_empty_terms_registration(open_main_page,form_page):
    form_page.fill_input(form_page.EASY_USERNAME,'Витя')
    form_page.fill_input(form_page.EASY_EMAIL, 'test@4.com')
    form_page.fill_input(form_page.EASY_PASSWORD, '11111111')
    form_page.select_text_in_dropdown(form_page.EASY_COUNTRY,'Germany')
    form_page.click_on_element_btn(form_page.EASY_REGISTER)
    form_page.check_field_validation_error(form_page.EASY_TERMS)

def test_medium_empty_username_registration(open_main_page,form_page):
    form_page.fill_input(form_page.VAL_EMAIL,'test@4.com')
    form_page.fill_input(form_page.VAL_PASSWORD,'11111111a')
    form_page.fill_input(form_page.VAL_CONFIRM_PASSWORD,'11111111a')
    form_page.click_on_element_btn(form_page.VAL_SUBMIT)
    form_page.check_found_text(form_page.VAL_VALID_RESULT, "Форма содержит ошибки. Исправьте их и попробуйте снова.")

def test_medium_empty_email_registration(open_main_page,form_page):
    form_page.fill_input(form_page.VAL_USERNAME,'Виктор')
    form_page.fill_input(form_page.VAL_PASSWORD,'11111111a')
    form_page.fill_input(form_page.VAL_CONFIRM_PASSWORD,'11111111a')
    form_page.click_on_element_btn(form_page.VAL_SUBMIT)
    form_page.check_found_text(form_page.VAL_VALID_RESULT, "Форма содержит ошибки. Исправьте их и попробуйте снова.")

def test_medium_empty_password_registration(open_main_page,form_page):
    form_page.fill_input(form_page.VAL_USERNAME, 'Виктор')
    form_page.fill_input(form_page.VAL_EMAIL,'test@4.com')
    form_page.fill_input(form_page.VAL_PASSWORD,'11111111a')
    form_page.fill_input(form_page.VAL_CONFIRM_PASSWORD,'11111111b')
    form_page.click_on_element_btn(form_page.VAL_SUBMIT)
    form_page.check_found_text(form_page.VAL_VALID_RESULT, "Форма содержит ошибки. Исправьте их и попробуйте снова.")

def test_hard_empty_name_registration(open_main_page,form_page):
    form_page.fill_input(form_page.DYNAMIC_EMAIL,'test@43com')
    form_page.fill_input(form_page.DYNAMIC_PHONE,'880053535')
    form_page.check_field_validation_error(form_page.DYNAMIC_USERNAME)


def test_hard_empty_email_registration(open_main_page,form_page):
    form_page.fill_input(form_page.DYNAMIC_USERNAME,'Виктор')
    form_page.fill_input(form_page.DYNAMIC_PHONE,'880053535')
    form_page.check_field_validation_error(form_page.DYNAMIC_EMAIL)

def test_hard_empty_phone_registration(open_main_page,form_page):
    form_page.fill_input(form_page.DYNAMIC_USERNAME,'Виктор')
    form_page.fill_input(form_page.DYNAMIC_EMAIL,'test@43com')
    form_page.check_field_validation_error(form_page.DYNAMIC_PHONE)





