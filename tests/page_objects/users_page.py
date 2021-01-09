from tests.helpers.support_functions import *

container = 'container'

def error_info_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, container)
    return elem.is_displayed()