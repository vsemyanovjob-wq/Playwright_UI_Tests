from .base_page import BasePage

class FramesPage(BasePage):
    # Локаторы iframe Hard
    FRAME_SIMPLE = '#simpleFrame'
    FRAME_BTN = '#iframeButton'
    FRAME_RESULT = '#iframeResult'


    # Локаторы Frame in Frame
    PARENT_FRAME = '#parentFrame'
    PARENT_FRAME_BTN = '#parentButton'
    CHILD_FRAME = '#childFrame'
    CHILD_FRAME_BTN = '#childButton'
    CHILD_RESULT = '#childResult'