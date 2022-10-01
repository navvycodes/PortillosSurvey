from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import vars


def run_survey(code_split_up):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),chrome_options=options)
    browser.get(vars.PORTILLOS_SURVEY_URL)
    browser.maximize_window()

    for code_counter in range(1, 8):
        id_name = vars.CODE_SPLIT_UP_START + str(code_counter)
        CN = browser.find_element(By.ID, id_name)
        CN.send_keys(code_split_up[code_counter])
    start_survey = browser.find_element(By.ID, vars.BUTTON_SUBMIT_ID)
    start_survey.click()

    validation_code = browser.find_elements(By.CLASS_NAME, vars.FREE_REWARD_CLASS_NAME)
    while len(validation_code) == 0:
        all_elements = browser.find_elements(By.CLASS_NAME, vars.SURVEY_BUTTONS_CLASS)
        number_of_elements = len(all_elements)
        if number_of_elements >= 5:
            for i in range(0, number_of_elements, 5):
                all_elements[i].click()
        elif 4 >= number_of_elements > 1:
            all_elements[1].click()
        else:
            my_elements = browser.find_elements(By.ID, vars.SELECT_DROPDOWN_ID)
            if len(my_elements) == 1:
                new_select = Select(my_elements[0])
                new_select.select_by_index(0)
        next_page = browser.find_element(By.ID, vars.BUTTON_SUBMIT_ID)
        next_page.click()
        validation_code = browser.find_elements(By.CLASS_NAME, vars.FREE_REWARD_CLASS_NAME)

    free_reward_code = validation_code[0].text
    print("Automation Finished")
    return str(free_reward_code)
