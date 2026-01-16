# MyProject - UI Automation Testing with Playwright & Pytest

Тестовый проект на Python, демонстрирующий навыки автоматизации UI-тестирования с использованием **Pytest** и **Playwright**.

Тестируемый сайт: https://aqa-proka4.org/sandbox/web

Проект содержит: ```99 тестов```

## Описание

Проект для автоматизации UI-тестирования веб-приложений с использованием Page Object Model (POM). Включает тесты для различных UI-компонентов и сценариев

---
##  Структура проекта
- `pages/` — реализация Page Object Model (POM)  
- `tests/` — тестовые сценарии  
- `conftest.py` — фикстуры pytest  
- `base_page.py` — базовый класс с общими методами для UI-тестов  
- `requirements.txt` — зависимости проекта

---
##  Используемые технологии
- Python  
- Pytest  
- Playwright  
- Page Object Model (POM)
- Allure Reports

---
## Браузер для тестирования

- Chromium (Google Chrome) - основной браузер для тестирования
---

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone git@github.com:vsemyanovjob-wq/MyProject.git
    cd MyProject
    ```
2. Установите зависимости:
    ```bash
    python -m venv .venv
    source .venv/bin/activate    # Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Установите браузеры для Playwright:
    ```bash
    playwright install
    ```
   
## Отчёты Allure (опционально)
1. Установите Allure CLI
    ```bash
    scoop install allure
    ```
2. Установите зависимость в проекте:
    ```bash
    pip install allure-pytest
    ```
3. Запуск тестов:
    ```bash
    pytest --alluredir=allure-results
    allure serve allure-results
    ```

##  Запуск тестов

Запуск всех тестов:
    ```
    pytest/ui -s -v
    ```

Запуск тестов с отображением браузера:
    ```
    pytest --headed -v -s
    ```

##  Пример теста

Пример UI-теста с использованием Page Object Model:
```
def test_tooltip_1_disappears_after_hover_out(open_main_page, hover_page):
    hover_page.show_alert(hover_page.TOOLTIP_BTN1)
    hover_page.check_found_text(hover_page.TOOLTIP_HINT1,'Это всплывающая подсказка!')
    hover_page.show_alert(hover_page.TOOLTIP_BTN2)
    hover_page.check_tooltip_disappeared(hover_page.TOOLTIP_HINT1)
```

##  Возможности проекта
Проект включает тесты для проверки различных UI-элементов:
- Forms
- Tables
- Download files
- Drag & Drop
- Modal windows
- Frames & iFrame
- Dynamic content
- Hover & tooltips


##  Контакты
GitHub: https://github.com/vsemyanovjob-wq

Email: vsemyanovjob@gmail.com

Telegram: @StDeform
