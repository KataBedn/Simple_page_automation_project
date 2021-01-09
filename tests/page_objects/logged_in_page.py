from tests.helpers.support_functions import *

logged_in_message = 'loggedInMessage'

def logged_in_message_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, logged_in_message)
    return elem.is_displayed()


