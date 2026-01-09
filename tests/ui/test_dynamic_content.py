# ==========================================
# POSITIVE SCENARIOS
# ==========================================
def test_show_dilay_content(open_main_page,dynamic_page):
    dynamic_page.click_on_element_btn(dynamic_page.SHOW_DELAY_BTN)
    for text in dynamic_page.EXPECTED_DYNAMIC_ELEMENTS:
        dynamic_page.check_found_texts_in_list(dynamic_page.DELAY_CONTENT_CONTAINER,text)

def test_download_ajax_content(open_main_page,dynamic_page):
    dynamic_page.click_on_element_btn(dynamic_page.LOAD_AJAX_BTN)
    dynamic_page.check_the_number_of_entries(dynamic_page.AJAX_CONTENT,5)

def test_get_infinity_scroll(open_main_page,dynamic_page):
    dynamic_page.scroll_into_last_element(dynamic_page.INFINITE_SCROLL_CONTAINER,dynamic_page.SCROLL_ITEMS)
    dynamic_page.check_found_text(dynamic_page.ITEM_COUNT,'10')
    dynamic_page.check_the_number_of_entries(dynamic_page.SCROLL_ITEMS,10)

# ==========================================
# NEGATIVE SCENARIOS
# ==========================================
def test_ajax_too_slow_error(open_main_page,dynamic_page):
    dynamic_page.click_on_element_btn(dynamic_page.LOAD_AJAX_BTN)
    try:
        dynamic_page.page.locator(dynamic_page.AJAX_CONTENT).first.wait_for(timeout=500)
    except Exception as e:
        print(f"Тест успешно поймал ошибку таймаута: {e}")