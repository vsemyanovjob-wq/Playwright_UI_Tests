from .base_page import BasePage

class DragAndDropPage(BasePage):
    # Локаторы: простой Drag & Drop Medium
    ELEMENTS_DATA = [
        {'attribute': '[data-item="item1"]', 'name': 'первый элемент'},
        {'attribute': '[data-item="item2"]', 'name': 'второй элемент'},
        {'attribute': '[data-item="item3"]', 'name': 'третий элемент'},
        {'attribute': '[data-item="item4"]', 'name': 'четвертый элемент'},
    ]
    TEST_FILE_FOR_EMPTY_PLACE = "button[onclick*='drag1']"

    BEGIN_ZONE = '#availableItems'
    ENDS_ZONE = '#selectedItems'
    BEGIN_ZONE_ITEMS = '#availableItems [data-item]'
    ENDS_ZONE_ITEMS = '#selectedItems [data-item]'

    # Локаторы: сортировка списка Medium
    LIST_DATA = [
        {'attribute': '[data-position="1"]', 'name': 'позиция 1'},
        {'attribute': '[data-position="2"]', 'name': 'позиция 2'},
        {'attribute': '[data-position="3"]', 'name': 'позиция 3'},
        {'attribute': '[data-position="4"]', 'name': 'позиция 4'},
        {'attribute': '[data-position="5"]', 'name': 'позиция 5'},
    ]
    SORT_LIST_CONTAINER = '#sortableList'

    # Локаторы: Перетаскивание между контейнерами Hard
    CONTAINER_TO_DO = '#todoContainer'
    CONTAINER_IN_PROGRESS = '#progressContainer'
    CONTAINER_DONE = '#doneContainer'

    ITEMS_IN_TODO = '#todoContainer [data-item]'
    ITEMS_IN_PROGRESS = '#progressContainer [data-item]'
    ITEMS_IN_DONE = '#doneContainer [data-item]'

    TASK_CREATE_DESIGN = '[data-task="task1"]'
    TASK_WRITE_TEST = '[data-task="task2"]'
    TASK_COD_REVIEW = '[data-task="task3"]'
    TASK_MAKE_API = '[data-task="task4"]'
    TASK_BASE_DATE = '[data-task="task5"]'

    LIST_WITH_CASES = ['Разработка API','Создать дизайн', 'Написать тесты','Код ревью','База данных']

