from tests.helpers.support_functions import *
from selenium.webdriver.support.select import Select

dropdown_tab = 'dropdownlist-header'
dropdown_content = 'dropdownlist-content'
dropdown_list = 'dropdown'
dropdown = 'dropdown'


def click_dropdown_tab(driver_instance):
    elem = driver_instance.find_element_by_id(dropdown_tab)
    elem.click()

def dropdown_content_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, dropdown_content)
    return elem.is_displayed()

def choose_option(driver_instance):
    elem_list = Select(driver_instance.find_element_by_id(dropdown_list))
    elem = driver_instance.find_element_by_id(dropdown_list)
    wait_for_visibility_of_element(driver_instance,dropdown_list, time_to_wait=1)
    elem_list.select_by_index(1)
    value = '1'
    if value == elem.get_attribute("value"):
        return True
    else:
        return False

