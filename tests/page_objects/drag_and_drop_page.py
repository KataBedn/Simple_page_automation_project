from tests.helpers.support_functions import *
from selenium.webdriver import ActionChains

drag_and_drop_tab = 'draganddrop-header'
drag_and_drop_content = 'draganddrop-content'
elem_a = 'column-a'
elem_b = 'column-b'


def click_drag_and_drop_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, drag_and_drop_tab)
    elem = driver_instance.find_element_by_id(drag_and_drop_tab)
    elem.click()


def drag_and_drop_content_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, drag_and_drop_content)
    return elem.is_displayed()


def drag_element_a_over_b(driver_instance):
    move_from = wait_for_visibility_of_element(driver_instance, elem_a)
    move_to = wait_for_visibility_of_element(driver_instance, elem_b)
    print(move_from.text)
    ActionChains(driver_instance).drag_and_drop(move_from, move_to).perform()
    print(move_from.text)
    value = "B"
    if value == move_from.text:
        return True
    else:
        return False


