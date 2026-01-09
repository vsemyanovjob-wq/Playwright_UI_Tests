# Учебный проект по автоматизации Python/Playwright/Pytest ресурса: https://aqa-proka4.org/sandbox/web

## Проект содержит тесты различных UI элеменов: 
- Forms
- Table
- Download files
- Drag & Drop
- Modal Windows
- Frames & Iframe
- Dynamic content
- Hover & tooltips

## Структура проекта
- `pages/` - Page Object Model
- `tests/` - Тесты
- `conftest.py` - Фикстуры
- `requirements.txt` - Зависимости
-  `base_page.py` - базовый класс с общими функциями для работы с элементами (клики, проверка текста, hover и т.д.)

## Как запустить
1. Клонировать репозиторий:
```bash
    git clone <URL репозитория>
   
2. Установка зависимостей:
    pip install -r requirements.txt

3. Установить бразуеры:
    playwright install

4. Запустить тесты:
    pytest --headed -v -s
 
```

