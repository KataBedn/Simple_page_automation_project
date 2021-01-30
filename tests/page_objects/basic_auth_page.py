from tests.helpers.support_functions import *

basic_auth_tab = 'basicauth-header'
basic_auth_content = 'basicauth-content'
input_username = 'ba_username'
input_password = 'ba_password'
login_button = '//*[@id="content"]/button'
invalid_credentials_message = 'Invalid credentials'


def click_basic_auth_tab(driver_instance):
    elem = driver_instance.find_element_by_id(basic_auth_tab)
    elem.click()


def basic_auth_content_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, basic_auth_content)
    return elem.is_displayed()


def send_correct_credentials_to_input(driver_instance):
    elem_username = driver_instance.find_element_by_id(input_username)
    elem_username.send_keys('admin')
    elem_password = driver_instance.find_element_by_id(input_password)
    elem_password.send_keys('admin')


def press_login(driver_instance):
    elem = driver_instance.find_element_by_xpath(login_button)
    elem.click()


def send_incorrect_credentials_to_input(driver_instance):
    elem_username = driver_instance.find_element_by_id(input_username)
    elem_username.send_keys('test')
    elem_password = driver_instance.find_element_by_id(input_password)
    elem_password.send_keys('test')


def invalid_credentials_message_displayed(driver_instance):
    elem = driver_instance.find_element_by_xpath("//p[contains(text(),'Invalid credentials')]")
    return elem.is_displayed()



