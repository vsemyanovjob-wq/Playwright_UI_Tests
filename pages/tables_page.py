from .base_page import BasePage

class TablesPage(BasePage):
    # Локаторы таблицы Medium a
    ID_MEDIUM_TABLE = "#sortableTable thead th:nth-child(1)"
    CHECK_FIRST_ROW_ID = '#sortableTable tbody tr:nth-child(1) td:nth-child(1)'
    NAME_MEDIUM_TABLE = "#sortableTable thead th:nth-child(2)"
    CHECK_FIRST_ROW_NAME = '#sortableTable tbody tr:nth-child(1) td:nth-child(2)'
    AGE_MEDIUM_TABLE = "#sortableTable thead th:nth-child(3)"
    CHECK_FIRST_ROW_AGE = '#sortableTable tbody tr:nth-child(1) td:nth-child(3)'
    SALARY_MEDIUM_TABLE = "#sortableTable thead th:nth-child(4)"
    CHECK_FIRST_ROW_SALARY = '#sortableTable tbody tr:nth-child(1) td:nth-child(4)'

    # Локаторы таблицы Medium b
    ROW_1_ID_TABLE = '#filterableTableBody tr:nth-child(1) td:nth-child(1)'
    ROW_1_NAME_TABLE = '#filterableTableBody tr:nth-child(1) td:nth-child(2)'
    ROW_1_EMAIL_TABLE = '#filterableTableBody tr:nth-child(1) td:nth-child(3)'
    ROW_1_STATUS = '#filterableTableBody tr:nth-child(1) td:nth-child(4)'
    ALL_STATUS = '#statusFilter'
    INPUT_SEARCH_NAME = '#filterInput'
    SHOWING_ENTRIES = '#filterCount'
    VISIBLE_ROWS = '#visibleRows'

    # Локаторы таблицы HARD
    ID_HARD_TABLE = '#paginatedTable thead th:nth-child(1)'
    PRODUCT_TABLE ='#paginatedTable thead th:nth-child(2)'
    CATEGORY_TABLE = '#paginatedTable thead th:nth-child(3)'
    PRICE_TABLE = '#paginatedTable thead th:nth-child(4)'
    PAGE_SIZE_TABLE = '#pageSize'
    FIRST_PAGE_BTN_TABLE = '#firstPageBtn'
    LAST_PAGE_BTN_TABLE = '#lastPageBtn'
    NEXT_PAGE_BTN_TABLE = '#nextPageBtn'
    PREVIOUS_PAGE_BTN_TABLE = '#prevPageBtn'
    PAGE_START = '#pageStart'
    PAGE_END = '#pageEnd'
    PAGINATION_CONTAINER = '#pageNumbers'
    PAGE_COUNT ='#paginatedTableBody tr'
    SEARCH_NEGATIVE_DATA =[
        ('tada','0'),
        (' ','6'),
        ('aLICE','1'),
        ('alice','1'),
        ('alice@','0'),
        ('1','0'),
        ('Active','0')
    ]
