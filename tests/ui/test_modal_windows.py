import pytest
from pages.modal_windows import ModalWindowsPage
# ==========================================
# POSITIVE SCENARIOS
# ==========================================
def test_press_close_modal_windows_easy(open_main_page, modal_page):
    modal_page.click_on_element_btn(modal_page.OPEN_MODAL_WINDOWS_BTN_EASY)
    modal_page.click_on_element_btn(modal_page.CLOSE_MODAL_BTN_EASY)
    modal_page.check_element_is_hidden(modal_page.MODAL_WINDOWS_EASY)

def test_press_ok_modal_windows_easy(open_main_page, modal_page):
    modal_page.click_on_element_btn(modal_page.OPEN_MODAL_WINDOWS_BTN_EASY)
    modal_page.click_on_element_btn(modal_page.CONFIRM_MODAL_BTN_EASY)
    modal_page.check_element_is_hidden(modal_page.MODAL_WINDOWS_EASY)

def test_full_path_modal_windows_medium(open_main_page, modal_page):
    modal_page.click_on_element_btn(modal_page.OPEN_MODAL_WINDOWS_BTN_MEDIUM)
    modal_page.click_on_element_btn(modal_page.OPEN_SECOND_MODAL_WINDOWS_BTN_MEDIUM)
    modal_page.click_on_element_btn(modal_page.OPEN_THIRD_NESTED_MODAL_WINDOWS_BTN_MEDIUM)
    modal_page.check_found_text(modal_page.MODAL_WINDOWS_MEDIUM,' Вы достигли максимального уровня вложенности!')
    modal_page.click_on_element_btn(modal_page.CLOSE_THIRD_NESTED_MODAL_WINDOWS_BTN_MEDIUM)
    modal_page.click_on_element_btn(modal_page.CLOSE_SECOND_NESTED_MODAL_WINDOWS_BTN_MEDIUM)
    modal_page.click_on_element_btn(modal_page.CLOSE_NESTED_MODAL_WINDOWS_BTN_MEDIUM)
    modal_page.check_element_is_hidden(modal_page.MODAL_WINDOWS_MEDIUM)

def test_success_modal_windows_hard(open_main_page, modal_page):
    modal_page.click_on_element_btn(modal_page.OPEN_SUCCESS_DYNAMIC_MODAL_WINDOWS_BTN_HARD)
    modal_page.check_found_text(modal_page.DYNAMIC_MODAL_WINDOWS_MESSAGE,'Данные успешно сохранены!')
    modal_page.click_on_element_btn(modal_page.CLOSE_DYNAMIC_MODAL_WINDOWS_BTN_HARD)
    modal_page.check_element_is_hidden(modal_page.DYNAMIC_MODAL_WINDOWS_MESSAGE)

def test_error_modal_windows_hard(open_main_page, modal_page):
    modal_page.click_on_element_btn(modal_page.OPEN_ERROR_DYNAMIC_MODAL_WINDOWS_BTN_HARD)
    modal_page.check_found_text(modal_page.DYNAMIC_MODAL_WINDOWS_MESSAGE,'Произошла ошибка при обработке запроса.')
    modal_page.click_on_element_btn(modal_page.CLOSE_DYNAMIC_MODAL_WINDOWS_BTN_HARD)
    modal_page.check_element_is_hidden(modal_page.DYNAMIC_MODAL_WINDOWS_MESSAGE)

def test_warning_modal_windows_hard(open_main_page, modal_page):
    modal_page.click_on_element_btn(modal_page.OPEN_WARNING_DYNAMIC_MODAL_WINDOWS_BTN_HARD)
    modal_page.check_found_text(modal_page.DYNAMIC_MODAL_WINDOWS_MESSAGE,'Эта операция необратима. Продолжить?')
    modal_page.click_on_element_btn(modal_page.CLOSE_DYNAMIC_MODAL_WINDOWS_BTN_HARD)
    modal_page.check_element_is_hidden(modal_page.DYNAMIC_MODAL_WINDOWS_MESSAGE)
# ==========================================
# NEGATIVE SCENARIOS
# ==========================================
@pytest.mark.parametrize('btn_open, hided_window', ModalWindowsPage.MODAL_WINDOWS_DATA)
def test_modal_not_persistent_on_refresh(open_main_page, modal_page,btn_open, hided_window):
    # Запуск 5 тестов
    modal_page.click_on_element_btn(btn_open)
    modal_page.check_element_is_visible(btn_open)
    modal_page.refresh_page()
    modal_page.check_element_is_hidden(hided_window)