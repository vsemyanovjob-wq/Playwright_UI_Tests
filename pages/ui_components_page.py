from .base_page import BasePage

class UiComponents(BasePage):
    # Локаторы Accordion / Collapsible
    DROP_DOWN_DATA = [
        {'name': 'Selenium','Locator': '[onclick="toggleAccordion(\'accordion1\')"]','content_locator':'#accordion1','text': 'Selenium — это инструмент для'},
        {'name': 'Playwright', 'Locator': '[onclick="toggleAccordion(\'accordion2\')"]','content_locator':'#accordion2','text': 'Playwright — современный фреймворк'},
        {'name': 'Cypress', 'Locator': '[onclick="toggleAccordion(\'accordion3\')"]','content_locator':'#accordion3','text': 'Cypress — это fast, easy и reliable testing'},
        {'name': 'Appium', 'Locator': '[onclick="toggleAccordion(\'accordion4\')"]','content_locator':'#accordion4','text': 'Appium — это open-source инструмент'}
    ]


    # Локаторы Multi-step Forms / Wizard
    WIZARD_NAME = '#wizardFirstName'
    WIZARD_LAST_NAME = '#wizardLastName'
    WIZARD_EMAIL = '#wizardEmail'
    WIZARD_PHONE = '#wizardPhone'
    WIZARD_RESULT = '#wizardStep3'
    WIZARD_FORM_WITH_RESULT = '#wizardSuccess'
    BTN_NEXT_PAGE_1 = 'button[onclick="nextWizardStep(2)"]'
    BTN_BACK_PAGE_2 = 'button[onclick="prevWizardStep(1)"]'
    BTN_NEXT_PAGE_2 = 'button[onclick="nextWizardStep(3)"]'
    BTN_BACK_PAGE_3 = 'button[onclick="prevWizardStep(2)"]'
    BTN_SUBMIT = 'button[onclick="submitWizard()"]'

   # Локаторы для подтверждения
    EXPECTED = {
        "#confirmFirstName": "Оля",
        "#confirmLastName": "Сергеева",
        "#confirmEmail": "test121@gmail.com",
        "#confirmPhone": "8800-555-3535"
    }
