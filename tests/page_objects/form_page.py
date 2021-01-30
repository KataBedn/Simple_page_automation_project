from tests.helpers.support_functions import *



form_page_content = 'form-content'
form_page_tab = 'form-header'
first_name = 'fname'
last_name = 'lname'
submit_button = 'formSubmitButton'
firstname_value = 'fname1'
lastname_value = 'surname1'


def click_form_page_tab(driver_instance):
    elem = driver_instance.find_element_by_id(form_page_tab)
    elem.click()

def form_page_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, form_page_content)
    return elem.is_displayed()

def send_correct_keys_to_first_name(driver_instance, firstname_value, first_name):
    wait_for_visibility_of_element(driver_instance, first_name, time_to_wait=1)
    elem = driver_instance.find_element_by_id(first_name)
    elem.send_keys(firstname_value)
    value = firstname_value
    if value == elem.get_attribute("value"):
        return True
    else:
        return False

def send_correct_keys_to_last_name(driver_instance, lastname_value, last_name):
    wait_for_visibility_of_element(driver_instance, last_name, time_to_wait=1)
    elem = driver_instance.find_element_by_id(last_name)
    elem.send_keys(lastname_value)
    value = lastname_value
    if value == elem.get_attribute("value"):
        return True
    else:
        return False

def press_submit(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, submit_button)
    elem.click()

def accept_alert_visible(driver_instance):
    try:
        wait_for_visibility_of_alert(driver_instance, 3)
        alert = driver_instance.switch_to.alert
        alert.accept()
        return True
    except NoSuchElementException:
        return False
