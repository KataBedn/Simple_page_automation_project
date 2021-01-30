from tests.helpers.support_functions import *

iframe_tab = '#iframe-header'
iframe_content = 'iframe-content'
button_1 = 'simpleButton1'
button_2 = 'simpleButton2'
message = 'whichButtonIsClickedMessage'


def click_iframe_tab(driver_instance):
    elem = wait_for_visibility_of_element_css(driver_instance, iframe_tab)
    elem.click()


def iframe_content_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, iframe_content)
    return elem.is_displayed()


def press_button_1(driver_instance):
    driver_instance.switch_to.frame(driver_instance.find_element_by_tag_name("iframe"))
    elem = driver_instance.find_element_by_id(button_1)
    elem.click()
    which_button = driver_instance.find_element_by_id(message)
    value = "Button 1 was clicked!"
    if value == which_button.text:
        return True
    else:
        return False


def press_button_2(driver_instance):
    driver_instance.switch_to.frame(driver_instance.find_element_by_tag_name("iframe"))
    elem = driver_instance.find_element_by_id(button_2)
    elem.click()
    which_button = driver_instance.find_element_by_id(message)
    value = "Button 2 was clicked!"
    if value == which_button.text:
        return True
    else:
        return False
