# ==========================================
# POSITIVE SCENARIOS
# ==========================================
def test_show_tooltip_up_after_hover(open_main_page, hover_page):
    hover_page.show_alert(hover_page.TOOLTIP_BTN1)
    hover_page.check_found_text(hover_page.TOOLTIP_HINT1,'Это всплывающая подсказка!')

def test_show_tooltip_down_after_hover(open_main_page, hover_page):
    hover_page.show_alert(hover_page.TOOLTIP_BTN2)
    hover_page.check_found_text(hover_page.TOOLTIP_HINT2,'Я снизу! 👇')

def test_show_tooltip_menu_after_hover(open_main_page, hover_page):
    hover_page.show_alert(hover_page.HOVER_MENU)
    hover_page.check_found_text(hover_page.HOVER_MENU,'Главная')
    hover_page.check_found_text(hover_page.HOVER_MENU, 'Профиль')
    hover_page.check_found_text(hover_page.HOVER_MENU, 'Настройки')
    hover_page.check_found_text(hover_page.HOVER_MENU, 'Выход')

def test_show_tooltip_on_card_after_hover(open_main_page, hover_page):
    hover_page.show_alert(hover_page.HOVER_CARD)
    hover_page.check_found_text(hover_page.HIDDEN_ELEMENT,'Секретный элемент! 🎉')
# ==========================================
# NEGATIVE SCENARIOS
# ==========================================
def test_tooltip_1_disappears_after_hover_out(open_main_page, hover_page):
    hover_page.show_alert(hover_page.TOOLTIP_BTN1)
    hover_page.check_found_text(hover_page.TOOLTIP_HINT1, 'Это всплывающая подсказка!')
    hover_page.show_alert(hover_page.TOOLTIP_BTN2)
    hover_page.check_tooltip_disappeared(hover_page.TOOLTIP_HINT1)

def test_tooltip_2_disappears_after_hover_out(open_main_page, hover_page):
    hover_page.show_alert(hover_page.TOOLTIP_BTN2)
    hover_page.check_found_text(hover_page.TOOLTIP_HINT2, 'Я снизу! 👇')
    hover_page.show_alert(hover_page.TOOLTIP_BTN1)
    hover_page.check_tooltip_disappeared(hover_page.TOOLTIP_HINT2)

def test_tooltip_3_disappears_after_hover_out(open_main_page, hover_page):
    hover_page.show_alert(hover_page.HOVER_MENU)
    hover_page.check_found_text(hover_page.HOVER_MENU, 'Главная')
    hover_page.check_found_text(hover_page.HOVER_MENU, 'Профиль')
    hover_page.check_found_text(hover_page.HOVER_MENU, 'Настройки')
    hover_page.check_found_text(hover_page.HOVER_MENU, 'Выход')
    hover_page.page.mouse.move(0, 0)
    hover_page.check_tooltip_disappeared(hover_page.HOVER_MENU_HIDDEN)

def test_tooltip_4_disappears_after_hover_out(open_main_page, hover_page):
    hover_page.show_alert(hover_page.HOVER_CARD)
    hover_page.check_found_text(hover_page.HIDDEN_ELEMENT, 'Секретный элемент! 🎉')
    hover_page.page.mouse.move(0, 0)
    hover_page.check_tooltip_disappeared(hover_page.HIDDEN_ELEMENT)







