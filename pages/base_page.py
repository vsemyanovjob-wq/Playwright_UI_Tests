from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click_on_element_btn(self, locator: str):
        # Клик по элементу
        element = self.page.locator(locator)
        element.wait_for(state='visible')
        element.click()

    def enter_frame_in_frame(self,locator_frame_parent: str, locator_frame_child: str, btn_in_frame: str):
        # Поиск элемента во фрейме
        parent_frame = self.page.frame_locator(locator_frame_parent)
        child_frame = parent_frame.frame_locator(locator_frame_child)
        child_frame.locator(btn_in_frame).click()

    def click_on_simple_frame(self, locator_frame: str, locator_btn: str):
        # Клик на кнопку во фрейме
        locator_frame = self.page.frame_locator(locator_frame)
        locator_frame.locator(locator_btn).click()

    def select_text_in_dropdown(self, locator: str, text: str):
        # Выбрать элемент в дропдауне
        element = self.page.locator(locator)
        element.focus()
        element.select_option(label=text)

    def fill_input(self, locator: str, name: str):
        # Ввести в поле текст
        element = self.page.locator(locator)
        self.page.locator(locator).fill("")
        element.fill(name)

    def check_active_page_number(self, locator: str, page_number: str):
        # Выбрать номер страницы
        active_button = self.page.locator(locator).locator(f"button.bg-blue-600:has-text('{page_number}')")
        expect(active_button).to_be_visible()

    def check_field_validation_error(self, locator: str):
        # Проверка хинта при пропуске пустого поля
        element = self.page.locator(locator).first
        expect(element).to_have_js_property("validity.valueMissing", True)

    def check_found_text(self, locator: str, text: str):
        # Проверка, что есть нужный текст
        expect(self.page.locator(locator)).to_contain_text(text)

    def check_found_texts_in_list(self, container: str, text: str):
        # Поиск текста в контейнере
        locator = self.page.locator(container)
        locator.wait_for(state='visible')
        container_text = locator.inner_text()
        assert text in container_text, f"'{text}'"

    def check_the_number_of_entries(self, locator: str, email_input: int):
        # Проверка количества элементов
        element = self.page.locator(locator)
        if email_input > 0:
            element.last.wait_for(state="attached")
        expect(element).to_have_count(email_input)

    def check_element_is_hidden(self,locator: str):
        # Проверка, что элемент исчез
        element = self.page.locator(locator)
        expect(element).to_be_hidden(timeout=3000)

    def check_element_is_visible(self,locator: str):
        # Проверка, что элемент появился
        element = self.page.locator(locator)
        expect(element).to_be_visible(timeout=5000)

    def check_iframe_text(self, locator_frame: str, container_result: str, text: str):
        # Поиск текста во фрейме
        frame = self.page.frame_locator(locator_frame)
        expect(frame.locator(container_result)).to_have_text(text)

    def check_iframe_in_iframe(self,parent_locator_frame: str, child_locator_frame: str, target_locator: str, final_text: str):
        # Поиск текста вложенного фрейма
        parent_frame = self.page.frame_locator(parent_locator_frame)
        child_frame = parent_frame.frame_locator(child_locator_frame)
        expect(child_frame.locator(target_locator)).to_have_text(final_text)

    def check_on_attribute(self,locator: str, attribute: str,expected_value: str):
        # Проверка по аттрибуту
        element = self.page.locator(locator)
        expect(element).to_have_attribute(attribute,expected_value)

    def check_dynamic_progress(self,locator: str, expected_value: str):
        # ожидание прогресс бара
        element = self.page.locator(locator)
        element.wait_for(state='visible')
        expect(element).to_have_text(expected_value)

    def check_disabled_btn(self,locator: str):
        # Проверка, что кнопка не активна
        element = self.page.locator(locator)
        expect(element).to_be_disabled()

    def check_tooltip_disappeared(self,locator: str):
        # Проверка, что элемент скрыт(путём проверки opacity)
        element = self.page.locator(locator)
        expect(element).to_have_css('opacity', '0')

    def refresh_page(self):
        # Обновить страницу
        self.page.reload()

    def move_element(self,locator: str, window_locator):
        # Перемещение элемента
        element = self.page.locator(locator)
        place_to_move = self.page.locator(window_locator)
        element.wait_for(state='visible')
        element.drag_to(place_to_move)

    def get_list_order(self, container_selector: str) -> list[str]:
        # Сортировка списка
        return self.page.locator(f"{container_selector} > *").all_text_contents()

    def change_element(self, item_a: str, item_b: str):
        #  Изменить элементы местами
        self.page.locator(item_a).drag_to(self.page.locator(item_b))

    def scroll_into_last_element(self,locator: str, item_selector: str):
        # Скролл к последнему элементу
        last_item = self.page.locator(locator).locator(item_selector).last
        last_item.scroll_into_view_if_needed()
        self.page.wait_for_timeout(1000)

    def choose_one_file(self, button_locator: str, file_path: str):
        # загрузка одного файла
        with self.page.expect_file_chooser() as info:
            self.page.locator(button_locator).click()
        info.value.set_files(file_path)

    def choose_two_files(self, button_locator: str, file_path_1, file_path_2: str,):
        # Загрузка двух файлов
        with self.page.expect_file_chooser() as info:
            self.page.locator(button_locator).click()
        info.value.set_files([file_path_1, file_path_2])

    def show_alert(self,locator: str):
        # Наведение на элемент с тултипом
        self.page.locator(locator).hover()






