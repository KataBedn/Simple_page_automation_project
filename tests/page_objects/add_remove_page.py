from tests.helpers.support_functions import *

add_remove_element_tab = 'addremoveelements-header'
add_remove_element_content = 'addremoveelements-content'
new_element = '//*[@id="addremoveelements-content"]/div/div/button'
added_element = '//*[@id="elements"]/button[1]'


def click_add_and_remove_tab(driver_instance):
    elem = driver_instance.find_element_by_id(add_remove_element_tab)
    elem.click()

def add_and_remove_content_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, add_remove_element_content)
    return elem.is_displayed()

def add_new_element(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, new_element)
    elem = driver_instance.find_element_by_xpath(new_element)
    elem.click()

def delete_element(driver_instance):
    elem = driver_instance.find_element_by_xpath(added_element)
    elem.click()
    wait_for_invisibility_of_element_by_xpath(driver_instance, added_element)


def element_invisible(driver_instance):
    try:
        wait_for_invisibility_of_element_by_xpath(driver_instance, added_element)
        return True
    except NoSuchElementException:
        return False

def element_visible(driver_instance):
    try:
        wait_for_visibility_of_element_xpath(driver_instance, added_element)
        return True
    except NoSuchElementException:
        return False