import pytest
from pages.tables_page import TablesPage
# ==========================================
# POSITIVE SCENARIOS
# ==========================================
def test_sort_valid_id(open_main_page, table_page):
    table_page.click_on_element_btn(table_page.ID_MEDIUM_TABLE)
    table_page.check_found_text(table_page.CHECK_FIRST_ROW_ID,'1')

def test_sort_valid_name(open_main_page, table_page):
    table_page.click_on_element_btn(table_page.NAME_MEDIUM_TABLE)
    table_page.check_found_text(table_page.CHECK_FIRST_ROW_NAME,'Alice Johnson')

def test_sort_valid_age(open_main_page, table_page):
    table_page.click_on_element_btn(table_page.AGE_MEDIUM_TABLE)
    table_page.check_found_text(table_page.CHECK_FIRST_ROW_AGE, '25')

def test_sort_valid_salary(open_main_page, table_page):
    table_page.click_on_element_btn(table_page.SALARY_MEDIUM_TABLE)
    table_page.check_found_text(table_page.CHECK_FIRST_ROW_SALARY,'$65,000')

def test_get_name(open_main_page, table_page):
    table_page.fill_input(table_page.INPUT_SEARCH_NAME,'Alice Cooper')
    table_page.check_found_text(table_page.ROW_1_NAME_TABLE,'Alice Cooper')
    table_page.check_found_text(table_page.VISIBLE_ROWS,'1')

def test_get_status_all(open_main_page, table_page):
    table_page.select_text_in_dropdown(table_page.ALL_STATUS, 'Все статусы')
    table_page.check_found_text(table_page.VISIBLE_ROWS, '6')

def test_get_status_active(open_main_page, table_page):
    table_page.select_text_in_dropdown(table_page.ALL_STATUS,'Active')
    table_page.check_found_text(table_page.VISIBLE_ROWS,'3')

def test_get_status_inactive(open_main_page, table_page):
    table_page.select_text_in_dropdown(table_page.ALL_STATUS,'Inactive')
    table_page.check_found_text(table_page.VISIBLE_ROWS,'2')

def test_get_status_pending(open_main_page, table_page):
    table_page.select_text_in_dropdown(table_page.ALL_STATUS,'Pending')
    table_page.check_found_text(table_page.VISIBLE_ROWS,'1')

def test_pagination_to_next_page(open_main_page, table_page):
    table_page.click_on_element_btn(table_page.NEXT_PAGE_BTN_TABLE)
    table_page.check_found_text(table_page.PAGE_START,'6')
    table_page.check_active_page_number(table_page.PAGINATION_CONTAINER,'2')

def test_pagination_to_previous_page(open_main_page, table_page):
    table_page.click_on_element_btn(table_page.NEXT_PAGE_BTN_TABLE)
    table_page.check_found_text(table_page.PAGE_START, '6')
    table_page.check_active_page_number(table_page.PAGINATION_CONTAINER, '2')
    table_page.click_on_element_btn(table_page.PREVIOUS_PAGE_BTN_TABLE)
    table_page.check_found_text(table_page.PAGE_START, '1')
    table_page.check_active_page_number(table_page.PAGINATION_CONTAINER, '1')

def test_pagination_to_last_page(open_main_page, table_page):
    table_page.click_on_element_btn(table_page.LAST_PAGE_BTN_TABLE)
    table_page.check_active_page_number(table_page.PAGINATION_CONTAINER,'4')
    table_page.check_found_text(table_page.PAGE_START,'16')

def test_pagination_to_first_page(open_main_page, table_page):
    table_page.click_on_element_btn(table_page.LAST_PAGE_BTN_TABLE)
    table_page.check_active_page_number(table_page.PAGINATION_CONTAINER,'4')
    table_page.check_found_text(table_page.PAGE_START,'16')
    table_page.click_on_element_btn(table_page.FIRST_PAGE_BTN_TABLE)
    table_page.check_active_page_number(table_page.PAGINATION_CONTAINER,'1')
    table_page.check_found_text(table_page.PAGE_START,'1')

def test_check_page_size_5(open_main_page, table_page):
    table_page.check_found_text(table_page.PAGE_SIZE_TABLE,'5 на странице')
    table_page.check_found_text(table_page.PAGE_END,'5')
    table_page.check_the_number_of_entries(table_page.PAGE_COUNT,5)

def test_check_page_size_10(open_main_page, table_page):
    table_page.select_text_in_dropdown(table_page.PAGE_SIZE_TABLE,'10 на странице')
    table_page.check_found_text(table_page.PAGE_SIZE_TABLE,'10')
    table_page.check_found_text(table_page.PAGE_END,'10')
    table_page.check_the_number_of_entries(table_page.PAGE_COUNT,10)

def test_check_page_size_20(open_main_page, table_page):
    table_page.select_text_in_dropdown(table_page.PAGE_SIZE_TABLE, '20 на странице')
    table_page.check_found_text(table_page.PAGE_SIZE_TABLE,'20')
    table_page.check_found_text(table_page.PAGE_END,'20')
    table_page.check_the_number_of_entries(table_page.PAGE_COUNT,20)
# ==========================================
# NEGATIVE SCENARIOS
# ==========================================
@pytest.mark.parametrize('search_text, expected_count', TablesPage.SEARCH_NEGATIVE_DATA)
# check 7 cases
def test_search_negative(open_main_page, table_page, search_text, expected_count):
    table_page.fill_input(table_page.INPUT_SEARCH_NAME, search_text)
    table_page.check_found_text(table_page.VISIBLE_ROWS, expected_count)

