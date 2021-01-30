from tests.helpers.support_functions import *
from time import sleep

date_picker_tab = 'datepicker-header'
date_picker_content = 'datepicker-content'
date_field = '#start'


def click_date_picker_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, date_picker_tab)
    elem = driver_instance.find_element_by_id(date_picker_tab)
    elem.click()


def date_picker_content_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, date_picker_content)
    return elem.is_displayed()


def insert_correct_data(driver_instance):
    elem = driver_instance.find_element_by_css_selector(date_field)
    elem.send_keys('10')
    elem.send_keys('02')
    value = '10.02.2020'
    if value == elem.text:
        return True
    else:
        return False


def insert_incorrect_data(driver_instance):
    elem = driver_instance.find_element_by_css_selector(date_field)
    print(elem.text)
    elem.send_keys('33')
    elem.send_keys('15')
    value = '33.15.2020'
    if value != elem.text:
        return True
    else:
        return False