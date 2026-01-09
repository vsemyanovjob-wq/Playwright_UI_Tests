import pytest
from pages.drag_and_drop_page import DragAndDropPage
# ==========================================
# POSITIVE SCENARIOS
# ==========================================
@pytest.mark.parametrize('element',DragAndDropPage.ELEMENTS_DATA)
def test_move_one_elements(open_main_page, drag_and_drop_page,element):
    drag_and_drop_page.move_element(element['attribute'],drag_and_drop_page.ENDS_ZONE)
    drag_and_drop_page.check_the_number_of_entries(drag_and_drop_page.ENDS_ZONE_ITEMS,1)

def test_move_all_elements(open_main_page, drag_and_drop_page):
    for element in drag_and_drop_page.ELEMENTS_DATA:
        drag_and_drop_page.move_element(element['attribute'],drag_and_drop_page.ENDS_ZONE)
    drag_and_drop_page.check_the_number_of_entries(drag_and_drop_page.BEGIN_ZONE_ITEMS,0)

def test_change_position(open_main_page, drag_and_drop_page):
    before = drag_and_drop_page.get_list_order(drag_and_drop_page.SORT_LIST_CONTAINER)
    drag_and_drop_page.change_element(drag_and_drop_page.LIST_DATA[0]['attribute'], drag_and_drop_page.LIST_DATA[2]['attribute'])
    after = drag_and_drop_page.get_list_order(drag_and_drop_page.SORT_LIST_CONTAINER)
    assert before != after

def test_todo_empty_when_all_moved(open_main_page, drag_and_drop_page):
    drag_and_drop_page.move_element(drag_and_drop_page.TASK_CREATE_DESIGN,drag_and_drop_page.CONTAINER_IN_PROGRESS)
    drag_and_drop_page.move_element(drag_and_drop_page.TASK_WRITE_TEST, drag_and_drop_page.CONTAINER_IN_PROGRESS)
    drag_and_drop_page.move_element(drag_and_drop_page.TASK_COD_REVIEW, drag_and_drop_page.CONTAINER_IN_PROGRESS)
    drag_and_drop_page.move_element(drag_and_drop_page.TASK_MAKE_API, drag_and_drop_page.CONTAINER_IN_PROGRESS)
    drag_and_drop_page.move_element(drag_and_drop_page.TASK_BASE_DATE, drag_and_drop_page.CONTAINER_IN_PROGRESS)
    drag_and_drop_page.check_the_number_of_entries(drag_and_drop_page.ITEMS_IN_TODO,0)
    drag_and_drop_page.check_the_number_of_entries(drag_and_drop_page.ITEMS_IN_DONE,0)

def test_in_progress_empty_when_all_moved(open_main_page, drag_and_drop_page):
    drag_and_drop_page.move_element(drag_and_drop_page.TASK_MAKE_API,drag_and_drop_page.CONTAINER_TO_DO)
    drag_and_drop_page.move_element(drag_and_drop_page.TASK_BASE_DATE,drag_and_drop_page.CONTAINER_TO_DO)
    drag_and_drop_page.check_the_number_of_entries(drag_and_drop_page.ITEMS_IN_PROGRESS,0)

def test_done_empty_when_all_moved(open_main_page, drag_and_drop_page):
    drag_and_drop_page.move_element(drag_and_drop_page.TASK_BASE_DATE,drag_and_drop_page.CONTAINER_IN_PROGRESS)
    drag_and_drop_page.check_the_number_of_entries(drag_and_drop_page.ITEMS_IN_DONE,0)

def test_full_todo_list_after_move(open_main_page, drag_and_drop_page):
    drag_and_drop_page.move_element(drag_and_drop_page.TASK_BASE_DATE, drag_and_drop_page.CONTAINER_TO_DO)
    drag_and_drop_page.move_element(drag_and_drop_page.TASK_MAKE_API, drag_and_drop_page.CONTAINER_TO_DO)

    for case in drag_and_drop_page.LIST_WITH_CASES:
        drag_and_drop_page.check_found_texts_in_list(drag_and_drop_page.CONTAINER_TO_DO, case)


def test_full_in_progress_list_after_move(open_main_page, drag_and_drop_page):
    drag_and_drop_page.move_element(drag_and_drop_page.TASK_CREATE_DESIGN,drag_and_drop_page.CONTAINER_IN_PROGRESS)
    drag_and_drop_page.move_element(drag_and_drop_page.TASK_WRITE_TEST, drag_and_drop_page.CONTAINER_IN_PROGRESS)
    drag_and_drop_page.move_element(drag_and_drop_page.TASK_BASE_DATE, drag_and_drop_page.CONTAINER_IN_PROGRESS)
    drag_and_drop_page.move_element(drag_and_drop_page.TASK_MAKE_API, drag_and_drop_page.CONTAINER_IN_PROGRESS)
    drag_and_drop_page.move_element(drag_and_drop_page.TASK_COD_REVIEW, drag_and_drop_page.CONTAINER_IN_PROGRESS)

    for case in drag_and_drop_page.LIST_WITH_CASES:
        drag_and_drop_page.check_found_texts_in_list(drag_and_drop_page.CONTAINER_IN_PROGRESS,case)


def test_full_done_list_after_move(open_main_page, drag_and_drop_page):
    drag_and_drop_page.move_element(drag_and_drop_page.TASK_CREATE_DESIGN, drag_and_drop_page.CONTAINER_DONE)
    drag_and_drop_page.move_element(drag_and_drop_page.TASK_WRITE_TEST, drag_and_drop_page.CONTAINER_DONE)
    drag_and_drop_page.move_element(drag_and_drop_page.TASK_MAKE_API, drag_and_drop_page.CONTAINER_DONE)
    drag_and_drop_page.move_element(drag_and_drop_page.TASK_COD_REVIEW, drag_and_drop_page.CONTAINER_DONE)

    for case in drag_and_drop_page.LIST_WITH_CASES:
        drag_and_drop_page.check_found_texts_in_list(drag_and_drop_page.CONTAINER_DONE, case)
# ==========================================
# NEGATIVE SCENARIOS
# ==========================================
@pytest.mark.parametrize('elements',DragAndDropPage.ELEMENTS_DATA)
def test_drag_and_drop_to_empty_space_returns_elements_back(open_main_page, drag_and_drop_page, elements):
    drag_and_drop_page.move_element(elements['attribute'],drag_and_drop_page.TEST_FILE_FOR_EMPTY_PLACE)
    drag_and_drop_page.check_the_number_of_entries(drag_and_drop_page.BEGIN_ZONE_ITEMS,4)
