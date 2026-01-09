from pages.base_page import BasePage

class DynamicContentPage(BasePage):
    # Локаторы появление элементов Medium
    SHOW_DELAY_BTN = '#showDelayedBtn'
    DELAY_CONTENT_CONTAINER = '#delayedContent'
    EXPECTED_DYNAMIC_ELEMENTS = ['Элемент 1','Элемент 2','Элемент 3']


    # Локаторы AJAX загрузки данных Medium
    LOAD_AJAX_BTN = '#loadAjaxBtn'
    AJAX_CONTENT = '#ajaxTableBody tr'

    # Локаторы  Infinite Scroll
    INFINITE_SCROLL_CONTAINER = '#infiniteScrollContainer'
    SCROLL_ITEMS = '.scroll-item'
    ITEM_COUNT = '#itemCount'