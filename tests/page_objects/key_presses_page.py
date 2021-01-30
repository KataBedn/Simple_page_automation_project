from tests.helpers.support_functions import *
from selenium.webdriver.common.keys import Keys


key_presses_tab = 'keypresses-header'
key_presses_content = 'keypresses-content'
input = 'target'
message = 'keyPressResult'



def click_key_presses_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, key_presses_tab)
    elem = driver_instance.find_element_by_id(key_presses_tab)
    elem.click()


def key_presses_content_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, key_presses_content)
    return elem.is_displayed()


def enter_and_verify_key(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, input)
    message_elem = driver_instance.find_element_by_id(message)
    elem.send_keys(Keys.TAB)
    value = "You entered: TAB"
    if value == message_elem.text:
        return True
    else:
        return False

