# ==========================================
# POSITIVE SCENARIOS
# ==========================================
def test_use_simple_iframe(open_main_page, frame_page):
    frame_page.click_on_simple_frame(frame_page.FRAME_SIMPLE,frame_page.FRAME_BTN)
    frame_page.check_iframe_text(frame_page.FRAME_SIMPLE,frame_page.FRAME_RESULT,'✓ Кнопка нажата!')

def test_open_frame_in_frame(page,open_main_page, frame_page):
    frame_page.enter_frame_in_frame(frame_page.PARENT_FRAME,frame_page.CHILD_FRAME,frame_page.CHILD_FRAME_BTN)
    frame_page.check_iframe_in_iframe(frame_page.PARENT_FRAME,frame_page.CHILD_FRAME,frame_page.CHILD_RESULT,'✓ Вложенная кнопка нажата!')
# ==========================================
# NEGATIVE SCENARIOS
# ==========================================