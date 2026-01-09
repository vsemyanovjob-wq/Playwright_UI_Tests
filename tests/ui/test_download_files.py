# ==========================================
# POSITIVE SCENARIOS
# ==========================================
def test_download_one_file(open_main_page, download_page):
    download_page.choose_one_file(download_page.DOWNLOAD_BTN_SINGLE_FILE,'C:\\Users\\StDef\\1.txt')
    download_page.check_found_text(download_page.SINGLE_FILE,'Выбран файл: 1.txt (0.03 KB)')

def test_download_two_files(page,open_main_page, download_page):
    download_page.choose_two_files(download_page.DOWNLOAD_BTN_MULTI_FILE,'C:\\Users\\StDef\\1.txt','C:\\Users\\StDef\\2.txt')
    download_page.check_found_text(download_page.MULTI_FILES,'1. 1.txt (0.03 KB)\n2. 2.txt (0.03 KB)')

def test_get_static_progress(open_main_page, download_page):
    download_page.check_on_attribute(download_page.STATIC_PROGRESS_BTN,'style','width: 75%')

def test_get_animation_progress(open_main_page, download_page):
    download_page.click_on_element_btn(download_page.START_PROGRESS_BTN)
    download_page.check_dynamic_progress(download_page.VALUE_PROGRESS_BTN,'100%')
# ==========================================
# NEGATIVE SCENARIOS
# ==========================================
def test_check_disable_btn_launch_progress(open_main_page, download_page):
    download_page.click_on_element_btn(download_page.START_PROGRESS_BTN)
    download_page.check_disabled_btn(download_page.START_PROGRESS_BTN)

def test_checking__file_is_not_selected(open_main_page, download_page):
    download_page.check_found_text(download_page.DOWNLOAD_BTN_SINGLE_FILE,'')

def test_checking_files_is_not_selected(open_main_page, download_page):
    download_page.check_found_text(download_page.DOWNLOAD_BTN_MULTI_FILE,'')


