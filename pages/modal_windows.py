from .base_page import BasePage

class ModalWindowsPage(BasePage):
    # Локаторы модальных окон Easy
    OPEN_MODAL_WINDOWS_BTN_EASY = '#openModalBtn'
    CONFIRM_MODAL_BTN_EASY = '#confirmModalBtn'
    CLOSE_MODAL_BTN_EASY = '#closeModalBtn'
    MODAL_WINDOWS_EASY = '#simpleModal'

    # Локаторы модальных окон Medium
    OPEN_MODAL_WINDOWS_BTN_MEDIUM = '#openNestedModalBtn'
    OPEN_SECOND_MODAL_WINDOWS_BTN_MEDIUM = '#openNestedModal2Btn'
    CLOSE_NESTED_MODAL_WINDOWS_BTN_MEDIUM = '#closeNestedModal1Btn'
    OPEN_THIRD_NESTED_MODAL_WINDOWS_BTN_MEDIUM = '#openNestedModal3Btn'
    CLOSE_SECOND_NESTED_MODAL_WINDOWS_BTN_MEDIUM = '#closeNestedModal2Btn'
    MODAL_WINDOWS_MEDIUM = '#nestedModal3'
    CLOSE_THIRD_NESTED_MODAL_WINDOWS_BTN_MEDIUM = '#closeNestedModal3Btn'

    # Локаторы модальных окон Hard
    OPEN_SUCCESS_DYNAMIC_MODAL_WINDOWS_BTN_HARD = '#successModalBtn'
    CLOSE_DYNAMIC_MODAL_WINDOWS_BTN_HARD = '#closeDynamicModalBtn'
    OPEN_ERROR_DYNAMIC_MODAL_WINDOWS_BTN_HARD = '#errorModalBtn'
    OPEN_WARNING_DYNAMIC_MODAL_WINDOWS_BTN_HARD = '#warningModalBtn'

    DYNAMIC_MODAL_WINDOWS_MESSAGE = '#dynamicModal'

    MODAL_WINDOWS_DATA = [
        # Кнопки с открытием модалки и модальное окно
        (OPEN_MODAL_WINDOWS_BTN_EASY, DYNAMIC_MODAL_WINDOWS_MESSAGE),
        (OPEN_MODAL_WINDOWS_BTN_MEDIUM, DYNAMIC_MODAL_WINDOWS_MESSAGE),
        (OPEN_SUCCESS_DYNAMIC_MODAL_WINDOWS_BTN_HARD, DYNAMIC_MODAL_WINDOWS_MESSAGE),
        (OPEN_ERROR_DYNAMIC_MODAL_WINDOWS_BTN_HARD, DYNAMIC_MODAL_WINDOWS_MESSAGE),
        (OPEN_WARNING_DYNAMIC_MODAL_WINDOWS_BTN_HARD, DYNAMIC_MODAL_WINDOWS_MESSAGE),
    ]





