import pytest
from pages.drag_and_drop_page import DragAndDropPage
from pages.dynamic_content_page import DynamicContentPage
from pages.form_fields_page import FormFieldsPage
from pages.hover_and_tooltips_page import HoverAndTooltipsPage
from pages.tables_page import TablesPage
from pages.modal_windows import ModalWindowsPage
from pages.frames_and_iframe_pages import FramesPage
from pages.download_files_page import DownloadFilesPage



@pytest.fixture()
def open_main_page(page):
    page.goto('https://aqa-proka4.org/sandbox/web')
    page.wait_for_load_state('domcontentloaded')
    return page

@pytest.fixture()
def form_page(page):
    form_page = FormFieldsPage(page)
    return form_page

@pytest.fixture()
def table_page(page):
    table_page = TablesPage(page)
    return table_page

@pytest.fixture()
def modal_page(page):
    modal_page = ModalWindowsPage(page)
    return modal_page

@pytest.fixture()
def drag_and_drop_page(page):
    drag_and_drop_page = DragAndDropPage(page)
    return drag_and_drop_page

@pytest.fixture()
def dynamic_page(page):
    dynamic_page = DynamicContentPage(page)
    return dynamic_page

@pytest.fixture()
def frame_page(page):
    frame_page = FramesPage(page)
    return frame_page

@pytest.fixture()
def download_page(page):
    download_page =  DownloadFilesPage(page)
    return download_page

@pytest.fixture()
def hover_page(page):
    hover_page = HoverAndTooltipsPage(page)
    return hover_page